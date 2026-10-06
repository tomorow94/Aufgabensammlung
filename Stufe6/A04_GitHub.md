# 🔴 Aufgabe A04: Bestehendes GitHub-Projekt und CI weiterentwickeln

## Ziel und Voraussetzungen

Dein Menüprojekt wird seit Stufe 3 mit Git verwaltet. Erweitere **dieses Repository**, statt es erneut zu initialisieren oder eine zweite Versionsgeschichte anzulegen. Jetzt ergänzt du Dokumentation, Branches, Reviews und automatisierte Prüfungen.

## Anforderungen

1. Prüfe mit `git status`, `git remote -v` und `git branch`, welches Repository du verwendest.
2. Pflege `.gitignore` für `bin`, `obj`, `.vs`, `TestResults`, `node_modules`, `.env` und lokale Buildordner. Zugangsdaten werden nicht eingecheckt.
3. Beschreibe in der README Modell, Startbefehle, Datenbankvorbereitung, Tests und API-Endpunkte.
4. Plane eine Erweiterung als Issue mit überprüfbaren Akzeptanzkriterien.
5. Erstelle einen Branch, implementiere die Änderung und eröffne einen Pull Request. Prüfe Diff und Tests vor dem Zusammenführen.
6. Führe Build und Tests über GitHub Actions aus. JavaScript ohne npm-Projekt benötigt kein erfundenes `npm test`.

## Typischer Ablauf im bestehenden Repository

```shell
git switch -c feature/contact-search
git status
git add README.md
git commit -m "Document contact search"
git push -u origin feature/contact-search
```

Stage die tatsächlich geänderten Dateien, nicht nur die README. Wenn du ausnahmsweise bisher kein Repository hast, initialisiere einmal mit `git init`, lege zuerst `.gitignore` an und richte danach einen Remote ein. Ein vorhandener Remote wird nicht noch einmal mit `git remote add origin` angelegt.

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

## SonarQube Cloud als optionale Vertiefung

Build und fachliche Tests sind der erste Schritt; Codeanalyse ergänzt sie. Richte in SonarQube Cloud Organisation und Projekt ein. Speichere `SONAR_TOKEN` als GitHub Actions Secret sowie `SONAR_PROJECT_KEY` und `SONAR_ORGANIZATION` als Repository-Variablen. Der Scanner benötigt Installation, **begin → build/test → end**. Eine vollständige Vorlage:

```yaml
name: SonarQube Cloud
on:
  push:
    branches: [main]
permissions:
  contents: read
jobs:
  analyze:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v5
        with:
          fetch-depth: 0
      - uses: actions/setup-dotnet@v5
        with:
          dotnet-version: '10.0.x'
      - name: Install scanner
        run: dotnet tool install --global dotnet-sonarscanner
      - name: Begin analysis
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
          SONAR_PROJECT_KEY: ${{ vars.SONAR_PROJECT_KEY }}
          SONAR_ORGANIZATION: ${{ vars.SONAR_ORGANIZATION }}
        run: >-
          dotnet sonarscanner begin
          /k:"$SONAR_PROJECT_KEY"
          /o:"$SONAR_ORGANIZATION"
          /d:sonar.host.url="https://sonarcloud.io"
          /d:sonar.token="$SONAR_TOKEN"
      - run: dotnet restore Beispiele/Adressbuch/Adressbuch.slnx
      - run: dotnet build Beispiele/Adressbuch/Adressbuch.slnx --configuration Release --no-restore --no-incremental
      - run: dotnet test Beispiele/Adressbuch/Adressbuch.slnx --configuration Release --no-build
      - name: End analysis
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
        run: dotnet sonarscanner end /d:sonar.token="$SONAR_TOKEN"
```

Der aktuelle Scanner kann seine JRE selbst bereitstellen. Prüfe bei der Einrichtung die [Scanner-Anforderungen](https://docs.sonarsource.com/sonarqube-cloud/analyzing-source-code/scanners/sonarscanner-for-dotnet/installing). Die Vorlage setzt eine Organisation in der EU-Region voraus; andere Regionen brauchen die entsprechende Serverkonfiguration. Ergänze einen Status-Badge erst, wenn dein Workflow tatsächlich ausgeführt wurde. Die Vorlage wird nicht ohne deine Sonar-Konfiguration aktiviert.

## Selbst prüfen

Ein fehlschlagender Test macht den Build rot. Ein erfolgreicher Commit wird grün. README-Startbefehle funktionieren aus einem frischen Checkout. Die `.gitignore` hält generierte Dateien und `.env` aus dem Diff. Das Issue enthält konkrete Beispiele, der Pull Request erklärt Verhalten und Prüfung. Die Sonar-Vorlage enthält alle drei Analyseschritte.

Zusatz: CONTRIBUTING, Lizenzentscheidung für öffentliche Projekte und automatisches Deployment erst nach einer funktionierenden manuellen Bereitstellung.
