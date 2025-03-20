# Aufgabe A01: Menüführung mit Klassen & Struktur

## Einleitung

Bisher wurden einzelne Programme als eigenständige Konsolenanwendungen geschrieben. Diese Vorgehensweise eignet sich für den Einstieg, aber bei wachsender Anzahl von Programmen wird die Verwaltung und Erweiterung zunehmend unübersichtlich. Um dies zu verbessern, wird nun ein **strukturiertes Menü-Projekt** erstellt, das als zentraler Einstiegspunkt für alle bisherigen Programme dient.

### **Warum verwenden wir eine Ordnerstruktur und mehrere Klassen?**
- **Modularität:** Jedes Programm wird als separate **Klasse** organisiert, was eine saubere Trennung von Verantwortlichkeiten ermöglicht.
- **Wiederverwendbarkeit:** Bestehende Programme müssen nicht kopiert oder mehrfach geschrieben werden, sondern können direkt aufgerufen werden.
- **Erweiterbarkeit:** Neue Programme können einfach hinzugefügt werden, indem neue Klassen erstellt werden, ohne das Hauptmenü zu verändern.
- **Verbesserte Lesbarkeit:** Eine gut strukturierte Ordnerhierarchie erleichtert die Navigation im Code.

### **Warum wechseln wir jetzt auf Englisch im Code?**
- **Standard in der Softwareentwicklung:** Die meisten professionellen Softwareprojekte verwenden Englisch als Programmiersprache, um internationale Zusammenarbeit zu erleichtern.
- **Vermeidung von Codierungsproblemen:** Deutsche Umlaute (ä, ö, ü) und Sonderzeichen können in bestimmten Umgebungen zu Fehlern führen.
- **Bessere Lesbarkeit für andere Entwickler:** Falls das Projekt später öffentlich gemacht oder mit anderen Entwicklern geteilt wird, ist ein englischer Code allgemein verständlicher.

### **Versionsverwaltung mit GitHub**
Dieses Projekt wird das erste sein, das mit **GitHub** verwaltet wird. Dadurch lernen Sie:
- **Versionskontrolle:** Änderungen werden nachvollziehbar gespeichert.
- **Backup und Zusammenarbeit:** Der Code kann jederzeit wiederhergestellt oder mit anderen geteilt werden.
- **Commit-Struktur und Branching:** Änderungen können schrittweise erfasst und dokumentiert werden.

---

## Ziel

In dieser Aufgabe sollen Sie eine **strukturierte Konsolenanwendung** entwickeln, die als Menü für bisherige Programme dient. Dabei werden alle bisherigen Programme als **eigene Klassen** in einem neuen "Menü-Projekt" abgelegt. Dadurch wird das **Verständnis für Klassen, Methoden und eine sinnvolle Code-Struktur** vertieft.

## Anforderungen

1. **Neues Menü-Projekt erstellen**
   - Erstellen Sie eine **neue Konsolenanwendung**, die als zentrales Menü dient.
   - Definieren Sie eine **sinnvolle Ordnerstruktur**, in der die bisherigen Programme abgelegt werden.

2. **Bisherige Programme als eigene Klassen einbinden**
   - Jedes bisherige Programm (z. B. "Hello World", "Guess the Number", "Stopwatch") soll in einer eigenen **Klasse** innerhalb des Menü-Projekts liegen.
   - Jede dieser Klassen muss eine **öffentliche Methode `Start()`** enthalten, die das jeweilige Programm startet.

3. **Menüführung implementieren**
   - Das Menü soll dem Benutzer **eine Auswahl der vorhandenen Programme** bieten.
   - Der Benutzer kann eine **Zahl eingeben**, um ein bestimmtes Programm zu starten.
   - Die Programme werden durch die **jeweilige `Start()`-Methode** aufgerufen.

4. **Code-Struktur & Ordnerorganisation**
   - Erstellen Sie einen Ordner `Programs`, in dem alle bisherigen Programme als **eigene Klassen** abgelegt werden.
   - Strukturieren Sie den Code **modular**, sodass das Menü leicht erweiterbar bleibt.

---

## Hinweise

- Nutzen Sie **Namespaces**, um den Code logisch zu organisieren (`namespace MenuApplication.Programs`).
- Verwenden Sie eine **Schleife**, um das Menü **so lange anzuzeigen, bis der Benutzer das Programm beendet**.
- Implementieren Sie **eine separate Klasse für die Menüführung**, um die Struktur übersichtlich zu halten.

---

## Beispielhafter Lösungsansatz

Da wir ab Stufe 3 nicht mehr alle Details über das Projekt wissen, geben wir hier nur eine **mögliche Lösungsskizze** für die Umsetzung.

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

                string input = Console.ReadLine();
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

## Erweiterungsmöglichkeiten
 - Dynamische Programmliste: Laden Sie die vorhandenen Klassen automatisch, statt sie manuell im switch-Statement zu hinterlegen.
 - Reflexion nutzen: Durch Reflection (Type.GetType()) könnten neue Programme automatisch im Menü erscheinen, ohne den Code ändern zu müssen.
 - GUI statt Konsole: Erweitern Sie das Projekt später mit Windows Forms oder WPF, um ein visuelles Menü zu erstellen.

## Abschluss

Diese Aufgabe bildet die Grundlage für ein gut strukturiertes Projekt. Sie fördert Modularität, Wiederverwendbarkeit und Code-Organisation. In zukünftigen Aufgaben wird darauf aufgesetzt.

Nächster Schritt:

- Erstellen Sie ein privates Repository auf GitHub, um die Versionskontrolle für dieses Projekt einzuführen.
- Fügen Sie alle Projektdateien hinzu und machen Sie den ersten Commit.
- Dokumentieren Sie Änderungen mit sinnvollen Commit-Nachrichten.
