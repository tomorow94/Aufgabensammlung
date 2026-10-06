# 🔴 Bonus A06: Kostenlose Qualitäts- und Sicherheitschecks auf GitHub

## Einordnung und Lernziele

**Status:** Bonus (optional; keine Voraussetzung für spätere Pflichtaufgaben).

**Voraussetzungen:** [Unit- und Integrationstests für das Adressbuch](A02_Testing.md), [Bestehendes GitHub-Projekt und CI weiterentwickeln](A04_GitHub.md)

**Intention:** Die Aussage und Grenzen zusätzlicher automatischer Analysen bewerten.

**Lernziele:**

- Du kannst passende kostenlose Checks für dein Repository auswählen und konfigurieren.
- Du kannst einen Befund prüfen und Scan-Erfolg von einem Quality Gate unterscheiden.

**Weiter im Pflichtpfad:** [Adressbuch mit Datenbank bereitstellen](A05_Deployment.md)

## Ziel und Voraussetzungen

Du hast die Tests und GitHub Actions aus [A04](./A04_GitHub.md) eingerichtet. Ergänze dein bestehendes Adressbuch um automatische Prüfungen und lerne, ihre Ergebnisse zu bewerten. Diese Aufgabe ist optional; beginne mit einem kleinen, verständlichen Satz von Checks.

Ein Build prüft, ob sich dein Programm übersetzen lässt. Tests prüfen ausgewählte Verhaltensweisen. Statische Analyse untersucht Code ohne Ausführung; Paketprüfungen suchen bekannte Schwachstellen in Abhängigkeiten. Kein einzelner Check deckt alles ab.

## Welche Werkzeuge passen zu deinem Repository?

Kostenstand: **6. Oktober 2026**. Prüfe die verlinkten Bedingungen bei der Einrichtung erneut. „Kostenloses Werkzeug“ bedeutet nicht automatisch unbegrenzte kostenlose CI-Laufzeit.

| Werkzeug | Prüft | Öffentliches Repository | Privates Repository |
| --- | --- | --- | --- |
| .NET-Analyser und `dotnet format` | Compilerwarnungen, Code-Regeln und Formatierung | Im SDK kostenlos | Im SDK kostenlos |
| NuGet Audit | Bekannte Schwachstellen direkter und transitiver Pakete | Kostenlos | Kostenlos |
| Dependabot | Verwundbare Pakete und Update-Pull-Requests für NuGet/GitHub Actions | Basisfunktionen kostenlos | Basisfunktionen kostenlos |
| SonarQube Cloud (früher SonarCloud) | Fehlerverdacht, Wartbarkeit, Duplikate und Sicherheitsbefunde | Kostenlose Analyse; zusätzlicher OSS-Tarif für passende Open-Source-Projekte | Kostenloser Tarif bis 50.000 Zeilen privaten Codes pro Organisation; laut Tarifdokumentation maximal fünf Mitglieder |
| GitHub CodeQL | Sicherheitsprobleme durch statische Analyse, unter anderem für C# und JavaScript | Kostenlos | GitHub Code Security erforderlich; keine allgemein kostenlose Option |
| GitHub Secret Scanning / Push Protection | Erkannte Zugangsdaten in Commits bzw. beim Push | Kostenlose Funktionen verfügbar | Zusätzlicher Tarif erforderlich; nutze für einen kostenlosen Einstieg etwa die Gitleaks-CLI |
| Gitleaks-CLI | Verdächtige Zugangsdaten in Dateien und Git-Historie | Kostenlos, MIT-Lizenz | Kostenlos, MIT-Lizenz |

Die Bedingungen stehen bei [GitHub Security](https://docs.github.com/en/code-security/getting-started/github-security-features), [Code Scanning](https://docs.github.com/en/code-security/concepts/code-scanning/code-scanning), [Secret Scanning](https://docs.github.com/en/code-security/how-tos/secure-your-secrets/detect-secret-leaks/enable-secret-scanning), [Sonar-Tarifen](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans) und [Gitleaks](https://github.com/gitleaks/gitleaks).

GitHub Actions auf **Standard-Runnern** ist für öffentliche Repositories kostenlos. Private Repositories haben ein tarifabhängiges Kontingent für Minuten und Speicher. Prüfe dort das Budget und eine Ausgabengrenze; größere Runner sind keine kostenlose Alternative. Siehe [Actions-Abrechnung](https://docs.github.com/en/billing/concepts/product-billing/github-actions).

## Anforderungen

1. Dokumentiere, ob dein Repository öffentlich oder privat ist und welche kostenlosen Funktionen du nutzen kannst.
2. Ergänze zuerst .NET-Formatprüfung, Compilerwarnungen und NuGet Audit. Richte anschließend Dependabot ein.
3. Wähle eine zusätzliche Analyse: SonarQube Cloud oder, bei einem öffentlichen Repository, CodeQL. Untersuche mindestens einen tatsächlichen Befund; wenn keine vorliegen, erkläre anhand einer dokumentierten Regel, was das Werkzeug erkennen kann.
4. Prüfe Zugangsdaten mit GitHub Secret Scanning oder lokal mit Gitleaks. Verwende für Experimente ausschließlich künstliche Testdaten.
5. Behebe einen nachvollziehbaren Befund in einem eigenen Pull Request. Falls kein echter Befund vorliegt, verbessere stattdessen die Check-Konfiguration oder ihre Dokumentation in einem Pull Request und erkläre einen Befund anhand einer dokumentierten Regel. Erkläre Auswirkung, Änderung und Prüfung. Begründe eine eventuelle Fehlalarm-Einstufung konkret.
6. Beschreibe die aktivierten Checks und ihre Grenzen in deiner README. Ergänze Status-Badges erst nach erfolgreichen echten Läufen.

## 1. .NET-Prüfungen ohne zusätzlichen Dienst

Alle Befehle werden vom Repository-Wurzelordner mit .NET 10 ausgeführt. Passe den Solution-Pfad für dein eigenes Projekt an.

```shell
dotnet restore Beispiele/Adressbuch/Adressbuch.slnx
dotnet format Beispiele/Adressbuch/Adressbuch.slnx --verify-no-changes --no-restore
dotnet build Beispiele/Adressbuch/Adressbuch.slnx --configuration Release --no-restore -warnaserror
dotnet test Beispiele/Adressbuch/Adressbuch.slnx --configuration Release --no-build
dotnet package list --project Beispiele/Adressbuch/Adressbuch.slnx --vulnerable --include-transitive --no-restore
```

`dotnet format --verify-no-changes` verändert keine Dateien und liefert bei nötigen Korrekturen einen Fehlerstatus. Führe zunächst lokal `dotnet format Beispiele/Adressbuch/Adressbuch.slnx` aus, prüfe den Diff und vereinbare bei Bedarf Regeln in einer `.editorconfig`. Ein neuer Formatcheck kann im bestehenden Code anfangs rot werden. `-warnaserror` macht Compiler- und ausgeführte Analyserwarnungen zu Buildfehlern; zusätzliche Regeln kannst du über `.editorconfig` festlegen. [Format-Befehl](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-format).

Die Paketliste ist ein **Bericht**, kein zuverlässiges CI-Gate allein durch ihren Exitcode. Die [Workflow-Vorlage](../Beispiele/Qualitaetschecks/quality-dotnet.yml) aktiviert stattdessen NuGet Audit beim Restore für alle Abhängigkeiten und behandelt mit `TreatWarningsAsErrors` die Restore-Warnungen als Fehler, einschließlich der Sicherheitswarnungen `NU1901` bis `NU1904`. Eine nicht erreichbare Auditquelle ist keine Entwarnung. [NuGet Audit](https://learn.microsoft.com/en-us/nuget/concepts/auditing-packages), [Paketliste](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-package-list).

Kopiere die Vorlage nach `.github/workflows/quality-dotnet.yml`. Führe sie nach dem Merge in den Standardbranch zunächst manuell über **Actions → .NET Quality → Run workflow** aus. Integriere die zusätzlichen Schritte nach einem erfolgreichen Lauf in deinen vorhandenen Build-Workflow; vermeide auf Dauer doppelte Builds. Passe `main` an deinen Standardbranch an, wenn du später einen Push-Trigger ergänzt.

## 2. Dependabot für Pakete und Actions

Aktiviere in den Repository-Einstellungen die Basisfunktionen **Dependabot alerts** und **Dependabot security updates** sowie den Dependency Graph. Je nach GitHub-Oberfläche findest du sie unter **Settings → Security and quality → Advanced Security**. Alerts melden bekannte Schwachstellen; Security Updates schlagen Reparaturen vor; Version Updates prüfen zusätzlich reguläre neue Versionen. [Einrichtung](https://docs.github.com/en/code-security/tutorials/secure-your-dependencies/dependabot-quickstart).

Kopiere [dependabot.yml](../Beispiele/Qualitaetschecks/dependabot.yml) nach `.github/dependabot.yml` und merge sie in deinen Standardbranch. Die Vorlage prüft wöchentlich alle vier .NET-Projekte und die verwendeten GitHub Actions. Sie fasst NuGet-Updates zusammen, damit zusammengehörende EF-/ASP.NET-Paketstände gemeinsam aktualisiert werden können. Passe die Verzeichnisse an dein eigenes Repository an. Für das Frontend ohne npm-Pakete brauchst du keinen npm-Eintrag.

Prüfe auch Updates des lokal installierten EF-Tools. Dependabot-Pull-Requests werden wie eigene Änderungen getestet und gelesen; ein grüner Build allein erklärt keine inkompatible Änderung einer neuen Hauptversion. [Konfigurationsoptionen](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuration-options-for-the-dependabot.yml-file).

## 3. SonarQube Cloud einrichten

1. Verbinde GitHub mit SonarQube Cloud und importiere dein Repository. Wähle einen passenden kostenlosen Tarif und kontrolliere dessen Grenzen. Im dokumentierten Free-Tarif sind nur der Hauptbranch und Pull Requests auf diesen Branch analysierbar; der OSS-Tarif bietet weitergehende Branch-Analyse.
2. Wähle für C# die Analyse über CI mit **SonarScanner for .NET**; verwende keine parallel laufende automatische Analyse für dasselbe Projekt.
3. Erstelle einen Sonar-Token. Speichere ihn unter **Settings → Secrets and variables → Actions** als Repository-Secret `SONAR_TOKEN`. Lege `SONAR_PROJECT_KEY` und `SONAR_ORGANIZATION` als Repository-Variablen an.
4. Kopiere [sonar-dotnet.yml](../Beispiele/Qualitaetschecks/sonar-dotnet.yml) nach `.github/workflows/sonar-dotnet.yml`. Ersetze `main`, falls dein Standardbranch anders heißt; setze denselben Hauptbranch im Sonar-Projekt.
5. Merge die Konfiguration in diesen Branch und kontrolliere anschließend Workflow und Sonar-Dashboard. Die Vorlage analysiert ausschließlich Pushes auf den Hauptbranch und setzt eine Sonar-Organisation in der EU-Region voraus.

Der Ablauf ist **Scanner installieren → begin → restore/build/test → end**. Der aktuelle Scanner kann seine Java-Laufzeit selbst bereitstellen. Prüfe bei der Einrichtung die [Scanner-Anforderungen](https://docs.sonarsource.com/sonarqube-cloud/analyzing-source-code/scanners/sonarscanner-for-dotnet/installing). Für reproduzierbare Läufe kannst du nach der Einrichtung eine geprüfte Scanner-Version mit `--version` festlegen.

Ein erfolgreicher Upload bedeutet noch kein bestandenes **Quality Gate**. Das Gate bewertet Kriterien wie neue Fehler oder Testabdeckung. Prüfe es im Dashboard; mit `/d:sonar.qualitygate.wait=true` im `begin`-Schritt lässt du den Workflow später auch bei einem fehlgeschlagenen Gate scheitern. [Analyseparameter für CI](https://docs.sonarsource.com/sonarqube-cloud/analyzing-source-code/analysis-parameters/parameters-not-settable-in-ui).

Die Vorlage führt Tests aus, erzeugt aber **keinen Coverage-Bericht**. Coverage musst du mit einem passenden Collector erzeugen und importieren, etwa als OpenCover mit `sonar.cs.opencover.reportsPaths`. Plane das vor einem Gate mit Coverage-Schwelle ein. Eine hohe Abdeckung zeigt ausgeführte Codezeilen, keine vollständige fachliche Prüfung. [C#-Testabdeckung](https://docs.sonarsource.com/sonarqube-cloud/enriching/test-coverage/dotnet-test-coverage).

Wenn du später PR-Analyse ergänzt: Tokens stehen Pull Requests aus fremden Forks normalerweise nicht zur Verfügung. Führe fremden PR-Code nicht mit Secrets über `pull_request_target` aus. Die Hauptbranch-Vorlage benötigt diesen Sonderfall nicht.

## 4. CodeQL als zusätzliche Option

Öffne bei einem öffentlichen Repository **Settings → Security and quality → Advanced Security → Code Security → CodeQL analysis** und wähle **Default setup**, sofern verfügbar. Kontrolliere, dass C# und JavaScript/TypeScript erkannt werden. Für private Repositories prüfe zuerst die benötigte kostenpflichtige Lizenz. [Default Setup](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning).

CodeQL-Befunde findest du unter **Security and quality → Code scanning**. Prüfe auch den Analyse-Status und die erkannten Sprachen: Ein Lauf ohne untersuchten C#-Code ist kein aussagekräftiger C#-Check. Wenn das Standard-Setup dein Projekt nicht korrekt analysiert, verwende Advanced Setup mit dem .NET-10-SDK und dem Solution-Pfad aus A04. [Analyse mit CodeQL](https://docs.github.com/en/code-security/concepts/code-scanning/codeql/about-code-scanning-with-codeql).

## 5. Zugangsdaten prüfen

Prüfe bei öffentlichen Repositories, ob Secret Scanning und Push Protection aktiv sind. Scans erkennen bestimmte Muster, nicht jede Form eines Passworts. Lege Tokens auch für Übungen in Secrets oder lokale, ignorierte Konfigurationen.

Als kostenlose lokale Option für öffentliche und private Repositories kannst du die Gitleaks-CLI aus den [offiziellen Releases](https://github.com/gitleaks/gitleaks/releases) installieren. Prüfe Versionsstand und veröffentlichte Prüfsummen. Danach im Repository:

```shell
gitleaks git --redact --exit-code 1 .
```

Dieser Befehl untersucht die Git-Historie; `gitleaks dir --redact .` untersucht zusätzlich den aktuellen Dateistand, auch noch nicht committete Dateien. Nutze für einen CI-Historienscan einen vollständigen Checkout mit `fetch-depth: 0`. Die kostenlose CLI und die Bedingungen einer separaten GitHub Action sind unterschiedliche Dinge; prüfe deren Lizenz vor der Auswahl.

Bei einem echten Fund sperrst bzw. rotierst du die Zugangsdaten beim Anbieter. Eine Datei zu löschen macht ein veröffentlichtes Geheimnis nicht wieder geheim. Dokumentiere im Issue oder PR nur den Fundort und die Behebung, nicht den geheimen Wert.

## Gestufte Hinweise

Versuche zuerst eine eigene Lösung. Öffne bei Bedarf zunächst Hinweis 1 und erst danach Hinweis 2; die vorhandenen Beispiele bzw. Referenzen dienen anschließend zum Vergleichen.

<details>
<summary>Hinweis 1: Denkanstoß</summary>

Welchen Fehler soll der neue Check erkennen, den dein Build allein nicht erkennt?

</details>

<details>
<summary>Hinweis 2: Vorgehensweise</summary>

Beginne mit einem lokalen .NET-Check; aktiviere einen Dienst erst mit passendem Tarif, Projektpfad und einer klaren Auswertung.

</details>

## Selbst prüfen

- Eine absichtlich veränderte Einrückung lässt die Formatprüfung scheitern. Nach der Korrektur wird sie grün.
- Ein absichtlich fehlschlagender fachlicher Test macht weiterhin die bestehende Test-CI rot.
- Dependabot erfasst die tatsächlichen `.csproj`-Dateien und GitHub Actions. Sein erster Update-PR wird geprüft; zusammengehörende Paketstände passen danach weiterhin zusammen.
- Sonar bzw. CodeQL analysiert deinen C#-Code. Du kannst einen Befund oder eine Regel erklären und weißt, ob der Workflow nur den Scan oder auch ein Quality Gate prüft.
- Die README nennt gewählte Checks, den passenden kostenlosen Tarif und etwaige CI-Kontingente. Tokens sind nicht Teil des Diffs.
- Du kannst erklären, warum ein grüner Scan fachliche Tests und ein Review weiterhin braucht.

Abgabe: Konfiguration, mindestens ein nachvollziehbarer Verbesserungs-PR (Befundbehebung oder Verbesserung der Checks/Dokumentation) und eine kurze Auswertung der Ergebnisse. Aktiviere zunächst wenige Checks und baue sie aus, wenn du ihre Meldungen sinnvoll bearbeiten kannst.

## Passende Lernquellen

[Leseempfehlung für diesen Lernschritt](../Referenzen/Lernquellen.md#stufe-6-http-tests-und-webseite). Wähle den dort genannten Abschnitt zur aktuellen Aufgabe und probiere ihn in deinem eigenen Programm aus.
