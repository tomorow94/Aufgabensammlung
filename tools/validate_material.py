"""Prüft Lehrmaterial und ausführbare Konsolenbeispiele ohne zusätzliche Python-Pakete.

Vom Repository-Wurzelordner: python tools/validate_material.py --compile
Zuvor die Adressbuch-Solution in Release bauen, damit deren Referenzen verfügbar sind:
dotnet build Beispiele/Adressbuch/Adressbuch.slnx --configuration Release
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import tempfile
import unicodedata
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
FRAGMENT_DOCUMENTS = {"Stufe3/A01_KlassenUndStruktur.md"}


def markdown_anchors(text: str) -> set[str]:
    """Abschnittsanker der hier verwendeten ATX-Überschriften (GitHub-Regeln)."""
    anchors: set[str] = set()
    in_code = False
    for line in text.splitlines():
        if re.match(r"^\s*`{3,}", line):
            in_code = not in_code
            continue
        if in_code:
            continue
        heading = re.match(r"^#{1,6}\s+(.+?)(?:\s+#+)?\s*$", line)
        if heading:
            title = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", heading.group(1)).lower()
            title = re.sub(r"\*+|`+|~+", "", title)
            title = re.sub(r"(?<!\w)_([^_]+)_(?!\w)", r"\1", title)
            base = "".join(c for c in title if c in " -_" or unicodedata.category(c)[0] in "LNM")
            base = base.replace(" ", "-")
            anchor = base
            suffix = 0
            while anchor in anchors:
                suffix += 1
                anchor = f"{base}-{suffix}"
            anchors.add(anchor)
    # Benutzerdefinierte Anker zählen nicht für die Nummerierung der Überschriften.
    for tag in re.findall(r"<a\s+[^>]*>", text):
        anchors.update(re.findall(r'(?:name|id)=["\']([^"\']+)["\']', tag))
    return anchors


def exact_local_case(path: Path) -> bool:
    """Erkennt auch unter Windows Pfade, die auf Linux/GitHub falsch wären."""
    normalized = Path(os.path.normpath(path))
    try:
        parts = normalized.relative_to(ROOT).parts
    except ValueError:
        return False
    current = ROOT
    for part in parts:
        if part not in {entry.name for entry in current.iterdir()}:
            return False
        current /= part
    return True


def curriculum_check() -> None:
    """Prüft Lernziele, Pflichtreihenfolge und die Trennung von Bonusaufgaben."""
    tasks = {p.resolve(): p.read_text(encoding="utf-8") for p in sorted(ROOT.glob("Stufe*/A*.md"))}
    required = [p for p, text in tasks.items() if "**Status:** Pflicht im Lernfaden." in text]
    bonus = [p for p, text in tasks.items() if "**Status:** Bonus (optional;" in text]
    errors = []
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    listed = {
        (ROOT / unquote(target.split("#", 1)[0])).resolve()
        for target in re.findall(r"\]\(([^\s)]+)\)", readme)
        if not re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target)
    }
    for path, text in tasks.items():
        label = path.relative_to(ROOT)
        if path not in required and path not in bonus:
            errors.append(f"{label}: Pflicht-/Bonusstatus fehlt")
        if path in required and path in bonus:
            errors.append(f"{label}: widersprüchlicher Status")
        metadata = re.search(r"^## Einordnung und Lernziele\n(.+?)(?=^## )", text, re.M | re.S)
        if metadata is None:
            errors.append(f"{label}: Einordnung fehlt")
            continue
        block = metadata.group(1)
        for field in ("Voraussetzungen", "Intention", "Lernziele", "Weiter im Pflichtpfad"):
            if f"**{field}:**" not in block:
                errors.append(f"{label}: {field} fehlt")
        if not re.search(r"^\*\*Intention:\*\* \S.+$", block, re.M):
            errors.append(f"{label}: Intention ist leer")
        if len(re.findall(r"^- Du kannst .+", block, re.M)) < 2:
            errors.append(f"{label}: prüfbare Lernziele fehlen")
        if "Hinweis 1: Denkanstoß" not in text or "Hinweis 2: Vorgehensweise" not in text:
            errors.append(f"{label}: gestufte Hinweise fehlen")
        if "## Passende Lernquellen" not in text:
            errors.append(f"{label}: Leseempfehlung fehlt")
        if path not in listed:
            errors.append(f"{label}: nicht in README verlinkt")
        if path in bonus and "Bonus A" not in text.splitlines()[0]:
            errors.append(f"{label}: Bonustitel fehlt")
        for section in re.split(r"(?=^## )", text, flags=re.M):
            if section.startswith("## Bonus"):
                if "**Intention:**" not in section or "**Lernziel:**" not in section:
                    errors.append(f"{label}: Bonusabschnitt ohne Intention/Lernziel")
        prerequisites = re.search(r"^\*\*Voraussetzungen:\*\* (.+)$", block, re.M)
        if prerequisites and path in required:
            for target in re.findall(r"\]\(([^\s)]+)\)", prerequisites.group(1)):
                dependency = (path.parent / unquote(target)).resolve()
                if dependency in bonus:
                    errors.append(f"{label}: Pflichtaufgabe setzt Bonus voraus")
                if dependency in required and required.index(dependency) >= required.index(path):
                    errors.append(f"{label}: Voraussetzung liegt nicht vorher im Pflichtpfad")
        onward = re.search(r"^\*\*Weiter im Pflichtpfad:\*\* (.+)$", block, re.M)
        if onward:
            targets = re.findall(r"\]\(([^\s)]+)\)", onward.group(1))
            resolved = [(path.parent / unquote(t)).resolve() for t in targets]
            if any(p not in required for p in resolved):
                errors.append(f"{label}: Fortsetzung ist keine Pflichtaufgabe")
            if path in required:
                index = required.index(path)
                expected = required[index + 1:index + 2]
                if resolved != expected:
                    errors.append(f"{label}: Fortsetzung überspringt einen Pflichtschritt")
    expected_count = f"{len(required)} Pflichtaufgaben und {len(bonus)} eigenständige Bonus-Aufgaben"
    if expected_count not in readme:
        errors.append("README: Aufgabenanzahl stimmt nicht")
    readme_required = [
        (ROOT / unquote(target.split("#", 1)[0])).resolve()
        for target in re.findall(r"\]\(([^\s)]+)\)", readme)
        if not re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target)
        and (ROOT / unquote(target.split("#", 1)[0])).resolve() in required
    ]
    if readme_required != required:
        errors.append("README: Pflichtaufgaben fehlen, sind doppelt oder stehen nicht in Lernreihenfolge")
    if errors:
        raise RuntimeError("\n".join(errors))
    print(f"Lernfaden, Lernziele und Bonus-Trennung: OK ({len(required)} Pflicht, {len(bonus)} Bonus)")


def markdown_check() -> list[tuple[Path, str]]:
    examples = []
    errors = []
    anchor_cache: dict[Path, set[str]] = {}
    links = 0
    section_links = 0
    for path in sorted(ROOT.rglob("*.md")):
        if any(part in {".git", ".build", "bin", "obj"} for part in path.parts):
            continue
        text = path.read_text(encoding="utf-8")
        in_code = False
        language = ""
        code = []
        details = 0
        for number, line in enumerate(text.splitlines(), 1):
            fence = re.match(r"^\s*(`{3,})([^`]*)$", line)
            if fence:
                if in_code:
                    if language == "csharp":
                        examples.append((path, "\n".join(code)))
                    code = []
                    in_code = False
                else:
                    in_code = True
                    language = fence.group(2).strip()
                continue
            if in_code:
                code.append(line)
                continue
            details += len(re.findall(r"<details(?:\s[^>]*)?>", line))
            details -= line.count("</details>")
            if details < 0:
                errors.append(f"{path.relative_to(ROOT)}:{number}: unerwartetes </details>")
                details = 0
            for target in re.findall(r"\]\(([^\s)]+)(?:\s+[^)]*)?\)", line):
                if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("//"):
                    continue
                local, _, fragment = target.strip("<>").partition("#")
                local = unquote(local)
                destination = path if not local else (
                    (ROOT / local.lstrip("/")) if local.startswith("/") else (path.parent / local)
                )
                links += 1
                if not destination.exists():
                    errors.append(f"{path.relative_to(ROOT)}:{number}: defekter Link {target}")
                    continue
                if not exact_local_case(destination):
                    errors.append(f"{path.relative_to(ROOT)}:{number}: falsche Pfadschreibweise {target}")
                if fragment and destination.suffix.lower() == ".md":
                    section_links += 1
                    if destination not in anchor_cache:
                        anchor_cache[destination] = markdown_anchors(destination.read_text(encoding="utf-8"))
                    if unquote(fragment) not in anchor_cache[destination]:
                        errors.append(f"{path.relative_to(ROOT)}:{number}: fehlender Abschnitt {target}")
        if in_code:
            errors.append(f"{path.relative_to(ROOT)}: nicht geschlossener Codeblock")
        if details:
            errors.append(f"{path.relative_to(ROOT)}: nicht geschlossenes <details>")
        if path.parent.name.startswith("Stufe") and "## Selbst prüfen" not in text:
            errors.append(f"{path.relative_to(ROOT)}: Lernkontrolle fehlt")
    if errors:
        raise RuntimeError("\n".join(errors))
    print(f"Lokale Verweise inklusive Pfadschreibweise: OK ({links}, davon {section_links} Abschnittsverweise)")
    return examples


def dotnet_references() -> tuple[Path, list[Path]]:
    sdks = subprocess.check_output(["dotnet", "--list-sdks"], text=True)
    entries = re.findall(r"^(10\.\d+\.\d+) \[(.+)\]$", sdks, re.M)
    if not entries:
        raise RuntimeError(".NET-10-SDK fehlt.")
    version, directory = max(entries, key=lambda entry: tuple(map(int, entry[0].split("."))))
    sdk = Path(directory) / version
    refs: dict[str, Path] = {}
    for pack in ("Microsoft.NETCore.App.Ref", "Microsoft.AspNetCore.App.Ref"):
        choices = [p for p in (sdk.parent.parent / "packs" / pack).glob("10.*") if p.is_dir()]
        selected = max(choices, key=lambda p: tuple(map(int, p.name.split("."))))
        for dll in (selected / "ref" / "net10.0").glob("*.dll"):
            refs[dll.name] = dll
    # Referenzen aus dem vorher gebauten Abschlussprojekt für SQL- und EF-Beispiele.
    assets_path = ROOT / "Beispiele/Adressbuch/Api/obj/project.assets.json"
    if not assets_path.exists():
        raise RuntimeError("Zuerst dotnet build Beispiele/Adressbuch/Adressbuch.slnx --configuration Release ausführen.")
    assets = json.loads(assets_path.read_text(encoding="utf-8"))
    for target in assets["targets"].values():
        for name, library in target.items():
            package_path = assets["libraries"][name].get("path", "")
            if library.get("type") != "package":
                continue
            for relative in library.get("compile", {}):
                if not relative.endswith(".dll"):
                    continue
                for folder in assets["packageFolders"]:
                    dll = Path(folder) / package_path / relative
                    if dll.exists():
                        refs.setdefault(dll.name, dll)
                        break
    for project in ("Core", "Data"):
        dll = ROOT / f"Beispiele/Adressbuch/{project}/bin/Release/net10.0/{project}.dll"
        if not dll.exists():
            raise RuntimeError("Die Referenzanwendung muss in Release gebaut werden.")
        refs[dll.name] = dll
    return sdk / "Roslyn/bincore/csc.dll", list(refs.values())


class Compiler:
    def __init__(self, directory: Path):
        self.directory = directory
        self.csc, self.refs = dotnet_references()
        self.index = 0

    def compile(self, source: str, probe: str | None = None) -> Path:
        name = f"example{self.index}"
        self.index += 1
        cs = self.directory / f"{name}.cs"
        cs.write_text(source + ("\n" + probe if probe else ""), encoding="utf-8")
        dll = self.directory / f"{name}.dll"
        args = ["-nologo", "-target:exe", "-nullable:enable", f"-out:{dll}"]
        if probe:
            args.append("-main:ReviewProbe")
        args += [f"-r:{ref}" for ref in self.refs] + [str(cs)]
        rsp = self.directory / f"{name}.rsp"
        rsp.write_text("\n".join(f'"{arg}"' for arg in args), encoding="utf-8")
        result = subprocess.run(["dotnet", str(self.csc), f"@{rsp}"], capture_output=True, text=True)
        if result.returncode:
            raise RuntimeError(result.stdout + result.stderr)
        dll.with_suffix(".runtimeconfig.json").write_text(json.dumps({"runtimeOptions": {
            "tfm": "net10.0", "frameworks": [
                {"name": "Microsoft.NETCore.App", "version": "10.0.0"},
                {"name": "Microsoft.AspNetCore.App", "version": "10.0.0"}
            ]}}), encoding="utf-8")
        return dll

    @staticmethod
    def run(dll: Path, input_text: str = "") -> str:
        result = subprocess.run(["dotnet", str(dll)], input=input_text, capture_output=True, text=True, timeout=30)
        if result.returncode:
            raise RuntimeError(result.stdout + result.stderr)
        return result.stdout


def check(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def compile_and_probe(examples: list[tuple[Path, str]]) -> None:
    with tempfile.TemporaryDirectory(prefix="material-check-") as temporary:
        compiler = Compiler(Path(temporary))
        sources = {}
        binaries = {}
        for path, source in examples:
            relative = path.relative_to(ROOT).as_posix()
            if relative in FRAGMENT_DOCUMENTS:
                continue
            if not re.search(r"\bclass\s+", source) or not re.search(r"static\s+(?:async\s+)?(?:void|int|Task(?:<[^>]+>)?)\s+Main\s*\(", source):
                continue
            try:
                binaries[relative] = compiler.compile(source)
                sources[relative] = source
            except RuntimeError as error:
                raise RuntimeError(f"{relative}:\n{error}") from error
        print(f"Vollständige Konsolenbeispiele kompiliert: {len(binaries)}")

        fibonacci = binaries["Stufe1/A10_Fibonacci.md"]
        check(compiler.run(fibonacci, "1\n").strip().endswith("0"), "Fibonacci: Sonderfall 1 falsch.")
        check(compiler.run(fibonacci, "47\n").strip().endswith("1836311903"), "Fibonacci: Überlauf/Grenze falsch.")
        check("Bitte" in compiler.run(fibonacci, "48\n"), "Fibonacci: unzulässiger Bereich akzeptiert.")

        pyramid_source = sources["Stufe2/A06_FibonacciPyramide.md"]
        probe = r'''class ReviewProbe { static void Main() {
            var method = typeof(Program).GetMethod("CalculateFibonacci", System.Reflection.BindingFlags.Static | System.Reflection.BindingFlags.NonPublic)!;
            var single = (System.Collections.Generic.List<int>)method.Invoke(null, new object[]{1})!;
            var last = (System.Collections.Generic.List<int>)method.Invoke(null, new object[]{47})!;
            if(single.Count != 1 || single[0] != 0 || last.Count != 47 || last[46] != 1836311903) throw new System.Exception("Fibonacci-Liste falsch.");
        }}'''
        compiler.run(compiler.compile(pyramid_source, probe))
        check("Bitte eine ganze Zahl" in compiler.run(binaries["Stufe3/A04_BesseresMenu.md"], "abc\n1\n0\n"), "Menü beendet sich bei Text.")
        check("Hallo Welt!" in compiler.run(binaries["Stufe3/A04_BesseresMenu.md"], "abc\n1\n0\n"), "Menü reagiert nach Texteingabe nicht mehr.")
        hangman = sources["Stufe4/A02_Hangman.md"].replace("words[Random.Shared.Next(words.Length)]", '"computer"')
        check("Verloren" in compiler.run(compiler.compile(hangman), "a\nb\nf\ng\nh\ni\nj\n"), "Hangman: Niederlage falsch.")
        check("Gewonnen" in compiler.run(compiler.compile(hangman), "C\nc\n1\nab\no\nm\np\nu\nt\ne\nr\n"), "Hangman: Eingabeprüfung/Gewinn falsch.")
        bank_probe = r'''class ReviewProbe { static void Main() {
            var account = new BankAccount("Test");
            if (!account.Deposit(100) || account.Balance != 100 || account.Deposit(-1) || account.Deposit(0) || account.Withdraw(101) || account.Balance != 100 || !account.Withdraw(100) || account.Balance != 0 || account.Withdraw(1)) throw new System.Exception("Kontologik falsch.");
        }}'''
        compiler.run(compiler.compile(sources["Stufe4/A03_Bankkonto.md"], bank_probe))
        compiler.run(binaries["Stufe5/A01_Sortieralgorithmen.md"])
        background_probe = r'''class ReviewProbe { static void Main() {
            var method = typeof(Program).GetMethod("CountPrimes", System.Reflection.BindingFlags.Static | System.Reflection.BindingFlags.NonPublic)!;
            foreach (var test in new[]{(10,4),(100,25)}) {
                int actual = (int)method.Invoke(null, new object[]{test.Item1, System.Threading.CancellationToken.None})!;
                if (actual != test.Item2) throw new System.Exception("Primzahlzählung falsch.");
            }
            try { method.Invoke(null,new object[]{100,new System.Threading.CancellationToken(true)}); throw new System.Exception("Abbruch fehlt."); }
            catch(System.Reflection.TargetInvocationException e) when(e.InnerException is System.OperationCanceledException) { }
        }}'''
        compiler.run(compiler.compile(sources["Stufe4/A04_Hintergrundaufgabe.md"], background_probe))
        print("Grenzfälle geprüft: Fibonacci, Menü, Hangman, Bankkonto, Sortierung und Hintergrundberechnung.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--compile", action="store_true")
    args = parser.parse_args()
    examples = markdown_check()
    curriculum_check()
    print("Markdown, lokale Links, ausklappbare Lösungen und Lernkontrollen: OK")
    if args.compile:
        compile_and_probe(examples)


if __name__ == "__main__":
    main()
