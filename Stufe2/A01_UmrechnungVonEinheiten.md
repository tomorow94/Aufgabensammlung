# Aufgabe A01: Umrechnung von Einheiten

## Ziel

Entwickeln Sie ein C#-Programm, das verschiedene Einheiten umrechnet. Beispiele hierfür sind:

- Celsius zu Fahrenheit
- Kilometer zu Meilen

## Anleitung

1. **Neues Projekt erstellen:**
   - Starten Sie Visual Studio.
   - Wählen Sie "Neues Projekt erstellen" aus.
   - Wählen Sie den Projekttyp "Konsolenanwendung" aus.
   - Geben Sie dem Projekt einen aussagekräftigen Namen, z. B. "EinheitenUmrechner".

2. **Programmstruktur:**
   - Das Programm sollte den Benutzer fragen, welche Umrechnung durchgeführt werden soll.
   - Basierend auf der Auswahl des Benutzers sollte das Programm die entsprechende Umrechnung durchführen und das Ergebnis anzeigen.

3. **Beispielhafte Umrechnungen:**
   - **Celsius zu Fahrenheit:** Die Formel lautet: `F = (C * 9/5) + 32`
   - **Kilometer zu Meilen:** Die Umrechnung erfolgt mit dem Faktor 1 Kilometer = 0,621371 Meilen.

4. **Benutzereingaben:**
   - Verwenden Sie `Console.ReadLine()`, um Eingaben vom Benutzer zu erhalten.
   - Validieren Sie die Eingaben und behandeln Sie ungültige Eingaben entsprechend.

<details>
<summary><strong>Lösungsvorschlag anzeigen</strong></summary>

```csharp
using System;

namespace EinheitenUmrechner
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Wählen Sie die Umrechnung:");
            Console.WriteLine("1: Celsius zu Fahrenheit");
            Console.WriteLine("2: Kilometer zu Meilen");
            Console.Write("Ihre Auswahl: ");
            string auswahl = Console.ReadLine();

            switch (auswahl)
            {
                case "1":
                    Console.Write("Geben Sie die Temperatur in Celsius ein: ");
                    if (double.TryParse(Console.ReadLine(), out double celsius))
                    {
                        double fahrenheit = (celsius * 9 / 5) + 32;
                        Console.WriteLine($"{celsius}°C entsprechen {fahrenheit}°F.");
                    }
                    else
                    {
                        Console.WriteLine("Ungültige Eingabe.");
                    }
                    break;
                case "2":
                    Console.Write("Geben Sie die Entfernung in Kilometern ein: ");
                    if (double.TryParse(Console.ReadLine(), out double kilometer))
                    {
                        double meilen = kilometer * 0.621371;
                        Console.WriteLine($"{kilometer} km entsprechen {meilen} Meilen.");
                    }
                    else
                    {
                        Console.WriteLine("Ungültige Eingabe.");
                    }
                    break;
                default:
                    Console.WriteLine("Ungültige Auswahl.");
                    break;
            }
        }
    }
}
```
</details>

## Hinweise

- **Fehlerbehandlung:** Stellen Sie sicher, dass das Programm ungültige Eingaben erkennt und den Benutzer entsprechend informiert. Verwenden Sie hierfür die `try-catch`-Struktur, um Ausnahmen abzufangen und geeignete Fehlermeldungen auszugeben.

- **Modularität:** Erstellen Sie für jede Umrechnung eine eigene Methode, um den Code übersichtlicher und wartbarer zu gestalten. Methoden ermöglichen es, bestimmte Aktionen zu kapseln und bei Bedarf mehrfach aufzurufen.

## Weiterführende Aufgaben

- **Weitere Umrechnungen hinzufügen:** Erweitern Sie das Programm um zusätzliche Umrechnungen, wie zum Beispiel:
  - Kilogramm zu Pfund
  - Liter zu Gallonen

- **Menü implementieren:** Entwickeln Sie ein Menü, das dem Benutzer ermöglicht, zwischen verschiedenen Umrechnungen zu wählen, ohne das Programm neu zu starten. Dies verbessert die Benutzerfreundlichkeit und Flexibilität des Programms.
