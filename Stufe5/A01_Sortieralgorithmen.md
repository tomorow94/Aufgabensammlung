# Aufgabe A01: Sortieralgorithmen – Bubble Sort, Insertion Sort & Co.

## Ziel

In dieser Aufgabe implementieren Sie verschiedene **Sortieralgorithmen** in C#.  
Dabei lernen Sie:
- **Grundprinzipien des Sortierens** in der Informatik.
- **Vergleichende Analyse der Laufzeiten** durch Zeitmessung.
- **Unterschiede zwischen einfachen und effizienteren Sortiermethoden**.

---

## Anforderungen

1. **Sortieralgorithmen implementieren**
   - **Bubble Sort**: Einfaches, aber ineffizientes Sortierverfahren mit paarweisem Tausch.
   - **Insertion Sort**: Einfügesortierung mit schrittweisem Einfügen an der richtigen Position.
   - **Optional:** Implementieren Sie **Selection Sort, Merge Sort oder Quick Sort** für einen erweiterten Vergleich.

2. **Vergleich der Laufzeiten**
   - Nutzen Sie `Stopwatch` aus `System.Diagnostics`, um die **Laufzeit der Algorithmen zu messen**.
   - Testen Sie die Algorithmen mit zufällig generierten Zahlenarrays.

3. **Benutzermenü zur Auswahl der Sortiermethode**
   - Der Benutzer kann eine **Sortiermethode auswählen**.
   - Das unsortierte und sortierte Array wird ausgegeben.
   - Die **Laufzeit des Algorithmus** wird angezeigt.

---

## Hinweise

- Nutzen Sie **Arrays oder `List<int>`** zur Speicherung der Zahlen.
- Verwenden Sie **Methoden**, um die Algorithmen modular zu halten.
- Beachten Sie die **Unterschiede in der Laufzeit**, besonders bei großen Datenmengen.

---

## Erweiterungsmöglichkeiten

- **Visualisierung:** Nutzen Sie eine grafische Darstellung (z. B. mit `Windows Forms` oder `WPF`).
- **Optimierte Sortierverfahren:** Implementieren Sie `Merge Sort` oder `Quick Sort`, um den Unterschied zu sehen.
- **Sortierung von Objekten:** Lassen Sie den Benutzer eine **Liste von Namen oder Objekten** sortieren.

---

<details>
<summary><strong>Lösungsvorschlag anzeigen</strong></summary>

```csharp
using System;
using System.Diagnostics;

class SortingAlgorithms
{
    static void BubbleSort(int[] array)
    {
        int n = array.Length;
        bool swapped;
        do
        {
            swapped = false;
            for (int i = 0; i < n - 1; i++)
            {
                if (array[i] > array[i + 1])
                {
                    (array[i], array[i + 1]) = (array[i + 1], array[i]);
                    swapped = true;
                }
            }
        } while (swapped);
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

    static void PrintArray(int[] array)
    {
        Console.WriteLine(string.Join(", ", array));
    }

    static void Main()
    {
        Random rand = new Random();
        int[] numbers = new int[10];
        for (int i = 0; i < numbers.Length; i++)
            numbers[i] = rand.Next(1, 100);

        Console.WriteLine("Original Array:");
        PrintArray(numbers);

        Console.WriteLine("\nChoose sorting algorithm:");
        Console.WriteLine("1. Bubble Sort");
        Console.WriteLine("2. Insertion Sort");
        Console.Write("Selection: ");
        string choice = Console.ReadLine();

        Stopwatch stopwatch = Stopwatch.StartNew();

        int[] sortedArray = (int[])numbers.Clone();

        switch (choice)
        {
            case "1":
                BubbleSort(sortedArray);
                break;
            case "2":
                InsertionSort(sortedArray);
                break;
            default:
                Console.WriteLine("Invalid choice.");
                return;
        }

        stopwatch.Stop();

        Console.WriteLine("\nSorted Array:");
        PrintArray(sortedArray);
        Console.WriteLine($"Sorting Time: {stopwatch.ElapsedMilliseconds} ms");
    }
}

```
</details>
