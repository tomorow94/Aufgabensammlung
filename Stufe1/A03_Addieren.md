# Aufgabe A03: Addieren

## Ziel

Erstellen Sie ein C#-Programm, das zwei Zahlen vom Benutzer einliest, ihre Summe berechnet und das Ergebnis auf der Konsole ausgibt. Diese Aufgabe dient dazu, den Umgang mit numerischen Datentypen und grundlegenden mathematischen Operationen in C# zu üben.

## Anleitung

1. **Neues Projekt erstellen:**
   - Starten Sie Visual Studio.
   - Wählen Sie "Neues Projekt erstellen" aus.
   - Wählen Sie unter den verfügbaren Projekttypen "Konsolenanwendung" aus.
   - Geben Sie dem Projekt einen aussagekräftigen Namen, z. B. "Addition".

2. **Programmcode schreiben:**
   - Ersetzen Sie den automatisch generierten Code durch folgenden Inhalt:

     ```csharp
     using System;

     namespace Addition
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

                 // Berechnung der Summe
                 double summe = zahl1 + zahl2;

                 // Ausgabe des Ergebnisses
                 Console.WriteLine($"Die Summe von {zahl1} und {zahl2} ist {summe}.");
             }
         }
     }
     ```

3. **Programm ausführen:**
   - Speichern Sie alle Änderungen.
   - Drücken Sie die Taste `F5` oder klicken Sie auf "Starten", um das Programm auszuführen.
   - Geben Sie zwei Zahlen ein und überprüfen Sie, ob die korrekte Summe angezeigt wird.

## Hinweise

- **Datentypen:** Verwenden Sie `double` für die Zahlen, um auch Dezimalzahlen verarbeiten zu können.
- **Eingabevalidierung:** Implementieren Sie eine Fehlerbehandlung, um ungültige Eingaben abzufangen.

## Weiterführende Aufgaben

- Erweitern Sie das Programm, sodass es mehrere Zahlen addieren kann.
- Implementieren Sie eine Schleife, die den Benutzer wiederholt Zahlen eingeben lässt, bis er das Programm beendet.
