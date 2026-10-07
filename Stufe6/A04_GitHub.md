# 🔴 Aufgabe A04: Bestehendes GitHub-Projekt und CI weiterentwickeln

## Einordnung und Lernziele

**Status:** Pflicht im Lernfaden.

**Voraussetzungen:** [Webseite für dasselbe Adressbuch](A03_Webentwicklung.md)

**Intention:** Änderungen im bestehenden Repository nachvollziehbar prüfen und zusammenführen.

**Lernziele:**

- Du kannst Issue, Branch, Diff und Pull Request zu einer Änderung verwenden.
- Du kannst einen Build-Test-Workflow ausführen und einen fehlgeschlagenen Test erkennen.

**Weiter im Pflichtpfad:** [Adressbuch mit Datenbank bereitstellen](A05_Deployment.md)

## Ziel und Voraussetzungen

Dein Menüprojekt wird seit Stufe 3 mit Git verwaltet. Ergänze **in diesem Repository** Dokumentation, Branches, Reviews und automatisierte Prüfungen.

## Anforderungen

1. Prüfe mit `git status`, `git remote -v` und `git branch`, welches Repository du verwendest.
2. Pflege `.gitignore` für `bin`, `obj`, `.vs`, `TestResults`, `node_modules`, `.env` und lokale Buildordner. Zugangsdaten werden nicht eingecheckt.
3. Beschreibe in der README Modell, Startbefehle, Datenbankvorbereitung, Tests und API-Endpunkte.
4. Plane eine Erweiterung als Issue mit überprüfbaren Akzeptanzkriterien.
5. Erstelle einen Branch, implementiere die Änderung und eröffne einen Pull Request. Prüfe Diff und Tests vor dem Zusammenführen.
6. Führe Build und Tests über GitHub Actions aus und passe die Projektpfade an dein Repository an.

## Typischer Ablauf im bestehenden Repository

```shell
git switch -c feature/contact-search
git status
git add README.md
git commit -m "Document contact search"
git push -u origin feature/contact-search
```

Stage die tatsächlich geänderten Dateien, nicht nur die README. Wenn du ausnahmsweise bisher kein Repository hast, initialisiere einmal mit `git init`, lege zuerst `.gitignore` an und richte danach einen Remote ein. Ein vorhandener Remote wird nicht noch einmal mit `git remote add origin` angelegt.

## Gestufte Hinweise

Versuche zuerst eine eigene Lösung. Öffne bei Bedarf zunächst Hinweis 1 und erst danach Hinweis 2; die vorhandenen Beispiele bzw. Referenzen dienen anschließend zum Vergleichen.

<details>
<summary>Hinweis 1: Denkanstoß</summary>

Welche Befehle benötigt ein frischer Checkout, um deine Änderung zu prüfen?

</details>

<details>
<summary>Hinweis 2: Vorgehensweise</summary>

Die Pipeline führt Restore, Build und Test auf dem richtigen Solution-Pfad aus; ein nicht ausgeführter Test ist kein Nachweis.

</details>

<details>
<summary>Build und Tests mit GitHub Actions</summary>

Die ausführbare Referenz enthält [build-test.yml](../.github/workflows/build-test.yml). Bei deinem eigenen Projekt passe den Solution-Pfad an. Die Schritte sind Restore → Build → Test; die Materialprüfung ist spezifisch für diese Aufgabensammlung.

```yaml
name: Build & Test
on: [push, pull_request]
permissions:
  contents: read
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v5
      - uses: actions/setup-dotnet@v5
        with:
          dotnet-version: '10.0.x'
      - run: dotnet restore Beispiele/Adressbuch/Adressbuch.slnx
      - run: dotnet build Beispiele/Adressbuch/Adressbuch.slnx --configuration Release --no-restore
      - run: dotnet test Beispiele/Adressbuch/Adressbuch.slnx --configuration Release --no-build
```

</details>

## Selbst prüfen

Ein fehlschlagender Test macht den Build rot. Ein erfolgreicher Commit wird grün. README-Startbefehle funktionieren aus einem frischen Checkout. Die `.gitignore` hält generierte Dateien und `.env` aus dem Diff. Das Issue enthält konkrete Beispiele, der Pull Request erklärt Verhalten und Prüfung.

## Bonus: Qualitäts- und Sicherheitschecks

**Intention:** Ergänze Build und Tests um weitere Analysen. **Lernziel:** Du kannst nach Bonus A06 die gewählten Checks einrichten und ihre Ergebnisse begründet auswerten. Ohne diesen Bonus bleiben die Kernanforderungen an CI vollständig erfüllt.

Die [Bonus-Aufgabe A06](./A06_Qualitaetschecks_Bonus.md) ergänzt .NET-Analyser, Formatprüfung, NuGet Audit, Dependabot, SonarQube Cloud, CodeQL und Secret Scanning. Sie erklärt die kostenlosen Möglichkeiten für öffentliche und private Repositories und enthält kopierbare Konfigurationen.

## Bonus: Zusammenarbeit und Auslieferung

**Intention:** Ergänze Regeln für weitere Mitwirkende und eine spätere automatische Auslieferung.

**Lernziel:** Du kannst CONTRIBUTING und Lizenzentscheidung dokumentieren; automatisches Deployment setzt die erfolgreiche manuelle Bereitstellung aus A05 voraus.

CONTRIBUTING, Lizenzentscheidung für öffentliche Projekte und automatisches Deployment erst nach einer funktionierenden manuellen Bereitstellung.

## Passende Lernquellen

[Leseempfehlung für diesen Lernschritt](../Referenzen/Lernquellen.md#stufe-6-http-tests-und-webseite). Wähle den dort genannten Abschnitt zur aktuellen Aufgabe und probiere ihn in deinem eigenen Programm aus.
