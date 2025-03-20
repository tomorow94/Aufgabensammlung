# Aufgabe A05: Multiplikation

## Ziel

Erstellen Sie ein C#-Programm, das zwei Zahlen vom Benutzer einliest, ihr Produkt berechnet und das Ergebnis auf der Konsole ausgibt. Diese Aufgabe dient dazu, den Umgang mit der Multiplikationsoperation in C# zu üben.

## Anleitung

1. **Neues Projekt erstellen:**
   - Starten Sie Visual Studio.
   - Wählen Sie "Neues Projekt erstellen" aus.
   - Wählen Sie unter den verfügbaren Projekttypen "Konsolenanwendung" aus.
   - Geben Sie dem Projekt einen aussagekräftigen Namen, z. B. "Multiplikation".

2. **Programmcode schreiben:**
   - Ersetzen Sie den automatisch generierten Code durch folgenden Inhalt:

     ```csharp
     using System;

     namespace Multiplikation
     {
         class Program
         {
             static void Main(string[] args)
             {
                 // Aufforderung zur Eingabe der ersten Zahl
                 Console.Write("Bitte geben Sie die erste Zahl ein: ");
                 double zahl1 = Convert.ToDouble(Console.ReadLine());

                 // Aufforderung zur Eingabe der zweiten Zahl
                 Console.Write("Bitte geben Sie die zweite Zahl ein: ");
                 double zahl2 = Convert.ToDouble(Console.ReadLine());

                 // Berechnung des Produkts
                 double produkt = zahl1 * zahl2;

                 // Ausgabe des Ergebnisses
                 Console.WriteLine($"Das Produkt von {zahl1} und {zahl2} ist {produkt}.");
             }
         }
     }
     ```

3. **Programm ausführen:**
   - Speichern Sie alle Änderungen.
   - Führen Sie das Programm aus und testen Sie es mit verschiedenen Zahlen.

## Hinweise

- **Datentypen:** Verwenden Sie `double`, um auch mit Dezimalzahlen arbeiten zu können.
- **Eingabevalidierung:** Stellen Sie sicher, dass der Benutzer gültige Zahlen eingibt.

## Weiterführende Aufgaben

- Erweitern Sie das Programm, um mehrere Zahlen nacheinander zu multiplizieren.
