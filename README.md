# 📚 Programmier-Aufgabensammlung

Diese deutschsprachige Sammlung führt von ersten **C#-Konsolenprogrammen** zu einem **Adressbuch mit Datenbank, REST-API und Webseite**. Sie enthält **31 Pflichtaufgaben und 5 eigenständige Bonus-Aufgaben**. Die Stufen erhöhen schrittweise Selbstständigkeit und Komplexität.

Jede Aufgabe nennt **Status, Voraussetzungen, Intention, prüfbare Lernziele und den nächsten Schritt im Pflichtpfad**. Versuche zuerst eine eigene Lösung, öffne bei Bedarf die beiden gestuften Hinweise und vergleiche anschließend mit Beispiel oder Referenz. Am Anfang sind die Beispiele vollständiger; später planst du selbst. Codebeispiele mit Kennzeichnung „Skizze“ brauchen die erwähnten zusätzlichen Klassen oder Methoden.

**Pflicht** vermittelt die aufeinander aufbauenden Grundlagen. **Bonus** vertieft ein Thema oder untersucht einen zusätzlichen Ansatz und ist keine Voraussetzung für eine spätere Pflichtaufgabe. Auch kleine Erweiterungen innerhalb einer Pflichtaufgabe sind ausdrücklich als Bonus mit Intention und Lernziel gekennzeichnet. „Selbst prüfen“ bezieht sich auf die Kernanforderungen; Bonus-Prüfungen sind gesondert benannt.

## Technischer Stand und Einstieg

- **.NET 10 LTS SDK** für alle C#-Projekte: [Download](https://dotnet.microsoft.com/en-us/download/dotnet/10.0).
- **Visual Studio 2026 (18.0+)** mit passenden C#/.NET-Workloads oder Visual Studio Code mit C#-Unterstützung. [Kompatibilität](https://learn.microsoft.com/en-us/dotnet/core/install/windows).
- Git; GitHub Desktop ist optional. Git wird ab Stufe 3 regelmäßig verwendet.
- Ab Stufe 5: SQL Server Express als Datenbank-Engine und SSMS als getrenntes Verwaltungswerkzeug.
- Für HTTP-Tests: Postman oder ein REST-Client. Für das lokale Container-Deployment: Docker mit Linux-Containern.
- Node.js/npm sind für das einfache HTML/CSS/JavaScript-Frontend nicht notwendig.

Prüfe `dotnet --version`. Erstelle Konsolenprojekte mit Framework `net10.0`. Die Einstiegsbeispiele zeigen eine ausdrückliche `Main()`-Methode: Ersetze jeweils den **ganzen Inhalt** von `Program.cs`, damit keine Top-Level-Anweisung aus der Vorlage daneben stehen bleibt. `Console.ReadLine()` kann `null` liefern; die Referenzen erklären nullable reference types.

Terminalbefehle stehen in `shell`-Blöcken, PowerShell-spezifische Befehle in `powershell`-Blöcken. Dezimaltrennzeichen in Benutzereingaben richten sich nach der Rechnerkultur; in einer deutschen Umgebung ist das meist das Komma. C#-Zahlenliterale im Quellcode verwenden einen Punkt.

## Roter Faden

Ab Stufe 3 hat ein Kontakt dieselben Felder: **Id, Name, Age, Gender, PhoneNumber, Email**. Die Entwicklung lautet:

**Konsole → JSON-Datei → SQL Server/ADO.NET → EF Core → REST-API → Webseite**.

Datenbank und Anwendung vergeben IDs; ein API-Client liefert keine ID für neue Kontakte. Spiele und Algorithmen sind eigenständige Übungen; das Abschlussprojekt entwickelt die Kontaktverwaltung weiter.

Der Lernfaden umfasst auch die Arbeitsweise: **Eingaben prüfen → Methoden und Debugging → Objekte und Refactoring → Zustands- und Geschäftsregeln → Datenhaltung → HTTP und Tests → Webseite → CI und Bereitstellung**. Spiele festigen Zustandsänderungen und Kapselung; Sortieren verbindet Sammlungen mit nachvollziehbaren Messungen. Danach setzt du die Arbeit am gleichen Adressbuch fort.

| Stufe | Intention | Du bist bereit für den nächsten Schritt, wenn … |
| --- | --- | --- |
| 1 | Ablauf und Eingaben verstehen | du Bedingungen, Schleifen und ungültige Eingaben erklären kannst |
| 2 | Logik zerlegen und Fehler untersuchen | reine Methoden, Dateioperationen und passende Sammlungen funktionieren; du einen Rechenfehler im Debugger erklären kannst |
| 3 | Daten und Verantwortlichkeiten modellieren | das Adressbuch nach Neustart funktioniert und eine Strukturänderung seine Prüffälle weiterhin erfüllt |
| 4 | gültige Zustandsänderungen schützen | ungültige Aktionen weder Spielzustand noch Kontostand verändern |
| 5 | das Kontaktmodell dauerhaft ablegen | SQL und EF dieselben Daten verwalten und du den gewählten Schemaweg erklären kannst |
| 6 | das fertige Adressbuch verbinden und prüfen | API, Tests, Webseite, CI und der lokale Bereitstellungsweg zusammen funktionieren |

Die [Debugging-Arbeitsweise](./Referenzen/Debugging.md) wird in Stufe 2, A01 praktisch eingeführt und später wiederverwendet. Die [Lernquellen](./Referenzen/Lernquellen.md) nennen je Stufe gezielte Leseabschnitte. Pflichtaufgaben bleiben auch ohne Bonus vollständig lösbar.

## Aufgaben und empfohlene Reihenfolge

Bonus-Aufgaben stehen direkt bei der passenden Stufe. Bearbeite sie erst nach ihren Voraussetzungen und kehre anschließend zum angegebenen Pflichtschritt zurück. Du kannst alle Bonus-Aufgaben auslassen.

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

Eigene Planung, reine Methoden, Debugging, Dateizugriffe, Zeitmessung und faire Vergleiche.

- [Aufgabe A01: Umrechnung von Einheiten](./Stufe2/A01_UmrechnungVonEinheiten.md)
- [Aufgabe A02: Primzahlenprüfung](./Stufe2/A02_Primzahlen.md)
- [Aufgabe A03: Kleiner Text-Editor](./Stufe2/A03_KleinerTextEditor.md)
- [Aufgabe A04: Stoppuhr](./Stufe2/A04_Stoppuhr.md)
- [Aufgabe A05: List, HashSet und Dictionary](./Stufe2/A05_Datenstrukturen.md)

#### Bonus (optional)

| Bonus | Voraussetzungen | Intention und Lernziel |
| --- | --- | --- |
| [Bonus A06: Fibonacci-Pyramide](./Stufe2/A06_FibonacciPyramide.md) | Fibonacci und Sammlungen | Methoden, Listen und verschachtelte Schleifen in einer zusätzlichen Darstellung verbinden |

### 🟠 Objektorientierung und Adressbuch

Klassen, Objekte, Eigenschaften und Schnittstellen. Das Adressbuch beginnt in der Konsole, erhält Dateispeicherung und wird anschließend ohne Verhaltensänderung aufgeräumt.

- [Aufgabe A01: Menüführung mit Klassen & Struktur](./Stufe3/A01_KlassenUndStruktur.md)
- [Aufgabe A02: Person, Eigenschaften, Konstruktor und Enum](./Stufe3/A02_KlassePerson.md)
- [Aufgabe A03: Adressbuch mit Kontakten und Dateispeicherung](./Stufe3/A03_EinfachesAdressbuch.md)
- [Aufgabe A04: Gemeinsame Schnittstelle und Menü](./Stufe3/A04_BesseresMenu.md)
- [Aufgabe A05: Bestehenden Code schrittweise verbessern (Refactoring)](./Stufe3/A05_Refactoring.md)

### 🟡 Anwendungen und Spiele

Tic-Tac-Toe, Hangman und gekapselte Kontologik festigen gültige Zustandsänderungen und Geschäftsregeln.

- [Aufgabe A01: Tic Tac Toe – Einführung in Spielmechaniken, Arrays und Entscheidungslogik](./Stufe4/A01_TicTacToe.md)
- [Aufgabe A02: Hangman](./Stufe4/A02_Hangman.md)
- [Aufgabe A03: Einfaches Bankkonto-System](./Stufe4/A03_Bankkonto.md)

#### Bonus (optional)

| Bonus | Voraussetzungen | Intention und Lernziel |
| --- | --- | --- |
| [Bonus A04: Hintergrundberechnung](./Stufe4/A04_Hintergrundaufgabe.md) | Methoden, Primzahlen und Spielzustände | CPU-Arbeit, Fortschritt und kooperativen Abbruch unterscheiden |

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

#### Bonus (optional)

| Bonus | Voraussetzungen | Intention und Lernziel |
| --- | --- | --- |
| [Bonus A06: Qualitätschecks](./Stufe6/A06_Qualitaetschecks_Bonus.md) | Tests und GitHub Actions | kostenlose Analysen einrichten, Befunde bewerten und ihre Grenzen erklären |
| [Bonus A07: Barrierefreiheit](./Stufe6/A07_Barrierefreiheit_Bonus.md) | funktionierende Webseite mit grundlegender Tastaturbedienung | zusätzliche Bedienweisen, zugeordnete Fehler und dynamische Meldungen prüfen |
| [Bonus A08: SQL-Server-Tests](./Stufe6/A08_SQLServerTests_Bonus.md) | EF, Migrationen, HTTP-Tests und lokale Testinstanz | providerspezifisches Verhalten und Migrationen mit isolierten Datenbanken absichern |

## Prüfen statt nur kopieren

Nutze pro Aufgabe die normalen Fälle, Grenzfälle und ungültigen Eingaben unter „Selbst prüfen“. Setze früh Haltepunkte und beobachte Variablen mit F10. Frühe xUnit-Tests sind in Stufe 2 ein gekennzeichneter Bonus; im Pflichtpfad führt Stufe 6 die Einrichtung und HTTP-Integrationstests ein.

Die [Referenzanwendung](./Beispiele/Adressbuch/README.md) enthält die zusammenhängende Lösung des Abschlussprojekts. Sie ist eine Vergleichsgrundlage für deine eigene Lösung. Die NuGet-Paketstände sind reproduzierbar festgelegt; beim Aktualisieren auf neue Patchstände müssen alle EF-/ASP.NET-Pakete und das EF-Tool zusammen passen und die Tests erneut laufen.

Vom Repository-Wurzelordner:

```shell
dotnet test Beispiele/Adressbuch/Adressbuch.slnx --configuration Release
python tools/validate_material.py --compile
```

Die automatisierten API-Tests benötigen keinen lokalen SQL Server; sie verwenden pro Test eine isolierte relationale SQLite-Datenbank. SQL-Server-Migrationen und das Docker-Deployment werden zusätzlich in der jeweiligen Entwicklungsumgebung geprüft. Mit optionalem Node.js (20+) kannst du zusätzlich `node --test tools/frontend.test.cjs` ausführen; die Tests prüfen Formularerhalt bei Fehlern und HTTP-Statusbehandlung. Die Webseite selbst benötigt weiterhin kein Node.js.

Die Materialprüfung kontrolliert lokale Links einschließlich Abschnittsankern und genauer Pfadschreibweise, Markdown-Codeblöcke, vollständige Konsolenbeispiele und bekannte Grenzfälle. Sie prüft außerdem Lernziele, Hinweise, Aufgabenanzahl und die Reihenfolge des Pflichtpfads in Aufgaben und README; Pflichtaufgaben dürfen keinen Bonus voraussetzen. Bonusabschnitte benötigen Intention und Lernziel. Fragmente werden als solche behandelt. Externe Webseiten und deren Verfügbarkeit werden dabei nicht automatisch geprüft.

## Referenzen

- [C#-Grundlagen](./Referenzen/Grundlagen.md)
- [C# Cheat Sheet](./Referenzen/CheatSheet_CSharp.md)
- [Debugging: Fehler nachvollziehen und beheben](./Referenzen/Debugging.md)
- [Gezielte Lernquellen nach Stufen](./Referenzen/Lernquellen.md)
- [Microsoft C#](https://learn.microsoft.com/en-us/dotnet/csharp/)
- [ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/?view=aspnetcore-10.0)
- [HTML](https://developer.mozilla.org/de/docs/Web/HTML), [CSS](https://developer.mozilla.org/de/docs/Web/CSS), [JavaScript](https://developer.mozilla.org/de/docs/Web/JavaScript)

Die Sammlung vermittelt die Grundlagen eines vollständigen Projekts. Eigene Lösungen, fachliche Tests, dokumentierte Startbefehle und eine nachvollziehbare Versionsgeschichte gehören zum Lernergebnis.
