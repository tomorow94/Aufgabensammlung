# 🟣 Aufgabe A01: Sortieralgorithmen fair vergleichen

## Einordnung und Lernziele

**Status:** Pflicht im Lernfaden.

**Voraussetzungen:** [Einfaches Bankkonto-System](../Stufe4/A03_Bankkonto.md)

**Intention:** Algorithmen zuerst auf Korrektheit, dann auf Laufzeit vergleichen.

**Lernziele:**

- Du kannst Bubble Sort und Insertion Sort auf Grenzfällen prüfen.
- Du kannst identische Ausgangsdaten und mehrere Messungen für einen Vergleich verwenden.

**Weiter im Pflichtpfad:** [Adressbuch mit SQL Server und ADO.NET](A02_Datenbank.md)

## Ziel und Voraussetzungen

Du kennst Arrays, Methoden und Laufzeitmessung. Implementiere Bubble Sort und Insertion Sort, prüfe zuerst ihre Ergebnisse und vergleiche dann die Laufzeiten. Beide sind bei zufälligen großen Arrays typischerweise O(n²); bereits sortierte Eingaben können sich anders verhalten.

## Anforderungen

1. Implementiere beide Algorithmen in eigenen Methoden.
2. Prüfe leere Arrays, ein Element, Duplikate, negative Werte und umgekehrte Reihenfolge.
3. Gib für ein kleines Array die Werte vor und nach der Sortierung aus.
4. Vergleiche verschiedene Größen und Eingabeordnungen mit identischen Ausgangsdaten.
5. Klone das Ausgangsarray **vor** der Zeitmessung. Ein Algorithmus darf nicht das schon sortierte Ergebnis eines anderen bekommen.
6. Wärme beide Algorithmen auf; miss mehrere Läufe im Release-Build ohne Debugger. Verwende `TotalMilliseconds` statt ganzer Millisekunden. Ausgabe und Ergebnisprüfung gehören außerhalb der Messung.

## Gestufte Hinweise

Versuche zuerst eine eigene Lösung. Öffne bei Bedarf zunächst Hinweis 1 und erst danach Hinweis 2; die vorhandenen Beispiele bzw. Referenzen dienen anschließend zum Vergleichen.

<details>
<summary>Hinweis 1: Denkanstoß</summary>

Wie verhinderst du, dass der zweite Algorithmus schon sortierte Daten erhält?

</details>

<details>
<summary>Hinweis 2: Vorgehensweise</summary>

Kopiere die Ausgangsdaten für jeden Lauf; vergleiche Resultate mit Array.Sort, bevor du Laufzeiten bewertest.

</details>

<details>
<summary>Vollständiges Beispiel für Program.cs (.NET 10)</summary>

```csharp
using System;
using System.Diagnostics;
using System.Linq;
class SortingAlgorithms
{
    static void BubbleSort(int[] array)
    {
        for (int end = array.Length - 1; end > 0; end--)
        {
            bool swapped = false;
            for (int i = 0; i < end; i++)
            {
                if (array[i] > array[i + 1])
                {
                    (array[i], array[i + 1]) = (array[i + 1], array[i]);
                    swapped = true;
                }
            }
            if (!swapped) return;
        }
    }
    static void InsertionSort(int[] array)
    {
        for (int i = 1; i < array.Length; i++)
        {
            int key = array[i];
            int j = i - 1;
            while (j >= 0 && array[j] > key)
            {
                array[j + 1] = array[j];
                j--;
            }
            array[j + 1] = key;
        }
    }
    static double Measure(int[] source, Action<int[]> sort)
    {
        int[] copy = (int[])source.Clone();
        var watch = Stopwatch.StartNew();
        sort(copy);
        watch.Stop();
        int[] expected = (int[])source.Clone();
        Array.Sort(expected);
        if (!copy.SequenceEqual(expected)) throw new InvalidOperationException("Falsches Sortierergebnis.");
        return watch.Elapsed.TotalMilliseconds;
    }
    static void Main()
    {
        int[][] cases = { Array.Empty<int>(), new[] { 1 }, new[] { 3, -1, 3, 0 }, new[] { 5, 4, 3, 2, 1 } };
        foreach (var source in cases)
        {
            Measure(source, BubbleSort);
            Measure(source, InsertionSort);
        }
        var example = new[] { 4, -1, 2, 2 };
        Console.WriteLine("Vorher: " + string.Join(", ", example));
        BubbleSort(example);
        Console.WriteLine("Nachher: " + string.Join(", ", example));
        var random = new Random(42);
        foreach (int size in new[] { 1000, 5000, 10000 })
        {
            var source = Enumerable.Range(0, size).Select(_ => random.Next(-size, size)).ToArray();
            for (int run = 0; run < 3; run++)
            {
                double bubble = Measure(source, BubbleSort);
                double insertion = Measure(source, InsertionSort);
                Console.WriteLine($"N={size}, Lauf {run + 1}: Bubble {bubble:F3} ms, Insertion {insertion:F3} ms");
            }
        }
    }
}
```

</details>

## Selbst prüfen

Die kleine Ausgabe ist `-1, 2, 2, 4`. Leere Arrays und einzelne Elemente bleiben unverändert; Duplikate gehen nicht verloren. Die eingebaute Prüfung vergleicht jedes Ergebnis mit `Array.Sort`. Wiederhole den Vergleich mit sortierten und rückwärts sortierten Daten. Erkläre, warum zehn Werte keine brauchbare Grundlage für allgemeine Laufzeitvergleiche sind.

## Bonus: Weitere Sortierverfahren

**Intention:** Vergleiche zusätzliche Algorithmen und belastbarere Messauswertungen.

**Lernziel:** Du kannst Median und Streuung beschreiben und später Merge Sort oder Quick Sort mit denselben Testdaten untersuchen.

Größere Aufwärmdaten, Mittelwert/Median und Streuung, anschließend Merge Sort oder Quick Sort. Nutze in normalen Anwendungen die Bibliothekssortierung; eigene Algorithmen dienen hier dem Verständnis.

## Passende Lernquellen

[Leseempfehlung für diesen Lernschritt](../Referenzen/Lernquellen.md#stufe-5-daten-und-abfragen). Wähle den dort genannten Abschnitt zur aktuellen Aufgabe und probiere ihn in deinem eigenen Programm aus.
