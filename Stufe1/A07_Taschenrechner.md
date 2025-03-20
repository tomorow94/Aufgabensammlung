# Aufgabe A07: Taschenrechner

## Ziel

Erstellen Sie ein C#-Programm, das als einfacher Taschenrechner fungiert. Der Benutzer soll zwei Zahlen und eine Rechenoperation (+, -, *, /) eingeben können. Das Programm führt die entsprechende Berechnung durch und gibt das Ergebnis auf der Konsole aus. Diese Aufgabe dient dazu, den Umgang mit Benutzereingaben, Kontrollstrukturen und grundlegenden mathematischen Operationen in C# zu vertiefen.

## Anleitung

1. **Neues Projekt erstellen:**
   - Starten Sie Visual Studio.
   - Wählen Sie "Neues Projekt erstellen" aus.
   - Wählen Sie unter den verfügbaren Projekttypen "Konsolenanwendung" aus.
   - Geben Sie dem Projekt einen aussagekräftigen Namen, z. B. "Taschenrechner".

2. **Programmcode schreiben:**
   - Ersetzen Sie den automatisch generierten Code durch folgenden Inhalt:

     ```csharp
     using System;

     namespace Taschenrechner
     {
         class Program
         {
             static void Main(string[] args)
             {
                 bool weiterRechnen = true;

                 while (weiterRechnen)
                 {
                     try
                     {
                         // Eingabe der ersten Zahl
                         Console.Write("Bitte geben Sie die erste Zahl ein: ");
                         double zahl1 = Convert.ToDouble(Console.ReadLine());

                         // Eingabe der zweiten Zahl
                         Console.Write("Bitte geben Sie die zweite Zahl ein: ");
                         double zahl2 = Convert.ToDouble(Console.ReadLine());

                         // Auswahl der Rechenoperation
                         Console.WriteLine("Wählen Sie eine Rechenoperation:");
                         Console.WriteLine("\t+ : Addition");
                         Console.WriteLine("\t- : Subtraktion");
                         Console.WriteLine("\t* : Multiplikation");
                         Console.WriteLine("\t/ : Division");
                         Console.Write("Ihre Auswahl: ");
                         string operation = Console.ReadLine();

                         double ergebnis = 0;

                         // Ausführung der gewählten Rechenoperation
                         switch (operation)
                         {
                             case "+":
                                 ergebnis = zahl1 + zahl2;
                                 Console.WriteLine($"Ergebnis: {zahl1} + {zahl2} = {ergebnis}");
                                 break;
                             case "-":
                                 ergebnis = zahl1 - zahl2;
                                 Console.WriteLine($"Ergebnis: {zahl1} - {zahl2} = {ergebnis}");
                                 break;
                             case "*":
                                 ergebnis = zahl1 * zahl2;
                                 Console.WriteLine($"Ergebnis: {zahl1} * {zahl2} = {ergebnis}");
                                 break;
                             case "/":
                                 if (zahl2 != 0)
                                 {
                                     ergebnis = zahl1 / zahl2;
                                     Console.WriteLine($"Ergebnis: {zahl1} / {zahl2} = {ergebnis}");
                                 }
                                 else
                                 {
                                     Console.WriteLine("Fehler: Division durch Null ist nicht erlaubt.");
                                 }
                                 break;
                             default:
                                 Console.WriteLine("Ungültige Operation. Bitte wählen Sie +, -, * oder /.");
                                 break;
                         }
                     }
                     catch (FormatException)
                     {
                         Console.WriteLine("Fehler: Bitte geben Sie eine gültige Zahl ein.");
                     }

                     // Abfrage, ob der Benutzer eine weitere Berechnung durchführen möchte
                     Console.Write("Möchten Sie eine weitere Berechnung durchführen? (j/n): ");
                     string weiter = Console.ReadLine();
                     if (weiter.ToLower() != "j")
                     {
                         weiterRechnen = false;
                     }
                 }
             }
         }
     }
     ```

3. **Programm ausführen:**
   - Speichern Sie alle Änderungen.
   - Drücken Sie die Taste `F5` oder klicken Sie auf "Starten", um das Programm auszuführen.
   - Folgen Sie den Anweisungen im Konsolenfenster, um Berechnungen durchzuführen.

## Hinweise

- **Fehlerbehandlung:** Das Programm verwendet `try-catch`, um ungültige Eingaben abzufangen und entsprechende Fehlermeldungen auszugeben.
- **Schleifen:** Eine `while`-Schleife ermöglicht es dem Benutzer, mehrere Berechnungen hintereinander durchzuführen, bis er das Programm beendet.
- **Eingabevalidierung:** Das Programm überprüft die Eingaben auf Gültigkeit und behandelt spezielle Fälle, wie z. B. die Division durch Null.

## Weiterführende Aufgaben

- **Erweiterung der Funktionen:** Fügen Sie weitere mathematische Operationen hinzu, wie z. B. Potenzierung oder Wurzelberechnung.
- **Modulare Struktur:** Lagern Sie die Berechnungslogik in separate Methoden aus, um den Code übersichtlicher zu gestalten.
- **Grafische Benutzeroberfläche:** Entwickeln Sie eine einfache grafische Benutzeroberfläche für den Taschenrechner mithilfe von Windows Forms oder WPF.
