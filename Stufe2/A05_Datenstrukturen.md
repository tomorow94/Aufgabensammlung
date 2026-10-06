# 🔵 Aufgabe A05: List, HashSet und Dictionary

## Einordnung und Lernziele

**Status:** Pflicht im Lernfaden.

**Voraussetzungen:** [Stoppuhr](A04_Stoppuhr.md)

**Intention:** Sammlungen anhand ihrer Eigenschaften passend auswählen.

**Lernziele:**

- Du kannst Reihenfolge, Duplikate und Schlüsselzugriff an List, HashSet und Dictionary zeigen.
- Du kannst Laufzeiten mit gleichen Daten vergleichen und Messgrenzen benennen.

**Weiter im Pflichtpfad:** [Menüführung mit Klassen & Struktur](../Stufe3/A01_KlassenUndStruktur.md)

## Ziel und Voraussetzungen

Nach Methoden und Stoppuhr vergleichst du Sammlungen. Beginne mit wenigen Einträgen; führe erst anschließend Messungen durch.

| Struktur | Eigenschaften | Typischer Einsatz |
|---|---|---|
| `List<T>` | Reihenfolge, Index, Duplikate | geordnete Folge |
| `HashSet<T>` | eindeutige Werte, keine zugesicherte Sortierung | Zugehörigkeit, Duplikate entfernen |
| `Dictionary<TKey,TValue>` | eindeutige Schlüssel, zugeordnete Werte | Stadt → Land |

`List.Contains` durchsucht die Liste linear, O(n). Das gilt auch für eine sortierte Liste; `BinarySearch` ist eine andere Methode. HashSet-Suche ist bei geeigneter Hash-Verteilung durchschnittlich O(1); Kollisionen werden behandelt, sie müssen nicht vollständig fehlen. Eine Liste eignet sich auch für große Datenmengen, wenn Reihenfolge oder Indexzugriff gebraucht werden.

## Anforderungen

1. Erstelle alle drei Strukturen, füge Werte hinzu, suche und entferne Einträge.
2. Füge denselben Wert zweimal in Liste und Set ein und vergleiche `Count`.
3. Frage beim Dictionary eine Stadt ab und nutze `TryGetValue`; ein fehlender Schlüssel soll keinen Absturz verursachen.
4. Schreibe Hilfsmethoden und vergleiche anschließend viele Suchanfragen für dieselben Werte.

## Messung vorbereiten

Eine einzelne Suche mit `ElapsedMilliseconds` ergibt oft `0 ms`. Verwende identische eindeutige Ausgangswerte, Aufwärmläufe, viele Anfragen, mehrere Wiederholungen und einen Release-Build ohne Debugger. Prüfe Treffer und Nichttreffer. Die Ergebnisse müssen verwendet werden. Miss nur die Suche, nicht Aufbau oder Ausgabe. Prüfe die Streuung; ein Wert ist kein allgemeines Leistungsgesetz.

## Gestufte Hinweise

Versuche zuerst eine eigene Lösung. Öffne bei Bedarf zunächst Hinweis 1 und erst danach Hinweis 2; die vorhandenen Beispiele bzw. Referenzen dienen anschließend zum Vergleichen.

<details>
<summary>Hinweis 1: Denkanstoß</summary>

Welche Struktur soll Duplikate entfernen, welche einen Wert über einen Schlüssel finden?

</details>

<details>
<summary>Hinweis 2: Vorgehensweise</summary>

Prüfe zuerst die Ergebnisse der Operationen; miss anschließend dieselben Operationen mit reproduzierbaren Daten außerhalb der Konsolenausgabe.

</details>

<details>
<summary>Vollständiges Beispiel für Program.cs (.NET 10)</summary>

```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
class Program
{
    static void Main()
    {
        var exampleList = new List<int> { 1, 1, 2 };
        var exampleSet = new HashSet<int>(exampleList);
        Console.WriteLine($"List: {exampleList.Count}, Set: {exampleSet.Count}");
        var cities = new Dictionary<string, string>(StringComparer.OrdinalIgnoreCase)
        { ["Berlin"] = "Deutschland", ["Paris"] = "Frankreich" };
        Console.Write("Stadt: ");
        string city = Console.ReadLine()?.Trim() ?? "";
        Console.WriteLine(cities.TryGetValue(city, out string? country) ? country : "Nicht gefunden.");
        foreach (int count in new[] { 1000, 10000, 100000 })
        {
            var list = Enumerable.Range(0, count).ToList();
            var set = new HashSet<int>(list);
            int[] queries = { 0, count / 2, count - 1, -1 };
            // Beide Sammlungen enthalten dieselben Werte; -1 ist ein Nichttreffer.
            Measure("List", list.Contains, queries, 10, false);
            Measure("Set", set.Contains, queries, 10, false);
            Console.WriteLine($"N = {count}");
            for (int trial = 0; trial < 3; trial++)
            {
                Measure("List", list.Contains, queries, 1000, true);
                Measure("Set", set.Contains, queries, 1000, true);
            }
        }
    }
    static void Measure(string name, Func<int, bool> contains, int[] queries, int repeats, bool print)
    {
        int hits = 0;
        var stopwatch = Stopwatch.StartNew();
        for (int i = 0; i < repeats; i++)
            foreach (int query in queries) if (contains(query)) hits++;
        stopwatch.Stop();
        if (print) Console.WriteLine($"{name}: {stopwatch.Elapsed.TotalMilliseconds:F3} ms, Treffer: {hits}");
    }
}
```

</details>

## Selbst prüfen

Liste hat `3`, Set `2` Einträge. `berlin` wird gefunden, eine unbekannte Stadt nicht. Jeder gemessene Lauf mit 1000 Wiederholungen hat `3000` Treffer aus `4000` Anfragen. Unterschiedliche Trefferzahlen bedeuten, dass du nicht denselben Inhalt oder dieselben Abfragen verglichen hast. Wiederholte Zeiten dürfen schwanken.

## Bonus: Messungen vertiefen

**Intention:** Untersuche weitere Einflussgrößen und die Grenzen einfacher Zeitmessung.

**Lernziel:** Du kannst Duplikatraten und sortierte Daten vergleichen; BenchmarkDotNet ist eine spätere zusätzliche Werkzeugvertiefung.

Zufallszahlen mit fester Startzahl (`new Random(42)`), unterschiedliche Duplikatraten, `BinarySearch` auf sortierten Listen. Bei genauer Performanceanalyse verwende später BenchmarkDotNet; diese Übung erklärt zunächst Datenstrukturen und grundlegende Messfehler.

## Passende Lernquellen

[Leseempfehlung für diesen Lernschritt](../Referenzen/Lernquellen.md#stufe-2-methoden-und-fehlersuche). Wähle den dort genannten Abschnitt zur aktuellen Aufgabe und probiere ihn in deinem eigenen Programm aus.
