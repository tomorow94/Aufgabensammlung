# Aufgabe A02: Primzahlenprüfung

## Ziel

Entwickeln Sie ein C#-Programm, das eine vom Benutzer eingegebene Zahl daraufhin überprüft, ob sie eine Primzahl ist. Diese Aufgabe dient dazu, den Umgang mit Schleifen, bedingten Anweisungen und mathematischen Operationen in C# zu üben.

## Anleitung

1. **Neues Projekt erstellen:**
   - Starten Sie Visual Studio.
   - Wählen Sie "Neues Projekt erstellen" aus.
   - Wählen Sie den Projekttyp "Konsolenanwendung" aus.
   - Geben Sie dem Projekt einen aussagekräftigen Namen, z. B. "PrimzahlenPruefung".

2. **Programmstruktur:**
   - Das Programm sollte den Benutzer auffordern, eine positive ganze Zahl einzugeben.
   - Anschließend prüft das Programm, ob die eingegebene Zahl eine Primzahl ist.
   - Das Ergebnis der Prüfung wird dem Benutzer angezeigt.

3. **Definition einer Primzahl:**
   - Eine Primzahl ist eine natürliche Zahl größer als 1, die nur durch 1 und sich selbst ohne Rest teilbar ist.

4. **Vorgehensweise zur Primzahlprüfung:**
   - Behandeln Sie Sonderfälle: Zahlen kleiner oder gleich 1 sind keine Primzahlen.
   - Überprüfen Sie, ob die Zahl durch eine der Zahlen von 2 bis zur Quadratwurzel der Zahl ohne Rest teilbar ist.
   - Wenn ja, ist die Zahl keine Primzahl; andernfalls ist sie eine Primzahl.

5. **Hinweise zur Implementierung:**
   - Verwenden Sie eine Schleife, um mögliche Teiler zu überprüfen.
   - Nutzen Sie die `Math.Sqrt`-Funktion, um die Quadratwurzel der Zahl zu berechnen.
   - Implementieren Sie eine geeignete Fehlerbehandlung für ungültige Eingaben.

## Hinweise

- **Effizienz:** Durch die Prüfung möglicher Teiler bis zur Quadratwurzel der Zahl reduzieren Sie die Anzahl der notwendigen Berechnungen und erhöhen die Effizienz des Programms.

- **Fehlerbehandlung:** Stellen Sie sicher, dass das Programm ungültige Eingaben erkennt und den Benutzer entsprechend informiert. Verwenden Sie hierfür die `int.TryParse`-Methode, um Eingaben zu validieren.

## Weiterführende Aufgaben

- **Erweiterung zur Primzahlliste:** Passen Sie das Programm so an, dass es alle Primzahlen bis zu einer vom Benutzer eingegebenen Zahl findet und ausgibt.

- **Optimierung:** Implementieren Sie den "Sieb des Eratosthenes"-Algorithmus, um die Effizienz bei der Suche nach Primzahlen in einem größeren Bereich zu erhöhen.

- **Benutzeroberfläche:** Entwickeln Sie eine einfache grafische Benutzeroberfläche (GUI) für das Programm, um die Benutzerinteraktion zu verbessern.

<details>
<summary><strong>Lösungsvorschlag anzeigen</strong></summary>

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
