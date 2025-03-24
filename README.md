# 📚 Programmier-Aufgabensammlung

Diese Aufgabensammlung bietet einen strukturierten Einstieg in die **Programmierung mit C#, objektorientierte Entwicklung, Datenbanken, Webentwicklung und DevOps**.  
Die Aufgaben sind in **verschiedene Stufen** unterteilt und decken Themen von **Grundlagen bis hin zu einem vollständigen Webprojekt mit API** ab.

Jede Aufgabe ist als **Markdown-Datei** abgelegt und enthält:
- Eine **detaillierte Aufgabenstellung**.
- Theoretische **Einführungen in Konzepte**.
- Eine **optionale Lösung** in einer ausklappbaren Sektion.

Eine Sammlung nützlicher Referenzen findet sich am Ende der Datei.

---

## 🛠 Technische Voraussetzungen

### **Für C#-Aufgaben (Stufe 1-5)**
- **.NET SDK** installieren: [Download](https://dotnet.microsoft.com/en-us/download)
- **Visual Studio 2022 Community Edition**: [Download](https://visualstudio.microsoft.com/de/vs/community/)
- **GitHub Desktop** (optional | für visuelles Git-Management): [Download](https://desktop.github.com/)

### **Für Datenbanken (Stufe 5)**
- **SQL Server Management Studio (SSMS)**: [Download](https://aka.ms/ssmsfullsetup)
  
### **Für Web-Entwicklung (Stufe 6)**
- **Visual Studio Code**: [Download](https://code.visualstudio.com/)
- **Node.js** (für npm, falls benötigt): [Download](https://nodejs.org/)
- **Postman** zum Testen der API: [Download](https://www.postman.com/)

---

## 📖 Aufbau & Ziel der Stufen

Die Aufgabensammlung ist in **6 Stufen** gegliedert, die jeweils unterschiedliche Lernziele verfolgen und sich in **Komplexität und Selbstständigkeit** steigern:

### 🟢 **Stufe 1: Grundlagen der Programmierung**
- Fokus: **Verstehen durch Ausprobieren**
- Jede Aufgabe behandelt ein **einzelnes Konzept** wie Ein-/Ausgabe, Variablen, Schleifen oder einfache Logik.
- Ziel: Mit einem „Copy → F5 → Es läuft!“-Erlebnis **erste Erfolgsmomente schaffen**.
- Charakter: Fast wie ein **interaktives Info-Kapitel**, ideal für Einsteiger ohne Vorwissen.

### 🔵 **Stufe 2: Strukturierung & Methoden**
- Ziel: Das in Stufe 1 Gelernte wird **angewendet**, **wiederverwendet** und in **Methoden strukturiert**.
- Themen wie Datei-IO, Datenstrukturen oder Performance-Vergleiche werden erstmals angeschnitten.
- Der Schwierigkeitsgrad steigt, aber die Aufgaben bleiben mit dem Wissen aus Stufe 1 **vollständig lösbar**.

### 🟠 **Stufe 3: Objektorientierte Programmierung (OOP)**
- Einführung von **Klassen, Objekten und Enums**.
- Alle vorherigen Programme werden in ein **geordnetes Menüprojekt** überführt.
- Hier zeigt sich der praktische Nutzen von **Ordnerstruktur, Code-Aufteilung und Wiederverwendbarkeit**.
- Diese Stufe markiert den **Übergang zu echten Softwareprojekten**.

### 🟡 **Stufe 4: Komplexe Anwendungen & Spielmechanik**
- Spielerische Aufgaben mit echten Herausforderungen.
- Einsatz von **Entscheidungslogik, Arrays und sogar Threads**.
- Projekte wie **Tic Tac Toe** oder ein **Bankkonto-System** vertiefen Verständnis für Zustände, Abläufe und Parallelität.

### 🟣 **Stufe 5: Datenbankanbindung & moderne Entwicklung**
- Erste Berührung mit **SQL, SSMS und ORM** (inkl. LINQ).
- Aufgaben zeigen, wie man **strukturiert mit echten Daten arbeitet**.
- Ziel ist es, Programm und Datenhaltung zu verbinden – wie es in der Praxis üblich ist.

### 🔴 **Stufe 6: API, Webentwicklung & Abschlussprojekt**
- Die vorher entwickelten Funktionen werden über eine **REST-API bereitgestellt**.
- Eine eigenständige **Webseite greift per JavaScript auf die API zu**.
- Hier steht die **Selbstständigkeit im Vordergrund**:
  - Weniger Erklärungen, mehr Eigenrecherche.
  - Fokus auf Zusammenspiel aller bisherigen Kenntnisse.
  - Inklusive **Testing, GitHub-Verwaltung, CI/CD und Deployment**.

> ✅ **Ziel:** Nach Abschluss aller Stufen kann ein vollständiges Softwareprojekt **von Grund auf umgesetzt, getestet, dokumentiert und bereitgestellt** werden – inklusive Versionskontrolle und Webanbindung.

---

## 📌 Aufgaben

### **🟢 Stufe 1: Grundlagen der Programmierung (C# Konsolenanwendungen)**
1. [A01_HalloWelt.md](./Stufe1/A01_HalloWelt.md) – Erstes Programm, einfache Konsolenausgabe.
2. [A02_Texteingabe.md](./Stufe1/A02_TexteingabeUndAusgabe.md) – Benutzer gibt seinen Namen ein, das Programm begrüßt ihn.
3. [A03_Addition.md](./Stufe1/A03_Addieren.md) – Zwei Zahlen addieren.
4. [A04_Subtraktion.md](./Stufe1/A04_Subtraktion.md) – Zwei Zahlen subtrahieren.
5. [A05_Multiplikation.md](./Stufe1/A05_Multiplikation.md) – Zwei Zahlen multiplizieren.
6. [A06_Division.md](./Stufe1/A06_Division.md) – Zwei Zahlen dividieren (inkl. Fehlerbehandlung für Division durch 0).
7. [A07_Taschenrechner.md](./Stufe1/A07_Taschenrechner.md) – Einfache Rechenoperationen per Benutzereingabe.
8. [A08_Zahlenraten.md](./Stufe1/A08_Zahlenraten.md) – Zufallszahl zwischen 1 und 100 erraten.
9. [A09_ZahlenpyramideUndFibonacci.md](./Stufe1/A09_ZahlenpyramideUndFibonacci.md) – Schleifen & Listen.
10. [A10_GroessereZahlFinden.md](./Stufe1/A10_GroessereZahlFinden.md) – Größere Zahl bestimmen.

### **🔵 Stufe 2: Strukturierte Programme & Datenstrukturen**
11. [A01_UmrechnungEinheiten.md](./Stufe2/A01_UmrechnungVonEinheiten.md) – Celsius in Fahrenheit & andere Einheiten.
12. [A02_Primzahlen.md](./Stufe2/A02_Primzahlen.md) – Prüfen, ob eine Zahl eine Primzahl ist.
13. [A03_KleinerTextEditor.md](./Stufe2/A03_KleinerTextEditor.md) – Text schreiben, speichern und laden.
14. [A04_Stoppuhr.md](./Stufe2/A04_Stoppuhr.md) – Einführung in Timer.
15. [A05_Datenstrukturen.md](./Stufe2/A05_Datenstrukturen.md) – List, HashSet & Dictionary.

### **🟠 Stufe 3: Objektorientierte Programmierung (OOP)**
16. [A01_Menuefuehrung.md](./Stufe3/A01_KlassenUndStruktur.md) – Alle bisherigen Programme als Menü organisieren.
17. [A02_Personenklasse.md](./Stufe3/A02_KlassePerson.md) – Einführung in Klassen & Enums.
18. [A03_Adressbuch.md](./Stufe3/A03_EinfachesAdressbuch.md) – Telefonnummern speichern & abrufen.
19. [A04_ErweitertesMenue.md](./Stufe3/A04_BesseresMenu.md) – Menü mit OOP verbessern.

### **🟡 Stufe 4: Komplexe Projekte**
20. [A01_TicTacToe.md](./Stufe4/A01_TicTacToe.md) – Einführung in Spielmechaniken.
21. [A02_Hangman.md](./Stufe4/A02_Hangman.md) – Buchstaben raten & Wort aufdecken.
22. [A03_Bankkonto.md](./Stufe4/A03_Bankkonto.md) – Konto mit Ein-/Auszahlungen.
23. [A04_MehrspielerTicTacToe.md](./Stufe4/A04_TicTacToeMehrspieler_Threading.md) – Threads & Parallelisierung.

### **🟣 Stufe 5: Fortgeschrittene Themen & Datenbanken**
24. [A01_Sortieralgorithmen.md](./Stufe5/A01_Sortieralgorithmen.md) – Bubble Sort, Insertion Sort.
25. [A02_SQLDatenbank.md](./Stufe5/A02_Datenbank.md) – Einführung in Microsoft SQL Server Express.
26. [A03_ORM.md](./Stufe5/A03_ORMundLINQ.md) – Objekt-Relational Mapping & LINQ.

### **🔴 Stufe 6: API & Webentwicklung**
27. [A01_REST_API.md](./Stufe6/A01_REST_API.md) – ASP.NET Core API erstellen.
28. [A02_Tests.md](./Stufe6/A02_Testing.md) – Unit & Integration Testing mit xUnit/Postman.
29. [A03_Webseite.md](./Stufe6/A03_Webentwicklung.md) – Web-Frontend mit HTML, CSS & JavaScript.
30. [A04_GitHubBestPractices.md](./Stufe6/A04_GitHubBest.md) – Versionskontrolle & CI/CD.
31. [A05_Deployment.md](./Stufe6/A05_Deployment.md) – API & Webseite online bereitstellen.

---

## 💡 Nützliche Links
- [C# - Ceate Sheet](./Referenzen/CheatSheet_CSharp.md)
- [Microsoft C# Dokumentation](https://learn.microsoft.com/en-us/dotnet/csharp/)
- [ASP.NET Core Tutorial](https://learn.microsoft.com/en-us/aspnet/core/)
- [HTML & CSS Grundlagen](https://developer.mozilla.org/de/docs/Web/HTML)
- [JavaScript Einführung](https://developer.mozilla.org/de/docs/Web/JavaScript)
- [GitHub Markdown Guide](https://www.markdownguide.org/basic-syntax/)

---

## 🎯 Fazit & Weiteres

Diese Aufgabensammlung bietet einen **kompletten Einstieg** in **Grundlagen** der **Programmierung mit C#, objektorientierte Entwicklung, Datenbanken, Webentwicklung und DevOps**. 
