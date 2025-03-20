# Aufgabe A04: Subtraktion

## Ziel

Erstellen Sie ein C#-Programm, das zwei Zahlen vom Benutzer einliest, die Differenz berechnet und das Ergebnis auf der Konsole ausgibt. Diese Aufgabe dient dazu, den Umgang mit der Subtraktionsoperation in C# zu üben.

## Anleitung

1. **Neues Projekt erstellen:**
   - Starten Sie Visual Studio.
   - Wählen Sie "Neues Projekt erstellen" aus.
   - Wählen Sie unter den verfügbaren Projekttypen "Konsolenanwendung" aus.
   - Geben Sie dem Projekt einen aussagekräftigen Namen, z. B. "Subtraktion".

2. **Programmcode schreiben:**
   - Ersetzen Sie den automatisch generierten Code durch folgenden Inhalt:

     ```csharp
     using System;

     namespace Subtraktion
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

                 // Berechnung der Differenz
                 double differenz = zahl1 - zahl2;

                 // Ausgabe des Ergebnisses
                 Console.WriteLine($"Die Differenz zwischen {zahl1} und {zahl2} ist {differenz}.");
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

- Erweitern Sie das Programm, um die Reihenfolge der Zahlen zu berücksichtigen und negative Ergebnisse entsprechend zu behandeln.
