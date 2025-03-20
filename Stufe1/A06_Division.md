# Aufgabe A06: Division

## Ziel

Erstellen Sie ein C#-Programm, das zwei Zahlen vom Benutzer einliest, die Division der ersten Zahl durch die zweite berechnet und das Ergebnis auf der Konsole ausgibt. Diese Aufgabe dient dazu, den Umgang mit der Division und der Behandlung von Sonderfällen wie der Division durch Null in C# zu üben.

## Anleitung

1. **Neues Projekt erstellen:**
   - Starten Sie Visual Studio.
   - Wählen Sie "Neues Projekt erstellen" aus.
   - Wählen Sie unter den verfügbaren Projekttypen "Konsolenanwendung" aus.
   - Geben Sie dem Projekt einen aussagekräftigen Namen, z. B. "Division".

2. **Programmcode schreiben:**
   - Ersetzen Sie den automatisch generierten Code durch folgenden Inhalt:

     ```csharp
     using System;

     namespace Division
     {
         class Program
         {
             static void Main(string[] args)
             {
                 try
                 {
                     // Aufforderung zur Eingabe der ersten Zahl
                     Console.Write("Bitte geben Sie die erste Zahl ein: ");
                     double zahl1 = Convert.ToDouble(Console.ReadLine());

                     // Aufforderung zur Eingabe der zweiten Zahl
                     Console.Write("Bitte geben Sie die zweite Zahl ein: ");
                     double zahl2 = Convert.ToDouble(Console.ReadLine());

                     // Überprüfung auf Division durch Null
                     if (zahl2 == 0)
                     {
                         Console.WriteLine("Division durch Null ist nicht erlaubt.");
                     }
                     else
                     {
                         // Berechnung der Division
                         double ergebnis = zahl1 / zahl2;
                         Console.WriteLine($"Das Ergebnis der Division von {zahl1} durch {zahl2} ist {ergebnis}.");
                     }
                 }
                 catch (FormatException)
                 {
                     Console.WriteLine("Bitte geben Sie eine gültige Zahl ein.");
                 }
             }
         }
     }
     ```

3. **Programm ausführen:**
   - Speichern Sie alle Änderungen.
   - Drücken Sie die Taste `F5` oder klicken Sie auf "Starten", um das Programm auszuführen.
   - Geben Sie zwei Zahlen ein und überprüfen Sie, ob das korrekte Ergebnis oder eine entsprechende Fehlermeldung angezeigt wird.

## Hinweise

- **Fehlerbehandlung:** Verwenden Sie `try-catch`, um ungültige Eingaben abzufangen und den Benutzer darauf hinzuweisen.
- **Division durch Null:** Implementieren Sie eine Überprüfung, um eine Division durch Null zu verhindern und eine entsprechende Meldung auszugeben.

## Weiterführende Aufgaben

- Erweitern Sie das Programm, sodass es auch den Restwert der Division (Modulo) berechnet und anzeigt.
- Implementieren Sie eine Schleife, die den Benutzer so lange nach gültigen Zahlen fragt, bis eine gültige Eingabe erfolgt.
