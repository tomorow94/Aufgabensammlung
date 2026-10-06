# 🟢 Aufgabe A06: Multiplikation und Wiederholung

## Ziel und Voraussetzungen

Du kannst bereits Zahlen einlesen, vergleichen und mit `TryParse` prüfen. Jetzt wiederholst du eine Berechnung mit einer **`while`-Schleife**. Eine Schleife führt ihren Block erneut aus, solange ihre Bedingung wahr ist.

## Anforderungen

1. Lies zwei Zahlen ein und gib ihr Produkt aus.
2. Bei ungültigen Eingaben beginne einen neuen Durchlauf.
3. Nach einer Berechnung fragt das Programm, ob du weiterrechnen möchtest.

`continue` startet den nächsten Schleifendurchlauf. `break` beendet die Schleife. Der Vergleich mit `OrdinalIgnoreCase` akzeptiert `j` und `J`.

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
            Console.Write("Erste Zahl (oder Ende der Eingabe zum Beenden): ");
            string? text = Console.ReadLine();
            if (text is null) break;
            if (!double.TryParse(text, out double a) || !double.IsFinite(a))
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
            double product = a * b;
            Console.WriteLine(double.IsFinite(product) ? $"Produkt: {product}" : "Ergebnis außerhalb des Zahlenbereichs.");
            Console.Write("Noch einmal? (j/n): ");
            if (!string.Equals(Console.ReadLine()?.Trim(), "j", StringComparison.OrdinalIgnoreCase)) break;
        }
    }
}
```

</details>

## Selbst prüfen

| Ablauf | Erwartung |
|---|---|
| `3`, `4`, `n` | `12`, Programm endet |
| `-3`, `4`, `j`, `0`, `9`, `n` | `-12`, dann `0` |
| `abc`, danach gültige Zahlen | Meldung, anschließend neue Eingabe |
| Antwort `J` | weitere Berechnung |

Setze einen Haltepunkt am Schleifenanfang. Verfolge, wohin `continue` und `break` springen. Zusatz: Zähle die erfolgreichen Berechnungen.
