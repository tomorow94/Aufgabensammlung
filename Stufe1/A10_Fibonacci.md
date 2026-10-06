# 🟢 Aufgabe A10: Fibonacci als Zahlenfolge

## Ziel und Voraussetzungen

Du kennst Schleifen und Variablen. Jetzt lernst du die **`for`-Schleife** an einer Zahlenfolge: Jeder neue Wert ist die Summe der beiden vorherigen. Wir beginnen mit `0, 1, 1, 2, 3, 5, …`.

## Anforderungen

1. Frage nach einer Anzahl zwischen **1 und 47**.
2. Gib genau so viele Fibonacci-Zahlen aus.
3. Behandle `1`, `2`, ungültigen Text und Werte außerhalb des Bereichs.

`int` reicht für `F(0)` bis `F(46)`; `F(47)` ist zu groß. Da wir bei null anfangen, entsprechen 47 ausgegebene Werte den Indizes `0–46`. Große Zahlenbereiche sind eine spätere Erweiterung mit `long` oder `BigInteger`.

<details>
<summary>Lösungsvorschlag für Program.cs (.NET 10)</summary>

```csharp
using System;
class Program
{
    static void Main()
    {
        Console.Write("Wie viele Werte (1–47)? ");
        if (!int.TryParse(Console.ReadLine(), out int count) || count < 1 || count > 47)
        {
            Console.WriteLine("Bitte eine ganze Zahl zwischen 1 und 47 eingeben.");
            return;
        }
        int previous = 0;
        int current = 1;
        for (int i = 0; i < count; i++)
        {
            int value;
            if (i == 0) value = previous;
            else if (i == 1) value = current;
            else
            {
                int next = checked(previous + current);
                previous = current;
                current = next;
                value = current;
            }
            Console.Write(value + (i + 1 == count ? "\n" : " "));
        }
    }
}
```

</details>

## Selbst prüfen und debuggen

| Eingabe | Erwartung |
|---|---|
| `1` | nur `0` |
| `2` | `0 1` |
| `5` | `0 1 1 2 3` |
| `47` | 47 Werte, letzter Wert `1836311903` |
| `0`, `48`, `abc` | Meldung, keine Berechnung |

Beobachte `previous`, `current` und `next` mit F10. `checked` meldet einen Ganzzahlüberlauf, statt unbemerkt falsche Zahlen zu erzeugen.

Nach den Datenstrukturen in Stufe 2 folgt die optionale [Fibonacci-Pyramide](../Stufe2/A06_FibonacciPyramide.md). Dort übst du Listen, verschachtelte Schleifen und Methoden getrennt vom ersten Einstieg.
