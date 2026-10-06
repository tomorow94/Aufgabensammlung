# 📚 Programmier-Aufgabensammlung

Diese deutschsprachige Sammlung führt von ersten **C#-Konsolenprogrammen** zu einem **Adressbuch mit Datenbank, REST-API und Webseite**. Sie enthält 32 Aufgaben, davon zwei optionale Vertiefungen. Die Stufen erhöhen schrittweise Selbstständigkeit und Komplexität.

Jede Aufgabe beschreibt Lernziel, Voraussetzungen und prüfbare Ergebnisse. Am Anfang helfen vollständige Beispiele; später planst du selbst und nutzt ausklappbare Lösungen oder die verlinkte Referenzanwendung. Lies zuerst die Aufgabe, versuche eine eigene Lösung und vergleiche sie anschließend. Codebeispiele mit Kennzeichnung „Skizze“ brauchen die erwähnten zusätzlichen Klassen oder Methoden.

## Technischer Stand und Einstieg

- **.NET 10 LTS SDK** für alle C#-Projekte: [Download](https://dotnet.microsoft.com/en-us/download/dotnet/10.0).
- **Visual Studio 2026 (18.0+)** mit passenden C#/.NET-Workloads oder Visual Studio Code mit C#-Unterstützung. Visual Studio 2022 ist für diesen .NET-10-Stand nicht die passende Zielumgebung. [Kompatibilität](https://learn.microsoft.com/en-us/dotnet/core/install/windows).
- Git; GitHub Desktop ist optional. Git wird ab Stufe 3 regelmäßig verwendet.
- Ab Stufe 5: SQL Server Express als Datenbank-Engine und SSMS als getrenntes Verwaltungswerkzeug.
- Für HTTP-Tests: Postman oder ein REST-Client. Für das lokale Container-Deployment: Docker mit Linux-Containern.
- Node.js/npm sind für das einfache HTML/CSS/JavaScript-Frontend nicht notwendig.

Prüfe `dotnet --version`. Erstelle Konsolenprojekte mit Framework `net10.0`. Die Einstiegsbeispiele zeigen eine ausdrückliche `Main()`-Methode: Ersetze jeweils den **ganzen Inhalt** von `Program.cs`, damit keine Top-Level-Anweisung aus der Vorlage daneben stehen bleibt. `Console.ReadLine()` kann `null` liefern; die Referenzen erklären nullable reference types.

Terminalbefehle stehen in `shell`-Blöcken, PowerShell-spezifische Befehle in `powershell`-Blöcken. Dezimaltrennzeichen in Benutzereingaben richten sich nach der Rechnerkultur; in einer deutschen Umgebung ist das meist das Komma. C#-Zahlenliterale im Quellcode verwenden einen Punkt.

## Roter Faden

Ab Stufe 3 hat ein Kontakt dieselben Felder: **Id, Name, Age, Gender, PhoneNumber, Email**. Die Entwicklung lautet:

**Konsole → JSON-Datei → SQL Server/ADO.NET → EF Core → REST-API → Webseite**.

Datenbank und Anwendung vergeben IDs; ein API-Client liefert keine ID für neue Kontakte. Spiele und Algorithmen bleiben eigenständige Übungen. Die API muss deshalb nicht jede frühere Konsolenfunktion als HTTP-Endpunkt nachbilden.

## Aufgaben und empfohlene Reihenfolge

### 🟢 Grundlagen

Erste Programme, Eingaben, Bedingungen und Schleifen. Der Zahlenvergleich kommt vor den komplexeren Programmen.

- [Aufgabe A01: Hallo Welt](./Stufe1/A01_HalloWelt.md)
- [Aufgabe A02: Texteingabe und -ausgabe](./Stufe1/A02_TexteingabeUndAusgabe.md)
- [Aufgabe A03: Addieren](./Stufe1/A03_Addieren.md)
- [Aufgabe A04: Größere Zahl finden](./Stufe1/A04_GroessereZahlFinden.md)
- [Aufgabe A05: Subtraktion und sichere Zahleneingabe](./Stufe1/A05_Subtraktion.md)
- [Aufgabe A06: Multiplikation und Wiederholung](./Stufe1/A06_Multiplikation.md)
- [Aufgabe A07: Division](./Stufe1/A07_Division.md)
- [Aufgabe A08: Taschenrechner mit Menü](./Stufe1/A08_Taschenrechner.md)
- [Aufgabe A09: Zahlenraten](./Stufe1/A09_Zahlenraten.md)
- [Aufgabe A10: Fibonacci als Zahlenfolge](./Stufe1/A10_Fibonacci.md)

### 🔵 Methoden und Datenstrukturen

Eigene Planung, Dateizugriffe, Zeitmessung und faire Vergleiche. Die Fibonacci-Pyramide ist eine optionale Vertiefung.

- [Aufgabe A01: Umrechnung von Einheiten](./Stufe2/A01_UmrechnungVonEinheiten.md)
- [Aufgabe A02: Primzahlenprüfung](./Stufe2/A02_Primzahlen.md)
- [Aufgabe A03: Kleiner Text-Editor](./Stufe2/A03_KleinerTextEditor.md)
- [Aufgabe A04: Stoppuhr](./Stufe2/A04_Stoppuhr.md)
- [Aufgabe A05: List, HashSet und Dictionary](./Stufe2/A05_Datenstrukturen.md)
- [Aufgabe A06: Fibonacci-Pyramide (optionale Vertiefung)](./Stufe2/A06_FibonacciPyramide.md)

### 🟠 Objektorientierung und Adressbuch

Klassen, Objekte, Eigenschaften und Schnittstellen. Das Adressbuch beginnt in der Konsole und erhält Dateispeicherung.

- [Aufgabe A01: Menüführung mit Klassen & Struktur](./Stufe3/A01_KlassenUndStruktur.md)
- [Aufgabe A02: Person, Eigenschaften, Konstruktor und Enum](./Stufe3/A02_KlassePerson.md)
- [Aufgabe A03: Adressbuch mit Kontakten und Dateispeicherung](./Stufe3/A03_EinfachesAdressbuch.md)
- [Aufgabe A04: Gemeinsame Schnittstelle und Menü](./Stufe3/A04_BesseresMenu.md)

### 🟡 Anwendungen und Spiele

Tic-Tac-Toe, Hangman und gekapselte Kontologik. Hintergrundberechnung mit Fortschritt ist eine optionale Aufgabe zur Nebenläufigkeit.

- [Aufgabe A01: Tic Tac Toe – Einführung in Spielmechaniken, Arrays und Entscheidungslogik](./Stufe4/A01_TicTacToe.md)
- [Aufgabe A02: Hangman](./Stufe4/A02_Hangman.md)
- [Aufgabe A03: Einfaches Bankkonto-System](./Stufe4/A03_Bankkonto.md)
- [Aufgabe A04: Hintergrundberechnung mit Fortschritt (optionale Vertiefung)](./Stufe4/A04_Hintergrundaufgabe.md)

### 🟣 Algorithmen und Datenbanken

Sortieren prüfen und vergleichen. Das gleiche Adressbuch wird zuerst mit SQL/ADO.NET, dann mit EF Core gespeichert.

- [Aufgabe A01: Sortieralgorithmen fair vergleichen](./Stufe5/A01_Sortieralgorithmen.md)
- [Aufgabe A02: Adressbuch mit SQL Server und ADO.NET](./Stufe5/A02_Datenbank.md)
- [Aufgabe A03: Dasselbe Adressbuch mit EF Core und LINQ](./Stufe5/A03_ORMundLINQ.md)

### 🔴 API und Abschlussprojekt

Dasselbe Modell und dieselbe Datenhaltung über HTTP, Tests, Webseite, CI und Deployment weiterverwenden.

- [Aufgabe A01: Adressbuch als REST-API mit ASP.NET Core](./Stufe6/A01_REST_API.md)
- [Aufgabe A02: Unit- und Integrationstests für das Adressbuch](./Stufe6/A02_Testing.md)
- [Aufgabe A03: Webseite für dasselbe Adressbuch](./Stufe6/A03_Webentwicklung.md)
- [Aufgabe A04: Bestehendes GitHub-Projekt und CI weiterentwickeln](./Stufe6/A04_GitHub.md)
- [Aufgabe A05: Adressbuch mit Datenbank bereitstellen](./Stufe6/A05_Deployment.md)

## Prüfen statt nur kopieren

Nutze pro Aufgabe die normalen Fälle, Grenzfälle und ungültigen Eingaben unter „Selbst prüfen“. Setze früh Haltepunkte und beobachte Variablen mit F10. Methoden mit reiner Berechnungslogik können schon in Stufe 2 durch kleine automatisierte Tests abgesichert werden; Stufe 6 behandelt xUnit und HTTP-Integrationstests ausführlicher.

Die [Referenzanwendung](./Beispiele/Adressbuch/README.md) enthält die zusammenhängende Lösung des Abschlussprojekts. Sie ist eine Vergleichsgrundlage für deine eigene Lösung. Die NuGet-Paketstände sind reproduzierbar festgelegt; beim Aktualisieren auf neue Patchstände müssen alle EF-/ASP.NET-Pakete und das EF-Tool zusammen passen und die Tests erneut laufen.

Vom Repository-Wurzelordner:

```shell
dotnet test Beispiele/Adressbuch/Adressbuch.slnx --configuration Release
python tools/validate_material.py --compile
```

Die automatisierten API-Tests benötigen keinen lokalen SQL Server; sie verwenden pro Test eine isolierte relationale SQLite-Datenbank. SQL-Server-Migrationen und das Docker-Deployment werden zusätzlich in der jeweiligen Entwicklungsumgebung geprüft. Mit optionalem Node.js (20+) kannst du zusätzlich `node --test tools/frontend.test.cjs` ausführen; die Tests prüfen Formularerhalt bei Fehlern und HTTP-Statusbehandlung. Die Webseite selbst benötigt weiterhin kein Node.js.

Die Materialprüfung kontrolliert lokale Links, Markdown-Codeblöcke, vollständige Konsolenbeispiele und bekannte Grenzfälle. Fragmente werden als solche behandelt.

## Referenzen

- [C#-Grundlagen](./Referenzen/Grundlagen.md)
- [C# Cheat Sheet](./Referenzen/CheatSheet_CSharp.md)
- [Microsoft C#](https://learn.microsoft.com/en-us/dotnet/csharp/)
- [ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/?view=aspnetcore-10.0)
- [HTML](https://developer.mozilla.org/de/docs/Web/HTML), [CSS](https://developer.mozilla.org/de/docs/Web/CSS), [JavaScript](https://developer.mozilla.org/de/docs/Web/JavaScript)

Die Sammlung vermittelt die Grundlagen eines vollständigen Projekts. Eigene Lösungen, fachliche Tests, dokumentierte Startbefehle und eine nachvollziehbare Versionsgeschichte gehören zum Lernergebnis.
