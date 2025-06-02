# 🔵 Aufgabe A02: Primzahlenprüfung

## Ziel der Aufgabe

Erstelle ein Programm, das überprüft, ob eine eingegebene Zahl eine **Primzahl** ist. Dabei sollst du lernen, wie man **mathematische Regeln**, **Schleifen**, **Methoden** und **Fehlermanagement** sinnvoll in einem Programm umsetzt.

Diese Aufgabe setzt voraus, dass du **selbst den Code schreibst** (kein Copy+Paste). Du kannst aber z. B. im **C#-Cheat-Sheet** nachsehen oder **online recherchieren**. Ziel ist, dein Verständnis für Programmstruktur und Logik zu vertiefen.

---

## Was du lernst

* Wie man Bedingungen und Schleifen kombiniert
* Wie man mathematische Regeln in Code übersetzt
* Wie man Methoden schreibt, die etwas zurückgeben (z. B. `bool`)
* Wie man ungültige Eingaben behandelt

---

## Vorgehen & Tipps

1. **Plane dein Programm zuerst in Stichpunkten**.

   * Du kannst deine Gedanken direkt im Code als Kommentare notieren.
   * Beispiel:

     ```csharp
     // Benutzer zur Eingabe auffordern
     // Zahl einlesen und überprüfen ob sie gültig ist
     // Methode zur Primzahlprüfung aufrufen
     // Ergebnis ausgeben
     ```

2. **So schreibt man in C# Kommentare:**

   * Einzeilig: `// dies ist ein Kommentar`
   * Mehrzeilig:

     ```csharp
     /*
        Dies ist ein
        mehrzeiliger Kommentar
     */
     ```

3. **Schreibe dann Schritt für Schritt die Teile, die du geplant hast.**

---

## Definition einer Primzahl

Eine **Primzahl** ist eine natürliche Zahl, die **nur durch 1 und sich selbst** ohne Rest teilbar ist. Beispiele: 2, 3, 5, 7, 11

* **Hinweis:** 1 ist **keine** Primzahl.
* Du musst nur bis zur **Quadratwurzel** der Zahl testen, um Teiler zu finden. Warum? Wenn eine Zahl durch etwas > Wurzel teilbar ist, dann gibt es bereits einen kleineren Teiler.

---

## Beispielstruktur deines Programms

```csharp
Console.Write("Bitte gib eine ganze Zahl > 1 ein: ");
// Eingabe einlesen und mit TryParse überprüfen
// Falls gültig, Methode zur Prüfung aufrufen
// Ausgabe: Primzahl oder nicht?
```

---

## Hinweise zur Umsetzung

* `Math.Sqrt(zahl)` liefert die Quadratwurzel einer Zahl.

* Nutze `bool` als Rückgabewert deiner Methode, z. B.:

  ```csharp
  static bool IstPrimzahl(int zahl)
  ```

* Verwende `int.TryParse`, um Benutzereingaben abzufangen.

* Verwende `for`- oder `while`-Schleifen zum Testen von Teilern.

* Nutze `continue` oder `return` sinnvoll, um Schleifen zu verlassen.

---

## Weiterführende Ideen

* Verwende **Debugging** in Visual Studio, um Schritt für Schritt zu beobachten, wie dein Programm Teiler prüft.
* Gib dem Benutzer die Möglichkeit, das Programm mehrfach zu verwenden (Schleife um `Main`).
* Erweitere das Programm so, dass alle **Primzahlen bis zu einer bestimmten Zahl** ausgegeben werden.
* Baue eine **Methode mit Sieb des Eratosthenes**, um viele Primzahlen effizient zu berechnen.
* Entwerfe und implementiere eine einfache grafische Benutzeroberfläche (GUI) für das Programm, um die Benutzerinteraktion zu verbessern.

---

> 🧠 Diese Aufgabe ist ideal, um das Zusammenspiel von Schleifen, Methoden und mathematischem Denken zu festigen. Sie ist außerdem eine gute Vorbereitung für spätere Algorithmen-Aufgaben.


---

<details>
<summary><strong>Möglichen Lösungsvorschlag anzeigen</strong></summary>

```csharp
using System;

namespace PrimzahlenPruefung
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Bitte geben Sie eine positive ganze Zahl ein: ");
            if (int.TryParse(Console.ReadLine(), out int zahl) && zahl > 0)
            {
                if (IstPrimzahl(zahl))
                {
                    Console.WriteLine($"{zahl} ist eine Primzahl.");
                }
                else
                {
                    Console.WriteLine($"{zahl} ist keine Primzahl.");
                }
            }
            else
            {
                Console.WriteLine("Ungültige Eingabe. Bitte geben Sie eine positive ganze Zahl ein.");
            }
        }

        static bool IstPrimzahl(int zahl)
        {
            if (zahl <= 1) return false;
            if (zahl == 2) return true;
            if (zahl % 2 == 0) return false;

            int grenze = (int)Math.Floor(Math.Sqrt(zahl));
            for (int i = 3; i <= grenze; i += 2)
            {
                if (zahl % i == 0)
                {
                    return false;
                }
            }
            return true;
        }
    }
}
</details>
