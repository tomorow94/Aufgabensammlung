# 🔵 Aufgabe A05: Datenstrukturen – List, HashSet, Dictionary

## Ziel der Aufgabe

Erstelle ein Programm, das die Unterschiede zwischen den drei wichtigsten C#-Datenstrukturen **`List<T>`**, **`HashSet<T>`** und **`Dictionary<TKey, TValue>`** erfahrbar macht.

Du lernst dabei:

* Wie man diese Datenstrukturen **erstellt**, **nutzt** und **vergleicht**
* Welche Struktur sich **wofür eignet** (z. B. schneller Zugriff vs. Reihenfolge)
* Wie man mit **großen Datenmengen performant arbeitet**

Diese Aufgabe erfordert, dass du den Code **selbst entwickelst**. Nutze bei Bedarf gezielte Internetrecherche.

---

## Einführung in die Datenstrukturen

### **1. List<T>**

* Eine `List<T>` ist eine dynamische Liste, die ähnlich wie ein Array funktioniert, aber automatisch in der Größe wächst.
* Elemente sind geordnet und können über einen Index angesprochen werden.
* Das Suchen eines Elements (`Contains`) hat eine **lineare Laufzeit O(n)**, wenn kein sortierter Zugriff oder `BinarySearch` genutzt wird.
* Eignet sich gut für **kleinere Mengen von Daten**, bei denen Reihenfolge und Duplikate wichtig sind.

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

**Beispiel:**

```csharp
HashSet<int> zahlenSet = new HashSet<int> { 1, 2, 3, 4, 5 };
zahlenSet.Add(6);
Console.WriteLine(zahlenSet.Contains(3)); // True
```

### **3. Dictionary\<TKey, TValue>**

Ein `Dictionary<TKey, TValue>` ist eine Sammlung von Schlüssel-Wert-Paaren, bei denen jeder Schlüssel eindeutig ist.
Der Zugriff auf Werte geschieht über den Schlüssel und hat in der Regel eine Laufzeit von O(1).
Nützlich für schnelle Zuordnungen, wie z. B. das Speichern von Namen und Telefonnummern.

**Beispiel:**

```csharp
Dictionary<string, int> alterVonPersonen = new Dictionary<string, int>
{
    { "Alice", 25 },
    { "Bob", 30 }
};
Console.WriteLine(alterVonPersonen["Alice"]); // 25
```

---

## Was du lernst

* Unterschiede zwischen `List`, `HashSet` und `Dictionary`
* Performance-Vergleich bei der **Suche mit `Contains()`**
* Verwendung von `Stopwatch` zur Zeitmessung
* Strukturierter Code mit Methoden und Vergleichsausgaben
* Erzeugen von Zufallszahlen mit `Random`

---

## Vorgehen & Tipps

### 1. Grundlagen ausprobieren

Erstelle in deinem Programm:

* Eine `List<int>` mit einigen Zahlen
* Ein `HashSet<int>` mit denselben Zahlen
* Ein `Dictionary<string, string>` mit z. B. Stadt → Land

Teste jeweils:

```csharp
Console.WriteLine(liste.Contains(3));
Console.WriteLine(set.Contains(3));
Console.WriteLine(woerterbuch["Berlin"]);
```

---

### 2. Performance-Vergleich: List vs. HashSet

Erzeuge 1 Million zufällige Zahlen in **List** und **HashSet**. Wähle eine davon aus der Mitte und miss die Zeit für `Contains()` mit der `Stopwatch`-Klasse:

<details>
<summary>💡 Zufallszahlen erzeugen</summary>
Nutze `Random`, um Zufallszahlen zu generieren – z. B. für spätere Tests mit großen Datenmengen:

```csharp
Random zufall = new Random();
int zahl = zufall.Next(1, 100); // Zahl zwischen 1 und 99
```
</details>

```csharp
Stopwatch sw = Stopwatch.StartNew();
list.Contains(suchzahl);
sw.Stop();
Console.WriteLine($"List: {sw.ElapsedMilliseconds} ms");
```

Vergleiche die Werte mit `HashSet.Contains()`.

💡 `HashSet<T>` ist bei großen Datenmengen deutlich schneller als `List<T>` beim Suchen.

🤔 **Extra-Tipp (nicht überspringen!)**: Schau dir ruhig mal `list.Count` und `set.Count` an, nachdem du viele Zufallszahlen eingefügt hast. Hast du erwartet, dass beide gleich viele Einträge enthalten?

```csharp
Console.WriteLine(list.Count);
Console.WriteLine(set.Count);
```

Teste das ruhig mehrmals.

<details>
<summary>💡 Warum hat das HashSet oft weniger Einträge?</summary>
Weil ein `HashSet` keine doppelten Werte erlaubt! Wenn du z. B. denselben zufälligen Wert mehrmals erzeugst, wird er in der `List` mehrfach eingefügt – im `HashSet` jedoch **nur einmal gespeichert**. So entsteht automatisch eine Art Duplikat-Filter.
</details>

---

### 3. Dictionary mit Benutzereingabe

Erstelle ein `Dictionary<string, string>` mit Städten und Ländern. Frage den Benutzer nach einer Stadt und gib das passende Land aus:

```csharp
Console.Write("Gib eine Stadt ein: ");
string stadt = Console.ReadLine();
if (map.ContainsKey(stadt))
{
    Console.WriteLine($"{stadt} liegt in {map[stadt]}.");
}
else
{
    Console.WriteLine("Stadt nicht gefunden.");
}
```

---

## Weiterführende Ideen

* Führe die Zeitmessung mehrfach durch und berechne Mittelwerte
* Führe `Add`, `Remove`, `Count` und `Clear` mit jeder Datenstruktur durch
* Sortiere eine Liste und nutze `BinarySearch`
* Füge eine Auswertung hinzu, wie oft jeder Wert gesucht wurde (mit Dictionary)
* Visualisiere die Unterschiede z. B. durch Balkendiagramme (später in GUI-Aufgaben)

---

<details>
<summary><strong>Beispielhafte Lösung anzeigen</strong></summary>

```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;

class Program
{
    static void Main()
    {
        // 1. Strukturen testen
        List<int> zahlenListe = new List<int> { 1, 2, 3, 4, 5 };
        HashSet<int> zahlenSet = new HashSet<int> { 1, 2, 3, 4, 5 };
        Dictionary<string, string> stadtLand = new Dictionary<string, string>
        {
            { "Berlin", "Deutschland" },
            { "Paris", "Frankreich" },
            { "Madrid", "Spanien" }
        };

        Console.WriteLine(zahlenListe.Contains(3));
        Console.WriteLine(zahlenSet.Contains(3));
        Console.WriteLine(stadtLand["Berlin"]);

        // 2. Performance-Test
        List<int> listTest = new List<int>();
        HashSet<int> setTest = new HashSet<int>();
        Random rand = new Random();

        for (int i = 0; i < 1000000; i++)
        {
            int num = rand.Next(1, 2000000);
            listTest.Add(num);
            setTest.Add(num);
        }

        Console.WriteLine($"List Count: {listTest.Count}");
        Console.WriteLine($"HashSet Count: {setTest.Count}");

        int testZahl = listTest[500000];

        Stopwatch sw = Stopwatch.StartNew();
        listTest.Contains(testZahl);
        sw.Stop();
        Console.WriteLine($"List: {sw.ElapsedMilliseconds} ms");

        sw.Restart();
        setTest.Contains(testZahl);
        sw.Stop();
        Console.WriteLine($"HashSet: {sw.ElapsedMilliseconds} ms");

        // 3. Dictionary-Suche
        Console.Write("Gib eine Stadt ein: ");
        string eingabe = Console.ReadLine();
        if (stadtLand.ContainsKey(eingabe))
        {
            Console.WriteLine($"{eingabe} liegt in {stadtLand[eingabe]}.");
        }
        else
        {
            Console.WriteLine("Nicht gefunden.");
        }
    }
}
```

</details>
