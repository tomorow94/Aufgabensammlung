# 🟢 Aufgabe A05: Subtraktion und sichere Zahleneingabe

## Ziel und Voraussetzungen

Nach Addition und Zahlenvergleich berechnest du eine Differenz. Neu ist die **Eingabeprüfung mit `TryParse`**: `abc` soll das Programm nicht mehr zum Absturz bringen. Erstelle eine C#-Konsolenanwendung mit .NET 10 und ersetze den Inhalt von `Program.cs`.

## Anforderungen

1. Lies zwei Zahlen ein und berechne erste minus zweite Zahl.
2. Prüfe beide Eingaben. Bei ungültigem Text gib eine Meldung aus und beende die Berechnung.
3. Nutze negative Zahlen und Kommazahlen. Das Dezimaltrennzeichen richtet sich nach der Spracheinstellung des Rechners, in einer deutschen Umgebung etwa `5,5`.

`TryParse(text, out zahl)` liefert `true`, wenn die Umwandlung gelingt. `out` schreibt den Zahlenwert in die Variable. `!` kehrt einen Wahrheitswert um; `||` bedeutet „oder“. `return` beendet hier die Methode `Main`.

<details>
<summary>Lösungsvorschlag</summary>

```csharp
using System;
class Program
{
    static void Main()
    {
        Console.Write("Erste Zahl: ");
        if (!double.TryParse(Console.ReadLine(), out double a) || !double.IsFinite(a))
        {
            Console.WriteLine("Bitte eine gültige, endliche Zahl eingeben.");
            return;
        }
        Console.Write("Zweite Zahl: ");
        if (!double.TryParse(Console.ReadLine(), out double b) || !double.IsFinite(b))
        {
            Console.WriteLine("Bitte eine gültige, endliche Zahl eingeben.");
            return;
        }
        Console.WriteLine($"{a} minus {b} ergibt {a - b}.");
    }
}
```

`IsFinite` schließt die Sonderwerte `NaN` und Unendlich aus. Die Zahlen sollen hier gewöhnliche Rechenwerte sein.

</details>

## Selbst prüfen

| Eingaben | Erwartung |
|---|---|
| `10`, `4` | `6` |
| `4`, `10` | `-6` |
| `5,5`, `2` (deutsche Umgebung) | `3,5` |
| `abc` oder leere Eingabe | Meldung, keine Berechnung |

Setze einen Haltepunkt an die erste `if`-Bedingung. Beobachte `a` bei gültiger und ungültiger Eingabe. Zusatz: Wiederhole die Eingabe, bis eine gültige Zahl vorliegt; dafür lernst du in der nächsten Aufgabe eine Schleife kennen.
