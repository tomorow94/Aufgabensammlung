# 🟢 Aufgabe A09: Zahlenpyramide und Fibonacci

## Ziel der Aufgabe

In dieser Aufgabe programmierst du ein kleines Tool, das **Fibonacci-Zahlen berechnet** und diese in einer **symmetrischen Pyramide auf der Konsole** darstellt.
Dabei lernst du, wie man mit **Listen**, **Schleifen** und **Formatierung** arbeitet.

---

## Was du lernst

- Wie man mit einer `List<int>` arbeitet
- Wie man eine Schleife zur Berechnung einer Zahlenfolge nutzt
- Wie man mit Zeichen (`' '`) die Ausgabe optisch aufbereitet
- Wie man Methoden zur besseren Strukturierung des Codes verwendet

---

## Schritt-für-Schritt-Anleitung

### 🔧 1. Projekt erstellen

1. Starte Visual Studio.
2. Neues Projekt: **Konsolenanwendung (C#)**.
3. Projektname: z. B. `FibonacciPyramide`

---

### 💻 2. Code eingeben

```csharp
using System;
using System.Collections.Generic;

class Program
{
    static void Main(string[] args)
    {
        Console.Write("Wie viele Fibonacci-Zahlen sollen angezeigt werden? ");
        if (int.TryParse(Console.ReadLine(), out int anzahl) && anzahl > 0)
        {
            List<int> fibonacciZahlen = BerechneFibonacci(anzahl);
            GibSymmetrischePyramideAus(fibonacciZahlen);
        }
        else
        {
            Console.WriteLine("Bitte gib eine gültige positive ganze Zahl ein.");
        }
    }

    static List<int> BerechneFibonacci(int n)
    {
        List<int> liste = new List<int> { 0, 1 };
        for (int i = 2; i < n; i++)
        {
            int neueZahl = liste[i - 1] + liste[i - 2];
            liste.Add(neueZahl);
        }
        return liste;
    }

    static void GibSymmetrischePyramideAus(List<int> zahlen)
    {
        int max = zahlen.Count;
        for (int i = 0; i < max; i++)
        {
            Console.Write(new string(' ', (max - i) * 2));
            // Aufsteigend
            for (int j = 0; j <= i; j++)
            {
                Console.Write(zahlen[j] + " ");
            }
            // Absteigend (ohne Verdopplung des letzten Werts)
            for (int j = i - 1; j >= 0; j--)
            {
                Console.Write(zahlen[j] + " ");
            }
            Console.WriteLine();
        }
    }
}
```

---

### ▶️ 3. Ausführen

- Starte das Programm mit `F5`.
- Gib eine Zahl wie `5` ein.
- Du solltest eine **symmetrische Pyramide** mit Fibonacci-Zahlen sehen.

**Beispielausgabe bei Eingabe von 5:**

```
                0 
              0 1 0 
            0 1 1 1 0 
          0 1 1 2 1 1 0 
        0 1 1 2 3 2 1 1 0 
```

---

## 🔍 Erklärt

| Konzept           | Beschreibung |
|-------------------|--------------|
| `List<int>`       | Eine dynamisch wachsende Liste von Zahlen |
| `for`-Schleife     | Wird verwendet, um Fibonacci-Zahlen zu berechnen und auszugeben |
| `string(' ', n)`  | Gibt eine bestimmte Anzahl an Leerzeichen zur Zentrierung aus |
| Methoden          | `BerechneFibonacci()` und `GibSymmetrischePyramideAus()` strukturieren den Code besser |

---

## 💡 Probiere selbst:

- Stelle sicher, dass das Programm auch bei großen Zahlen nicht unleserlich wird.
- Füge einen **Modus** hinzu, in dem die Pyramide **rückwärts** aufgebaut wird.
- Versuche die Fibonacci-Berechnung **rekursiv** umzusetzen.

**Was bedeutet rekursiv?**
Eine rekursive Methode ruft sich selbst auf, um ein Problem schrittweise zu lösen. Dabei wird das Problem in kleinere Teilprobleme zerlegt, bis eine sogenannte **Abbruchbedingung** erreicht ist.

Ein Beispiel:
Stell dir vor, du möchtest wissen, wie viele Stufen eine Treppe hat, indem du immer die nächste Stufe erklimmst und bei jeder Stufe nochmal dieselbe Frage stellst – bis keine Stufe mehr da ist. Genau das macht ein rekursiver Aufruf – er "fragt sich selbst", bis die Lösung offensichtlich ist.



---

<details>
<summary>💬 Lösungsvorschlag - Rekursion</summary>

```csharp
int Fibonacci(int n)
{
    if (n <= 1)
        return n;
    return Fibonacci(n - 1) + Fibonacci(n - 2);
}
```
Dies ist eine typische rekursive Funktion. Sie löst das Problem durch wiederholte Aufrufe von sich selbst – jeweils mit kleineren Eingaben – bis `n` gleich 1 oder 0 ist. 

Zum besseren Verständnis kannst du ein **Debugging-Tool** oder **Haltepunkte** in Visual Studio verwenden, um nachzuvollziehen, wie sich die rekursiven Aufrufe im Ablauf stapeln und wieder zurückkehren.

</details>

---

> 🚀 Diese Aufgabe verbindet mathematische Logik, Ausgabeformatierung und Listenverarbeitung in einer schönen kleinen Programmidee!

