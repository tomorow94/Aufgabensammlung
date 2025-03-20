# Aufgabe A08: Zahlenraten

## Ziel

Entwickeln Sie ein C#-Programm, bei dem der Benutzer eine zufällig generierte Zahl zwischen 1 und 100 erraten muss. Nach jedem Rateversuch erhält der Benutzer einen Hinweis, ob die gesuchte Zahl größer oder kleiner ist als die eingegebene Zahl. Das Spiel endet, wenn die Zahl erraten wurde oder die maximale Anzahl von Versuchen erreicht ist.

## Anleitung

1. **Neues Projekt erstellen:**
   - Starten Sie Visual Studio.
   - Wählen Sie "Neues Projekt erstellen" aus.
   - Wählen Sie unter den verfügbaren Projekttypen "Konsolenanwendung" aus.
   - Geben Sie dem Projekt einen aussagekräftigen Namen, z. B. "Zahlenraten".

2. **Programmcode schreiben:**
   - Ersetzen Sie den automatisch generierten Code durch folgenden Inhalt:

     ```csharp
     using System;

     namespace Zahlenraten
     {
         class Program
         {
             static void Main(string[] args)
             {
                 // Zufallszahlengenerator initialisieren
                 Random zufall = new Random();
                 int geheimeZahl = zufall.Next(1, 101); // Zahl zwischen 1 und 100
                 int versuche = 0;
                 int maximaleVersuche = 10;
                 bool zahlErraten = false;

                 Console.WriteLine("Willkommen zum Zahlenratespiel!");
                 Console.WriteLine($"Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht. Sie haben {maximaleVersuche} Versuche, um sie zu erraten.");

                 while (versuche < maximaleVersuche && !zahlErraten)
                 {
                     Console.Write("Bitte geben Sie Ihren Tipp ein: ");
                     string eingabe = Console.ReadLine();

                     if (int.TryParse(eingabe, out int tipp))
                     {
                         versuche++;
                         if (tipp < geheimeZahl)
                         {
                             Console.WriteLine("Die gesuchte Zahl ist größer.");
                         }
                         else if (tipp > geheimeZahl)
                         {
                             Console.WriteLine("Die gesuchte Zahl ist kleiner.");
                         }
                         else
                         {
                             zahlErraten = true;
                             Console.WriteLine($"Herzlichen Glückwunsch! Sie haben die Zahl {geheimeZahl} in {versuche} Versuchen erraten.");
                         }
                     }
                     else
                     {
                         Console.WriteLine("Ungültige Eingabe. Bitte geben Sie eine ganze Zahl ein.");
                     }
                 }

                 if (!zahlErraten)
                 {
                     Console.WriteLine($"Leider haben Sie die Zahl nicht erraten. Die gesuchte Zahl war {geheimeZahl}.");
                 }

                 Console.WriteLine("Danke fürs Spielen!");
             }
         }
     }
     ```

3. **Programm ausführen:**
   - Speichern Sie alle Änderungen.
   - Drücken Sie die Taste `F5` oder klicken Sie auf "Starten", um das Programm auszuführen.
   - Folgen Sie den Anweisungen im Konsolenfenster, um das Spiel zu spielen.

## Hinweise

- **Zufallszahl:** Die Klasse `Random` wird verwendet, um eine zufällige Zahl zwischen 1 und 100 zu generieren.
- **Eingabevalidierung:** Mit `int.TryParse` wird überprüft, ob die Benutzereingabe eine gültige ganze Zahl ist.
- **Schleifen und Bedingungen:** Eine `while`-Schleife ermöglicht mehrere Rateversuche, und `if`-Bedingungen geben Hinweise, ob die gesuchte Zahl größer oder kleiner ist.

## Weiterführende Aufgaben

- **Versuchszähler:** Begrenzen Sie die Anzahl der Versuche und informieren Sie den Benutzer über die verbleibenden Versuche.
- **Schwierigkeitsgrad:** Fügen Sie verschiedene Schwierigkeitsgrade hinzu, die den Zahlenbereich oder die Anzahl der Versuche beeinflussen.
- **Highscore-Liste:** Implementieren Sie eine Highscore-Liste, die die besten Spieler mit der geringsten Anzahl von Versuchen speichert.
