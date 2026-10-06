# Vorlagen für die Bonus-Aufgabe

Die [Bonus-Aufgabe A06](../../Stufe6/A06_Qualitaetschecks_Bonus.md) erklärt Einrichtung, Kostenbedingungen und Auswertung. Diese Dateien dienen als Kopiervorlagen; hier im Beispielordner werden sie nicht von GitHub ausgeführt.

| Vorlage | Ziel im eigenen Repository | Einrichtung |
| --- | --- | --- |
| [quality-dotnet.yml](./quality-dotnet.yml) | `.github/workflows/quality-dotnet.yml` | Solution-Pfad anpassen, zunächst lokal formatieren, nach dem Merge manuell starten |
| [dependabot.yml](./dependabot.yml) | `.github/dependabot.yml` | Projektverzeichnisse anpassen, Alerts/Security Updates einschalten, in den Standardbranch mergen |
| [sonar-dotnet.yml](./sonar-dotnet.yml) | `.github/workflows/sonar-dotnet.yml` | Sonar-Projekt in der EU-Region, Token-Secret und zwei Variablen einrichten; Standardbranch und Solution-Pfad anpassen |

Der Sonar-Workflow lädt eine Analyse hoch; Coverage-Import und ein den Workflow blockierendes Quality Gate sind weitere Schritte der Aufgabe. CodeQL und Secret Scanning werden in der Aufgabe über die GitHub-Einstellungen eingerichtet. Für ein privates Repository prüfst du zuerst Tarif und Actions-Kontingent.
