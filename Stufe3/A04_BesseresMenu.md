# Aufgabe A04: Erweiterung des Menüs mit OOP-Struktur

## Ziel

Das bestehende **Menü-Projekt** soll weiterentwickelt werden, um eine **bessere Organisation der Programme** zu erreichen. Anstatt jeden Menüpunkt direkt aufzurufen, werden nun **alle Programme als eigene Klassen mit einer gemeinsamen Struktur** organisiert. Dies hilft, die Grundkonzepte von **Vererbung, Schnittstellen oder abstrakten Klassen** in der objektorientierten Programmierung (OOP) zu verstehen.

Zusätzlich soll eine **Navigationsfunktion** in die Basisklasse integriert werden, die es ermöglicht, **mit `Ctrl + B` eine Ebene zurück oder mit `Ctrl + M` direkt ins Hauptmenü zu wechseln**.

---

## Anforderungen

1. **Basisklasse für Programme mit Navigationsfunktion**
   - Erstellen Sie eine **Basisklasse `BaseProgram`**, von der alle Programme erben.
   - Diese Basisklasse enthält eine **`Start()`-Methode**, die in den Kindklassen überschrieben wird.
   - Fügen Sie eine **Navigationsmethode** hinzu, die es ermöglicht:
     - Mit `Ctrl + B` eine Ebene zurückzugehen.
     - Mit `Ctrl + M` ins Hauptmenü zurückzukehren.

2. **Programme in eigenen Klassen verwalten**
   - Alle Programme müssen nun von `BaseProgram` erben.
   - Die bisher im Menü aufgerufenen Programme müssen auf die neue Struktur umgestellt werden.

3. **Menü dynamisch generieren**
   - Das Menü soll die vorhandenen Programme **automatisch** erkennen.
   - Statt manueller `switch`-Abfragen soll eine **Liste von Programmklassen** verwendet werden.
   - Das Menü ruft das jeweilige Programm durch `Start()` auf.

---

## Hinweise

- Nutzen Sie **Reflection oder eine generische Liste**, um Programme zu verwalten.
- Die Navigation sorgt für eine **bessere Benutzerführung** und ermöglicht eine flexible Menüstruktur.
- `Ctrl + B` und `Ctrl + M` verhindern versehentliche Eingaben und verbessern die Bedienbarkeit.

---

## Beispielhafter Lösungsansatz

### **1. Erstellung der `BaseProgram`-Klasse mit Navigation**

```csharp
using System;

public abstract class BaseProgram
{
    protected void NavigateBack()
    {
        Console.WriteLine("\nPress 'Ctrl + B' to go back or 'Ctrl + M' to return to the main menu.");

        while (true)
        {
            var key = Console.ReadKey(intercept: true);

            if (key.Modifiers.HasFlag(ConsoleModifiers.Control))
            {
                if (key.Key == ConsoleKey.B)
                {
                    return; // Goes back to the previous menu level
                }
                if (key.Key == ConsoleKey.M)
                {
                    throw new Exception("MainMenu"); // Exception used for menu navigation
                }
            }

            Console.WriteLine("Invalid input. Press 'Ctrl + B' to go back or 'Ctrl + M' to return to the main menu.");
        }
    }

    public abstract void Start();
}
```

### **2. Programme erben von `BaseProgram`**

```csharp
public class HelloWorld : BaseProgram
{
    public override void Start()
    {
        Console.WriteLine("Hello, World!");
        NavigateBack();
    }
}
```

### **3. Menü mit automatischer Programmsuche und Navigation**

```csharp
using System;
using System.Collections.Generic;

namespace MenuApplication
{
    class Menu
    {
        private List<BaseProgram> programs = new List<BaseProgram>
        {
            new HelloWorld(),
            new GuessTheNumber(),
            new StopwatchProgram()
        };

        public void Start()
        {
            while (true)
            {
                try
                {
                    Console.WriteLine("===== Main Menu =====");
                    for (int i = 0; i < programs.Count; i++)
                    {
                        Console.WriteLine($"{i + 1}. {programs[i].GetType().Name}");
                    }
                    Console.WriteLine("0. Exit");
                    Console.Write("Select a program: ");

                    if (int.TryParse(Console.ReadLine(), out int choice) && choice > 0 && choice <= programs.Count)
                    {
                        programs[choice - 1].Start();
                    }
                    else if (choice == 0)
                    {
                        Console.WriteLine("Exiting...");
                        break;
                    }
                    else
                    {
                        Console.WriteLine("Invalid selection. Try again.");
                    }
                }
                catch (Exception ex) when (ex.Message == "MainMenu")
                {
                    // Catch the exception and loop back to main menu
                }
            }
        }
    }
}
```

### **4. Hauptprogramm**

```csharp
class Program
{
    static void Main()
    {
        new Menu().Start();
    }
}
```

## Erweiterungsmöglichkeiten

- **Reflection nutzen**: Finden und instanziieren Sie Klassen **automatisch** durch `Assembly.GetExecutingAssembly()`.
- **Kategorien einführen**: Programme könnten in **Untermenüs** nach Themen gruppiert werden.
- **Logging-Funktion**: Speichern Sie, wann welche Programme gestartet wurden.

## Vorteile dieser Erweiterung:

- **Bessere Strukturierung**: Jedes Programm ist nun eine eigene Klasse.
- **Flexiblere Navigation**: Benutzer können gezielt zurück oder direkt ins Hauptmenü springen.
- **Leichtere Erweiterbarkeit**: Neue Programme können einfach hinzugefügt werden.

Diese Anpassung verbessert das Menü-Projekt nachhaltig, macht die Navigation intuitiver und bereitet auf komplexere OOP-Konzepte vor! 🚀
