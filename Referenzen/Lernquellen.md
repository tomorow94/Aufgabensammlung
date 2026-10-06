# Gezielte Lernquellen zur Sammlung

Die Aufgaben verlinken hierher passend zum Lernschritt. Lies zuerst den genannten Abschnitt und wende ihn im eigenen Programm an. Die Quellen ergänzen die Aufgabe; ein kompletter externer Kurs ist keine Voraussetzung. Die Materialien sind frei zugänglich, viele vertiefende Dokumentationen auf Englisch.

## Stufe 1: Eingaben und Ablauf

- [Microsoft Learn: Erste Schritte mit C#, Teil 1](https://learn.microsoft.com/de-de/training/paths/get-started-c-sharp-part-1/) – deutschsprachiger Einstieg in Ausgabe, Variablen und einfache Rechnungen; parallel zu A01–A03 verwenden.
- [C#-Dokumentation](https://learn.microsoft.com/en-us/dotnet/csharp/) – schlage gezielt Bedingungen, Iterationsanweisungen und Zahlenoperatoren nach, sobald A04–A10 diese einführen. Sprachreferenz-Beispiele sind kein Ersatz für die eigene Eingabeprüfung.

## Stufe 2: Methoden und Fehlersuche

- [Methoden in C#](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/methods) – für A01/A02 Parameter, Aufruf und Rückgabewerte; Vererbung und asynchrone Methoden werden später eingeführt.
- [Microsoft: C# debuggen](https://learn.microsoft.com/en-us/visualstudio/get-started/csharp/tutorial-debugger) – Haltepunkte, schrittweises Ausführen, lokale Variablen und Aufrufstapel; begleitend zur [Debugging-Übung](./Debugging.md).
- [Text in Dateien schreiben](https://learn.microsoft.com/en-us/dotnet/standard/io/how-to-write-text-to-a-file) – für A03 zunächst den einfachen Dateizugriff lesen und den Dateipfad im eigenen Programm anzeigen.
- [Stopwatch](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.stopwatch?view=net-10.0) – für A04 die Methoden `Start`, `Stop`, `Reset` und die Eigenschaften `Elapsed`, `IsRunning` nachschlagen.
- [Sammlungen in C#](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/collections) – für A05 zunächst nur indexbasierte Sammlungen und Schlüsselzugriff lesen. Spezialisierte Typen und Iteratoren sind spätere Vertiefungen.

## Stufe 3: Struktur und Versionsgeschichte

- [C#-Dokumentation](https://learn.microsoft.com/en-us/dotnet/csharp/) – suche nach Klassen, Eigenschaften, Konstruktoren und Schnittstellen. Ordne jeden Begriff einer Stelle im eigenen Adressbuch zu.
- [Pro Git auf Deutsch](https://git-scm.com/book/de/v2) – zuerst „Änderungen nachverfolgen und im Repository speichern“, dann „Einfaches Branching und Merging“. Für A05 genügen kleine Commits und ein nachvollziehbarer Diff.

## Stufe 4: Zustand und Geschäftsregeln

- [C#-Dokumentation](https://learn.microsoft.com/en-us/dotnet/csharp/) – Arrays für das Spielfeld, Zeichenketten für Hangman und Zugriffsmodifikatoren für das Bankkonto. Lies jeweils nur den Teil, den du gerade implementierst.
- [Debugger-Überblick](https://learn.microsoft.com/en-us/visualstudio/debugger/debugger-feature-tour) – beobachte Zustandsänderungen in Spielen. Erweiterte Leistungs- und Speicheranalyse gehört nicht zum Pflichtpfad.

## Stufe 5: Daten und Abfragen

- [Transact-SQL-Referenz](https://learn.microsoft.com/en-us/sql/t-sql/language-reference) – für A02 zunächst `CREATE TABLE`, `SELECT`, `INSERT`, `UPDATE` und `DELETE` nachschlagen; anschließend Parameter im C#-Code prüfen.
- [EF-Core-Dokumentation](https://learn.microsoft.com/en-us/ef/core/) – Modellierung, Abfragen und Migrationen für A03. Vergleiche eine LINQ-Abfrage mit ihrer SQL-Wirkung und bleibe beim vorhandenen Kontaktmodell.

## Stufe 6: HTTP, Tests und Webseite

- [ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/?view=aspnetcore-10.0) – für A01 Controller, Routing, Dependency Injection und Modellvalidierung; verwende die Dokumentationsansicht für .NET 10.
- [ASP.NET-Core-Integrationstests](https://learn.microsoft.com/en-us/aspnet/core/test/integration-tests?view=aspnetcore-10.0) – für A02 zunächst Testhost, `WebApplicationFactory` und dessen Anpassung lesen.
- [MDN: Webentwicklung lernen](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core) – für A03 semantisches HTML, Formulare, CSS und JavaScript-Ereignisse. Framework-Kapitel sind für die einfache Webseite keine Voraussetzung.
- [GitHub Actions verstehen](https://docs.github.com/en/actions/get-started/understand-github-actions) – für A04 Trigger, Jobs, Runner und Steps am eigenen Build-Test-Workflow wiedererkennen.
- [Docker Compose Quickstart](https://docs.docker.com/compose/gettingstarted/) – für A05 Dienste, Build und Startbefehle verstehen. Das Tutorial nutzt eine andere Anwendung; du überträgst die Begriffe auf App, Migration und Datenbank im Adressbuch.

## Bonus: Zugänglichkeit und Datenbanktests

- [W3C WAI: Formulare](https://www.w3.org/WAI/tutorials/forms/) – für Bonus A07 Beschriftungen, Anweisungen und Rückmeldungen. Übertrage ein konkretes Beispiel auf das eigene Kontaktformular und teste die Bedienung.
- [EF Core: Teststrategie wählen](https://learn.microsoft.com/en-us/ef/core/testing/choosing-a-testing-strategy) – für Bonus A08 die Unterschiede zwischen SQLite und dem verwendeten Datenbanksystem nachvollziehen.
- [EF Core: Mit dem verwendeten Datenbanksystem testen](https://learn.microsoft.com/en-us/ef/core/testing/testing-with-the-database) – Testdaten vorbereiten, Tests isolieren und Aufräumen planen. Die Beispielanwendung ist eine andere; du übernimmst die Vorgehensweise auf dein Adressbuch.

Die Werkzeugquellen für Bonus A06 stehen direkt in der [Qualitätscheck-Aufgabe](../Stufe6/A06_Qualitaetschecks_Bonus.md), jeweils neben Einrichtung und Tarifbedingungen.
