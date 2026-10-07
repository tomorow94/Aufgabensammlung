# Aufgabe A01: Menüführung mit Klassen & Struktur

## Einordnung und Lernziele

**Status:** Pflicht im Lernfaden.

**Voraussetzungen:** [List, HashSet und Dictionary](../Stufe2/A05_Datenstrukturen.md)

**Intention:** Bekannte Programme über Klassen in einem gemeinsamen Menü zusammenführen.

**Lernziele:**

- Du kannst zwei frühere Programme über Start-Methoden aufrufen.
- Du kannst den einzigen Einstiegspunkt und die Rückkehr ins Menü erklären.
- Du kannst den Projektstand in Git speichern und spätere Änderungen als Diff nachvollziehen.

**Weiter im Pflichtpfad:** [Person, Eigenschaften, Konstruktor und Enum](A02_KlassePerson.md)

## Einleitung

Bisher wurden einzelne Programme als eigenständige Konsolenanwendungen geschrieben. Diese Vorgehensweise eignet sich für den Einstieg, aber bei wachsender Anzahl von Programmen wird die Verwaltung und Erweiterung zunehmend unübersichtlich. Um dies zu verbessern, wird nun ein **strukturiertes Menü-Projekt** erstellt, das als zentraler Einstiegspunkt für schrittweise übernommene Programme dient.

### **Warum verwenden wir eine Ordnerstruktur und mehrere Klassen?**
- **Modularität:** Jedes Programm wird als separate **Klasse** organisiert, was eine saubere Trennung von Verantwortlichkeiten ermöglicht.
- **Wiederverwendbarkeit:** Bestehende Programme müssen nicht kopiert oder mehrfach geschrieben werden, sondern können direkt aufgerufen werden.
- **Erweiterbarkeit:** Neue Programme erhalten eigene Klassen und werden zunächst ausdrücklich im Menü registriert. In A04 vereinfachst du diese Registrierung mit einer gemeinsamen Schnittstelle.
- **Verbesserte Lesbarkeit:** Eine gut strukturierte Ordnerhierarchie erleichtert die Navigation im Code.

### **Warum wechseln wir jetzt auf Englisch im Code?**
- **Standard in der Softwareentwicklung:** Viele professionelle Softwareprojekte verwenden Englisch für Bezeichner und Kommentare, um internationale Zusammenarbeit zu erleichtern.
- **Einheitliche Benennung:** Englische Bezeichner und Kommentare dienen im Menüprojekt als gemeinsame Teamkonvention.
- **Bessere Lesbarkeit für andere Entwickler:** Falls das Projekt später öffentlich gemacht oder mit anderen Entwicklern geteilt wird, ist ein englischer Code allgemein verständlicher.

### **Versionsverwaltung mit GitHub**
Dein eigenes Menüprojekt wird ab hier mit **Git und GitHub** verwaltet. Falls du bereits in einem Repository arbeitest, führe dessen Versionsgeschichte weiter. Dadurch lernst du:
- **Versionskontrolle:** Änderungen werden nachvollziehbar gespeichert.
- **Backup und Zusammenarbeit:** Der Code kann jederzeit wiederhergestellt oder mit anderen geteilt werden.
- **Commit-Struktur und Branching:** Änderungen können schrittweise erfasst und dokumentiert werden.

---

## Ziel

In dieser Aufgabe entwickelst du eine **strukturierte Konsolenanwendung**, die als Menü für bisherige Programme dient. Zunächst werden zwei Programme aus dem Pflichtpfad als **eigene Klassen** in einem neuen „Menü-Projekt“ abgelegt. Weitere Programme kannst du danach ergänzen; ausgelassene Bonus-Aufgaben musst du dafür nicht nachholen. Dadurch wird das **Verständnis für Klassen, Methoden und eine sinnvolle Code-Struktur** vertieft.

## Anforderungen

1. **Neues Menü-Projekt erstellen**
   - Erstellen Sie eine **neue Konsolenanwendung**, die als zentrales Menü dient.
   - Definieren Sie eine **sinnvolle Ordnerstruktur**, in der die bisherigen Programme abgelegt werden.

2. **Bisherige Programme als eigene Klassen einbinden**
   - Übernimm zunächst zwei bisherige Programme (z. B. "Hello World" und "Guess the Number"), jeweils in eine eigene **Klasse** innerhalb des Menü-Projekts. Weitere Programme folgen schrittweise.
   - Jede dieser Klassen muss eine **öffentliche Methode `Start()`** enthalten, die das jeweilige Programm startet.

3. **Menüführung implementieren**
   - Das Menü soll dem Benutzer **eine Auswahl der vorhandenen Programme** bieten.
   - Der Benutzer kann eine **Zahl eingeben**, um ein bestimmtes Programm zu starten.
   - Die Programme werden durch die **jeweilige `Start()`-Methode** aufgerufen.

4. **Code-Struktur & Ordnerorganisation**
   - Erstelle einen Ordner `Programs` für die übernommenen Programmklassen.
   - Strukturieren Sie den Code **modular**, sodass das Menü leicht erweiterbar bleibt.

---

## Hinweise

- Nutzen Sie **Namespaces**, um den Code logisch zu organisieren (`namespace MenuApplication.Programs`).
- Verwenden Sie eine **Schleife**, um das Menü **so lange anzuzeigen, bis der Benutzer das Programm beendet**.
- Implementieren Sie **eine separate Klasse für die Menüführung**, um die Struktur übersichtlich zu halten.

---

## Beispielhafter Lösungsansatz

Die folgende **Lösungsskizze** zeigt die Aufteilung in Menü, Programmklassen und Einstiegspunkt. Passe die eingebundenen Programme und deren Aufrufe an dein eigenes Projekt an.

## Gestufte Hinweise

Versuche zuerst eine eigene Lösung. Öffne bei Bedarf zunächst Hinweis 1 und erst danach Hinweis 2; die vorhandenen Beispiele bzw. Referenzen dienen anschließend zum Vergleichen.

<details>
<summary>Hinweis 1: Denkanstoß</summary>

Welche Main-Methode gehört zum Gesamtprojekt und welche bisherigen Programme werden Unterprogramme?

</details>

<details>
<summary>Hinweis 2: Vorgehensweise</summary>

Nur das Hauptprojekt behält Main; verschiebe Unterprogramme in eigene Klassen und rufe deren Start-Methode aus dem Menü auf.

</details>

<details> <summary><strong>Lösungsvorschlag anzeigen</strong></summary>
  
### **1. Menü-Klasse (`Menu.cs`)**

```csharp
using System;
using MenuApplication.Programs;

namespace MenuApplication
{
    class Menu
    {
        public void Start()
        {
            while (true)
            {
                Console.WriteLine("===== Main Menu =====");
                Console.WriteLine("1. Hello World");
                Console.WriteLine("2. Guess the Number");
                Console.WriteLine("3. Stopwatch");
                Console.WriteLine("0. Exit");
                Console.Write("Select a program: ");

                string? input = Console.ReadLine();

                if (input is null) return;
                switch (input)
                {
                    case "1":
                        new HelloWorld().Start();
                        break;
                    case "2":
                        new GuessTheNumber().Start();
                        break;
                    case "3":
                        new StopwatchProgram().Start();
                        break;
                    case "0":
                        Console.WriteLine("Exiting program...");
                        return;
                    default:
                        Console.WriteLine("Invalid input. Please try again.");
                        break;
                }
                Console.WriteLine();
            }
        }
    }
}
```

### **2. Beispiel für eine Programm-Klasse (HelloWorld.cs)**

```csharp
namespace MenuApplication.Programs
{
    class HelloWorld
    {
        public void Start()
        {
            Console.WriteLine("Hello, World!");
        }
    }
}
```

### **3. Program.cs – Einstiegspunkt**

```csharp
namespace MenuApplication
{
    class Program
    {
        static void Main()
        {
            new Menu().Start();
        }
    }
}
```

</details>

## Abschluss

Diese Aufgabe bildet die Grundlage für ein gut strukturiertes Projekt. Sie fördert Modularität, Wiederverwendbarkeit und Code-Organisation. In zukünftigen Aufgaben wird darauf aufgesetzt.

Nächster Schritt:

- Erstelle für dein eigenes Projekt ein privates Repository auf GitHub, falls noch keines vorhanden ist. Initialisiere ein vorhandenes Repository nicht erneut.
- Lege vor dem ersten Commit eine `.gitignore` an, insbesondere für `bin`, `obj` und `.vs`. Füge die Quelldateien und Projektdateien hinzu.
- Dokumentieren Sie Änderungen mit sinnvollen Commit-Nachrichten.

## Schrittweise Übernahme

Starte mit Hallo Welt und einer Rechenaufgabe. Ersetze deren `Main()` durch eine öffentliche `Start()`-Methode; nur das Hauptprojekt behält `Main()`. Füge anschließend weitere Programme hinzu. Im Menü müssen anfangs neue Einträge und Aufrufe ergänzt werden. Für das Beispiel sind `GuessTheNumber` und `StopwatchProgram` deine eigenen umgebauten Klassen, keine mitgelieferten Bibliothekstypen.

## Selbst prüfen

Ein gültiger Menüpunkt startet sein Programm und kehrt anschließend ins Menü zurück. Ungültiger Text erzeugt eine Meldung. `0` beendet. Nur das Hauptprojekt enthält einen Einstiegspunkt; überprüfe, dass keine kopierten `Main()`-Methoden als zweite Einstiegspunkte verbleiben.

## Bonus: Andere Registrierung und Oberfläche

**Intention:** Untersuche zusätzliche Wege erst nach der grundlegenden Menüstruktur.

**Lernziel:** Du kannst nach A04 explizite Registrierung und Reflection unterscheiden; eine Desktop-GUI erfordert zusätzliche UI-Kenntnisse außerhalb dieses Lernfadens.

 - Dynamische Programmliste: Laden Sie die vorhandenen Klassen automatisch, statt sie manuell im switch-Statement zu hinterlegen.
 - Reflection nutzen: Untersuche nach A04 die Typen einer Assembly und filtere gezielt die Implementierungen deiner Schnittstelle. `Type.GetType()` löst einen bekannten Typnamen auf; es entdeckt keine Programmliste automatisch.
 - **Desktopoberfläche außerhalb des Pflichtpfads:** Windows Forms oder WPF setzen zusätzliche UI-Kenntnisse voraus. Intention: dieselben Programme mit einer anderen Oberfläche aufrufen. Lernziel: bekannte `Start()`-Aufrufe auf Button-Ereignisse abbilden.

## Passende Lernquellen

[Leseempfehlung für diesen Lernschritt](../Referenzen/Lernquellen.md#stufe-3-struktur-und-versionsgeschichte). Wähle den dort genannten Abschnitt zur aktuellen Aufgabe und probiere ihn in deinem eigenen Programm aus.
