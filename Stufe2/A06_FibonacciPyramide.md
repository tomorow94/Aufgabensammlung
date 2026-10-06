# 🔵 Bonus A06: Fibonacci-Pyramide

## Einordnung und Lernziele

**Status:** Bonus (optional; keine Voraussetzung für spätere Pflichtaufgaben).

**Voraussetzungen:** [Fibonacci als Zahlenfolge](../Stufe1/A10_Fibonacci.md), [List, HashSet und Dictionary](A05_Datenstrukturen.md)

**Intention:** Methoden, Listen und verschachtelte Schleifen an einer zusätzlichen Darstellung verbinden.

**Lernziele:**

- Du kannst eine Fibonacci-Liste getrennt von ihrer Darstellung erzeugen.
- Du kannst Zeilenlänge und Einrückung einer Pyramide systematisch bestimmen.

**Weiter im Pflichtpfad:** [Menüführung mit Klassen & Struktur](../Stufe3/A01_KlassenUndStruktur.md)

## Ziel und Voraussetzungen

Nach [Fibonacci](../Stufe1/A10_Fibonacci.md) und [Datenstrukturen](A05_Datenstrukturen.md) kombinierst du **Methoden, Listen und verschachtelte Schleifen**. Löse die Teile nacheinander: erst die Liste, dann eine einfache Pyramide aus `*`, zuletzt die Zahlenpyramide.

## Anforderungen

1. Schreibe `CalculateFibonacci(int count)` für 1 bis 47 Werte.
2. Teste die Methode zunächst ohne Formatierung.
3. Gib jede Zeile vorwärts und rückwärts aus; der mittlere Wert erscheint einmal.
4. Benutze gleich breite Zahlenfelder. Dadurch bleibt die Ausgabe auch mit mehrstelligen Zahlen symmetrisch.

## Gestufte Hinweise

Versuche zuerst eine eigene Lösung. Öffne bei Bedarf zunächst Hinweis 1 und erst danach Hinweis 2; die vorhandenen Beispiele bzw. Referenzen dienen anschließend zum Vergleichen.

<details>
<summary>Hinweis 1: Denkanstoß</summary>

Welche Daten werden berechnet und welche betreffen nur die Ausgabe?

</details>

<details>
<summary>Hinweis 2: Vorgehensweise</summary>

Erzeuge erst die Liste, dann eine Sternpyramide; ersetze erst danach Sterne durch die entsprechenden Zahlen.

</details>

<details>
<summary>Lösungsvorschlag für Program.cs (.NET 10)</summary>

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
class Program
{
    static void Main()
    {
        Console.Write("Anzahl (1–47; für schmale Konsolen höchstens 10): ");
        if (!int.TryParse(Console.ReadLine(), out int count) || count < 1 || count > 47)
        {
            Console.WriteLine("Ungültige Anzahl.");
            return;
        }
        PrintPyramid(CalculateFibonacci(count));
    }
    static List<int> CalculateFibonacci(int count)
    {
        if (count < 1 || count > 47) throw new ArgumentOutOfRangeException(nameof(count));
        var values = new List<int> { 0 };
        if (count >= 2) values.Add(1);
        for (int i = 2; i < count; i++) values.Add(checked(values[i - 1] + values[i - 2]));
        return values;
    }
    static void PrintPyramid(List<int> values)
    {
        int width = values.Max().ToString().Length + 1;
        for (int row = 0; row < values.Count; row++)
        {
            Console.Write(new string(' ', (values.Count - row - 1) * width));
            for (int col = 0; col <= row; col++) Console.Write(values[col].ToString().PadLeft(width));
            for (int col = row - 1; col >= 0; col--) Console.Write(values[col].ToString().PadLeft(width));
            Console.WriteLine();
        }
    }
}
```

</details>

## Selbst prüfen

`1` erzeugt genau eine Zeile mit `0`, `2` genau zwei Zeilen. Bei `8` enthält die letzte Zeile `13`; die Zahlenfelder müssen weiterhin gleich breit sein. `47` enthält keine negativen Werte; die vollständige Pyramide braucht aber ein sehr breites Fenster. `0`, `48` und `abc` werden abgewiesen.

## Bonus: Rekursion untersuchen

**Intention:** Vergleiche eine andere Berechnungsweise und ihre Kosten.

**Lernziel:** Du kannst Abbruchfälle und wiederholte rekursive Aufrufe im Aufrufstapel zeigen.


Eine rekursive Methode ruft sich selbst auf. Definiere zunächst die Abbruchfälle `F(0)=0` und `F(1)=1`. Die naive Formel `F(n)=F(n-1)+F(n-2)` wiederholt viele Berechnungen und ist exponentiell teuer. Begrenze dieses Experiment auf `0–25`; beobachte den Aufrufstapel mit Haltepunkten. Vergleiche danach eine iterative Lösung oder speichere bereits berechnete Werte (Memoisierung). Rekursion ist hier eine Untersuchung, keine Verbesserung der effizienten Schleife.

## Passende Lernquellen

[Leseempfehlung für diesen Lernschritt](../Referenzen/Lernquellen.md#stufe-2-methoden-und-fehlersuche). Wähle den dort genannten Abschnitt zur aktuellen Aufgabe und probiere ihn in deinem eigenen Programm aus.
