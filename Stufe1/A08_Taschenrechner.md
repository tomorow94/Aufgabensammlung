# 🟢 Aufgabe A08: Taschenrechner mit Menü

## Ziel und Voraussetzungen

Kombiniere Eingabeprüfung, Bedingungen und Schleifen zu einem Taschenrechner. Neu ist **`switch`**: abhängig von einer Auswahl wird genau ein passender Zweig ausgeführt.

## Anforderungen

1. Biete `+`, `-`, `*`, `/` und `0` zum Beenden an.
2. Prüfe beide Zahlen und verhindere die Division durch null.
3. Nach einer Rechnung erscheint wieder das Menü.

<details>
<summary>Lösungsvorschlag für Program.cs (.NET 10)</summary>

```csharp
using System;
class Program
{
    static void Main()
    {
        while (true)
        {
            Console.Write("Operation (+, -, *, /; 0 = Ende): ");
            string? operation = Console.ReadLine()?.Trim();
            if (operation is null or "0") return;
            if (operation != "+" && operation != "-" && operation != "*" && operation != "/")
            {
                Console.WriteLine("Ungültige Operation.");
                continue;
            }
            Console.Write("Erste Zahl: ");
            if (!double.TryParse(Console.ReadLine(), out double a) || !double.IsFinite(a))
            {
                Console.WriteLine("Ungültige Zahl.");
                continue;
            }
            Console.Write("Zweite Zahl: ");
            if (!double.TryParse(Console.ReadLine(), out double b) || !double.IsFinite(b))
            {
                Console.WriteLine("Ungültige Zahl.");
                continue;
            }
            if (operation == "/" && b == 0)
            {
                Console.WriteLine("Division durch null ist nicht erlaubt.");
                continue;
            }
            double result = 0;
            switch (operation)
            {
                case "+": result = a + b; break;
                case "-": result = a - b; break;
                case "*": result = a * b; break;
                case "/": result = a / b; break;
            }
            Console.WriteLine(double.IsFinite(result) ? $"Ergebnis: {result}" : "Ergebnis außerhalb des Zahlenbereichs.");
        }
    }
}
```

</details>

## Selbst prüfen

| Operation und Zahlen | Erwartung |
|---|---|
| `+`, `2`, `3` | `5` |
| `-`, `2`, `3` | `-1` |
| `*`, `2`, `3` | `6` |
| `/`, `7`, `2` | `3,5` in deutscher Umgebung |
| `/`, `2`, `0` | Fehlermeldung, danach Menü |
| `?`, `abc`, leere Zahleneingabe | Meldung, kein Absturz |
| `0` im Menü | Programm endet |

Setze einen Haltepunkt an `switch` und gehe mit F10 durch eine Division. Zusatz für **Stufe 2**: Schreibe `static double Calculate(double a, double b, string operation)` und trenne reine Berechnung von Konsoleneingaben. Verwende gezielte Exceptions nur für unzulässige Methodenargumente; gewöhnliche Menüauswahl benötigt keine Exception.
