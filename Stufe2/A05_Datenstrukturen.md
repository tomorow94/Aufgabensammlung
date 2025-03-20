# Aufgabe A05: Datenstrukturen – List, HashSet, Dictionary

## Ziel

In dieser Aufgabe lernen Sie verschiedene Datenstrukturen in C# kennen: `List<T>`, `HashSet<T>` und `Dictionary<TKey, TValue>`. Sie sollen deren Unterschiede verstehen, insbesondere hinsichtlich ihrer Performance bei der Suche und Speicherung von Werten.

## Einführung in die Datenstrukturen

### **1. List<T>**
- Eine `List<T>` ist eine dynamische Liste, die ähnlich wie ein Array funktioniert, aber automatisch in der Größe wächst.
- Elemente sind geordnet und können über einen Index angesprochen werden.
- Das Suchen eines Elements (`Contains`) hat eine **lineare Laufzeit O(n)**, wenn kein sortierter Zugriff oder `BinarySearch` genutzt wird.
- Eignet sich gut für **kleinere Mengen von Daten**, bei denen Reihenfolge und Duplikate wichtig sind.

**Beispiel:**
```csharp
List<int> zahlenListe = new List<int> { 1, 2, 3, 4, 5 };
zahlenListe.Add(6);
Console.WriteLine(zahlenListe.Contains(3)); // True
```
### **2. HashSet<T>**
Ein `HashSet<T>` speichert nur eindeutige Werte und verwendet eine Hash-Funktion, um die Suche zu beschleunigen.
Die Suche (`Contains`) hat nahezu konstante Laufzeit O(1), sofern keine Hash-Kollisionen auftreten.
Es ist sehr effizient für große Mengen von Daten, bei denen die Reihenfolge unwichtig ist.
Beispiel:

```csharp
HashSet<int> zahlenSet = new HashSet<int> { 1, 2, 3, 4, 5 };
zahlenSet.Add(6);
Console.WriteLine(zahlenSet.Contains(3)); // True
```

### **3. Dictionary<TKey, TValue>**
Ein `Dictionary<TKey, TValue>` ist eine Sammlung von Schlüssel-Wert-Paaren, bei denen jeder Schlüssel eindeutig ist.
Der Zugriff auf Werte geschieht über den Schlüssel und hat in der Regel eine Laufzeit von O(1).
Nützlich für schnelle Zuordnungen, wie z. B. das Speichern von Namen und Telefonnummern.
Beispiel:

```csharp
Dictionary<string, int> alterVonPersonen = new Dictionary<string, int>
{
    { "Alice", 25 },
    { "Bob", 30 }
};
Console.WriteLine(alterVonPersonen["Alice"]); // 25
```

## Aufgaben
### 1. Datenstrukturen ausprobieren

Erstellen Sie eine `List<int>`, ein `HashSet<int>` und ein `Dictionary<string, int>`.
Fügen Sie einige Werte hinzu und testen Sie `Contains()` für `List<T>` und `HashSet<T>` sowie das Abrufen eines Wertes für `Dictionary<TKey, TValue>`.

### 2. Performance-Vergleich: List vs. HashSet

Erstellen Sie eine `List<int>` und ein `HashSet<int>` mit 1 Million zufälligen Zahlen.
Messen Sie die Zeit für die Suche nach einer Zahl mit `Contains()` und vergleichen Sie die Laufzeiten.

### 3. Key-Value-Zuordnung mit Dictionary

Erstellen Sie ein `Dictionary<string, string>`, das Städtenamen als Schlüssel und deren Länder als Wert speichert.
Lassen Sie den Benutzer eine Stadt eingeben und geben Sie das entsprechende Land aus.

## Hinweise
Verwenden Sie `Stopwatch` aus `System.Diagnostics`, um die Zeitmessung für die Performance-Vergleiche durchzuführen.
Beachten Sie, dass `List<T>` nützlich ist, wenn eine Reihenfolge beibehalten werden soll, `HashSet<T>` für große Mengen einzigartiger Daten und `Dictionary<TKey, TValue>` für schnelle Key-Value-Zuordnungen.

<details> <summary><strong>Lösungsvorschlag anzeigen</strong></summary>

```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;

class Program
{
    static void Main()
    {
        // 1. Datenstrukturen ausprobieren
        List<int> zahlenListe = new List<int> { 1, 2, 3, 4, 5 };
        HashSet<int> zahlenSet = new HashSet<int> { 1, 2, 3, 4, 5 };
        Dictionary<string, string> stadtLand = new Dictionary<string, string>
        {
            { "Berlin", "Deutschland" },
            { "Paris", "Frankreich" }
        };

        Console.WriteLine(zahlenListe.Contains(3)); // True
        Console.WriteLine(zahlenSet.Contains(3));   // True
        Console.WriteLine(stadtLand["Berlin"]);     // Deutschland

        // 2. Performance-Vergleich: List vs. HashSet
        List<int> listTest = new List<int>();
        HashSet<int> setTest = new HashSet<int>();
        Random rand = new Random();

        for (int i = 0; i < 1000000; i++)
        {
            int num = rand.Next(1, 2000000);
            listTest.Add(num);
            setTest.Add(num);
        }

        int testZahl = listTest[500000];

        Stopwatch sw = Stopwatch.StartNew();
        bool inList = listTest.Contains(testZahl);
        sw.Stop();
        Console.WriteLine($"List: {sw.ElapsedMilliseconds} ms");

        sw.Restart();
        bool inSet = setTest.Contains(testZahl);
        sw.Stop();
        Console.WriteLine($"HashSet: {sw.ElapsedMilliseconds} ms");

        // 3. Key-Value-Zuordnung mit Dictionary
        Console.Write("Geben Sie eine Stadt ein: ");
        string stadt = Console.ReadLine();
        if (stadtLand.ContainsKey(stadt))
        {
            Console.WriteLine($"{stadt} liegt in {stadtLand[stadt]}.");
        }
        else
        {
            Console.WriteLine("Stadt nicht gefunden.");
        }
    }
}
```

</details>
