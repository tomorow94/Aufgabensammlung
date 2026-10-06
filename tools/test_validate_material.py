"""Regressionstests für lokale Links und die README-Lernreihenfolge."""
import contextlib
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import validate_material as material


class MaterialCheckTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.patch = patch.object(material, "ROOT", self.root)
        self.patch.start()
        self.addCleanup(self.patch.stop)

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def markdown_check(self):
        with contextlib.redirect_stdout(io.StringIO()):
            return material.markdown_check()

    def test_unicode_formatting_duplicates_and_code_fences(self):
        text = "# **Überblick**\n## _Überblick_\n```md\n## Unsichtbar\n```\n<a name=\"extra\"></a>"
        self.assertEqual({"überblick", "überblick-1", "extra"}, material.markdown_anchors(text))

    def test_self_cross_file_encoded_and_root_links(self):
        self.write("README.md", "# Einstieg\n[Hier](#einstieg)\n[Weiter](Referenzen/Ziele.md#%C3%BCbung)\n")
        self.write("Referenzen/Ziele.md", "# Übung\n[Zurück](/README.md#einstieg)\n")
        self.markdown_check()

    def test_missing_self_anchor_is_rejected(self):
        self.write("README.md", "# Einstieg\n[Fehler](#fehlt)\n")
        with self.assertRaisesRegex(RuntimeError, "fehlender Abschnitt"):
            self.markdown_check()

    def test_missing_cross_file_anchor_is_rejected(self):
        self.write("README.md", "[Fehler](Ziele.md#fehlt)\n")
        self.write("Ziele.md", "# Übung\n")
        with self.assertRaisesRegex(RuntimeError, "fehlender Abschnitt"):
            self.markdown_check()

    def test_missing_file_is_rejected(self):
        self.write("README.md", "[Fehler](Fehlt.md)\n")
        with self.assertRaisesRegex(RuntimeError, "defekter Link"):
            self.markdown_check()

    def test_case_is_checked_independently_of_operating_system(self):
        path = self.write("Referenzen/Ziele.md", "# Ziele\n")
        self.assertTrue(material.exact_local_case(path))
        self.assertFalse(material.exact_local_case(self.root / "referenzen/Ziele.md"))
        self.assertFalse(material.exact_local_case(self.root / "Referenzen/ziele.md"))

    def test_external_links_and_code_examples_are_ignored(self):
        self.write("README.md", "[Extern](https://example.com/#abschnitt)\n```md\n[Skizze](Fehlt.md)\n```\n")
        self.markdown_check()

    def prepare_curriculum(self, reverse=False):
        template = """# Aufgabe
## Einordnung und Lernziele
**Status:** Pflicht im Lernfaden.
**Voraussetzungen:** {previous}
**Intention:** Einen Schritt verstehen.
**Lernziele:**
- Du kannst das Ergebnis erklären.
- Du kannst einen Fehler erkennen.
**Weiter im Pflichtpfad:** {next}
## Selbst prüfen
Hinweis 1: Denkanstoß
Hinweis 2: Vorgehensweise
## Passende Lernquellen
"""
        self.write("Stufe1/A01_Start.md", template.format(previous="Keine.", next="[Weiter](A02_Ende.md)"))
        self.write("Stufe1/A02_Ende.md", template.format(previous="[Start](A01_Start.md)", next="Abschluss."))
        names = ["A01_Start.md", "A02_Ende.md"]
        if reverse:
            names.reverse()
        self.write("README.md", "2 Pflichtaufgaben und 0 eigenständige Bonus-Aufgaben\n" +
                   "\n".join(f"[Aufgabe](Stufe1/{name})" for name in names))

    def test_readme_and_task_navigation_agree(self):
        self.prepare_curriculum()
        with contextlib.redirect_stdout(io.StringIO()):
            material.curriculum_check()

    def test_reversed_readme_learning_order_is_rejected(self):
        self.prepare_curriculum(reverse=True)
        with self.assertRaisesRegex(RuntimeError, "Lernreihenfolge"):
            material.curriculum_check()


if __name__ == "__main__":
    unittest.main()
