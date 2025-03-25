# 🟢 Aufgabe A07: Taschenrechner

## Ziel der Aufgabe

In dieser Aufgabe erstellst du einen einfachen **Taschenrechner**, der zwei Zahlen verarbeiten kann. Der Benutzer wählt eine Rechenoperation (+, -, *, /), und das Programm führt die Berechnung durch.

Dabei übst du den Umgang mit **Benutzereingaben**, **Kontrollstrukturen** (`switch`, `if`) und **Schleifen**.

---

## Was du lernst

- Wie man Benutzereingaben liest und interpretiert
- Wie man mit `switch` zwischen mehreren Fällen unterscheidet
- Wie man Schleifen für wiederholte Berechnungen nutzt

---

## Schritt-für-Schritt-Anleitung

### 🔧 1. Projekt erstellen

1. Starte Visual Studio.
2. Neues Projekt: **Konsolenanwendung (C#)**.
3. Projektname: z. B. `Taschenrechner`

---

### 💻 2. Code eingeben

```csharp
using System;

class Program
{
    static void Main(string[] args)
    {
        bool weiterRechnen = true;

        while (weiterRechnen)
        {
            try
            {
                Console.Write("Erste Zahl: ");
                double a = Convert.ToDouble(Console.ReadLine());

                Console.Write("Zweite Zahl: ");
                double b = Convert.ToDouble(Console.ReadLine());

                Console.WriteLine("Rechenoperation wählen (+, -, *, /): ");
                string op = Console.ReadLine();

                double ergebnis;
                switch (op)
                {
                    case "+":
                        ergebnis = a + b;
                        Console.WriteLine($"Ergebnis: {a} + {b} = {ergebnis}");
                        break;
                    case "-":
                        ergebnis = a - b;
                        Console.WriteLine($"Ergebnis: {a} - {b} = {ergebnis}");
                        break;
                    case "*":
                        ergebnis = a * b;
                        Console.WriteLine($"Ergebnis: {a} * {b} = {ergebnis}");
                        break;
                    case "/":
                        if (b == 0)
                        {
                            Console.WriteLine("Fehler: Division durch 0 nicht erlaubt.");
                        }
                        else
                        {
                            ergebnis = a / b;
                            Console.WriteLine($"Ergebnis: {a} / {b} = {ergebnis}");
                        }
                        break;
                    default:
                        Console.WriteLine("Ungültige Operation. Bitte +, -, * oder / eingeben.");
                        break;
                }
            }
            catch (FormatException)
            {
                Console.WriteLine("Ungültige Eingabe! Bitte Zahlen verwenden.");
            }

            Console.Write("Weitere Berechnung? (j/n): ");
            string eingabe = Console.ReadLine();
            if (eingabe.ToLower() != "j")
            {
                weiterRechnen = false;
            }
        }
    }
}
```

---

### ▶️ 3. Ausführen

- Starte das Programm mit `F5`.
- Teste mehrere Rechenarten hintereinander.
- Achte auf die Fehlerbehandlung bei falscher Eingabe oder Division durch 0.

---

## 🔍 Erklärt

| Konzept         | Beschreibung |
|----------------|--------------|
| `switch`       | Mit `switch` wählst du gezielt aus, welche Anweisung für eine bestimmte Eingabe ausgeführt werden soll. In diesem Fall: +, -, * oder /. Jede `case`-Anweisung übernimmt die passende Rechenart. |
| `try-catch`    | Mit `try` wird ein blockweise geschützter Bereich erstellt. Tritt ein Fehler auf (z. B. ungültige Eingabe wie Buchstaben statt Zahlen), springt das Programm direkt in den `catch`-Block und gibt eine Fehlermeldung aus, statt abzustürzen. |
| `while`        | Die `while`-Schleife läuft so lange, wie `weiterRechnen` true ist. Das bedeutet: Solange der Benutzer nach jeder Berechnung mit "j" bestätigt, wird der Rechner nicht beendet. |
| `Convert.ToDouble()` | Wandelt eine Texteingabe (string) in eine Gleitkommazahl um. Das ist nötig, da `Console.ReadLine()` standardmäßig Text liefert. |
| `ToLower()`    | Wandelt Benutzereingabe wie "J", "j", "Ja" in Kleinbuchstaben um, um einfache Vergleiche wie `== "j"` zu ermöglichen. |

---

## 💡 Probiere selbst:

- Erweitere den Rechner um **Potenz** oder **Wurzel**.
- Trenne Berechnungslogik in eine eigene Methode und verwende diese um für mehr Übersichtlichkeit im Code zu sorgen, z. B.:
  ```csharp
  static double Berechne(double a, double b, string op)
  ```
  Eine Methode ist ein Codeblock, der eine Reihe von Anweisungen enthält.
  Ein Programm bewirkt die Ausführung der Anweisungen, indem die Methode aufgerufen wird und alle erforderlichen Methodenargumente angegeben werden.  
  Beim Beispiel `Berechne()`, von oben, sind `a`, `b` und `op`, die zu übergebenden Argumente (Parameter), und das `double`, vor dem Methodennamen, `Berechne` beschreibt den Typ der Ausgabe der Methode, hier also eine Kommazahl.
- Baue ein **einfaches Textmenü** zur Auswahl der Operation.

---

<details><summary>Lösungssvorschlag - Eigene "Berechne" Methode</summary>

```csharp
using System;

class Program
{
    static void Main(string[] args)
    {
        bool weiterRechnen = true;

        while (weiterRechnen)
        {
            try
            {
                Console.Write("Erste Zahl: ");
                double a = Convert.ToDouble(Console.ReadLine());

                Console.Write("Zweite Zahl: ");
                double b = Convert.ToDouble(Console.ReadLine());

                Console.WriteLine("Rechenoperation wählen (+, -, *, /): ");
                string op = Console.ReadLine();

                // Die neue Methode "Berechne" wird benutzt um das ergebnis zu berechnen und wirft einen Fehler, wenn die Eingabe nicht verarbeitet werden kann
                double ergebnis = Berechne(a, b, op);

                Console.WriteLine($"Ergebnis: {a} {op} {b} = {ergebnis}");
            }
            catch (Exception e)
            {
                // Fehler, beim Ausführen des Codes, werden abgefangen und dem Nutzer in der Konsole angezeigt.
                if (e is FormatException fe)
                {
                    // Hier wird ein spezieller Text angezeigt, der meist auftritt, wenn statt einer Zahl beispielsweise ein Buchstabe übergeben wird.
                    Console.WriteLine("Ungültige Eingabe! Bitte Zahlen verwenden.");
                }
                else
                {
                    // Hier werden alle anderen Fehler-nachrichten ausgegeben.
                    Console.WriteLine(e.Message);
                }
            }

            Console.Write("Weitere Berechnung? (j/n): ");
            string eingabe = Console.ReadLine();
            if (eingabe.ToLower() != "j")
            {
                weiterRechnen = false;
            }
        }
    }

    static double Berechne(double a, double b, string op)
    {
        switch (op)
        {
            case "+":
                // Die Rechenoperation wird durchgeführt und das ergebnis wirdzurückgegeben.
                return a + b;
            case "-":
                return a - b;
            case "*":
                return a * b;
            case "/":
                if (b == 0)
                {
                    // Anstelle eines ergebnisses wird ein Fehler geworfen mit einer selbst geschriebenen Nachricht.
                    throw new ArgumentException("Fehler: Division durch 0 nicht erlaubt.");
                }
                else
                {
                    return a / b;
                }
            default:
                throw new ArgumentException("Ungültige Operation. Bitte +, -, * oder / eingeben.");
        }
    }
}
```

</details>

---

> 🧠 Mit dieser Aufgabe kombinierst du viele Grundelemente: Eingabe, Verzweigung, Schleifen und Fehlerbehandlung – und bekommst ein richtiges Mini-Programm!

