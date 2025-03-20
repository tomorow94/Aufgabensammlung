# Aufgabe A09: Zahlenpyramide und Fibonacci

## Ziel

Erstellen Sie ein C#-Programm, das die Fibonacci-Zahlen bis zu einer vom Benutzer angegebenen Anzahl berechnet und diese in Form einer Pyramide auf der Konsole ausgibt. Diese Aufgabe dient dazu, den Umgang mit Schleifen, Listen und der Fibonacci-Folge in C# zu üben.

## Anleitung

1. **Neues Projekt erstellen:**
   - Starten Sie Visual Studio.
   - Wählen Sie "Neues Projekt erstellen" aus.
   - Wählen Sie unter den verfügbaren Projekttypen "Konsolenanwendung" aus.
   - Geben Sie dem Projekt einen aussagekräftigen Namen, z. B. "FibonacciPyramide".

2. **Programmcode schreiben:**
   - Ersetzen Sie den automatisch generierten Code durch folgenden Inhalt:

     ```csharp
     using System;
     using System.Collections.Generic;

     namespace FibonacciPyramide
     {
         class Program
         {
             static void Main(string[] args)
             {
                 // Aufforderung zur Eingabe der Anzahl der Fibonacci-Zahlen
                 Console.Write("Bitte geben Sie die Anzahl der Fibonacci-Zahlen ein: ");
                 if (int.TryParse(Console.ReadLine(), out int anzahl) && anzahl > 0)
                 {
                     // Berechnung der Fibonacci-Zahlen
                     List<int> fibonacciZahlen = BerechneFibonacci(anzahl);

                     // Ausgabe der Fibonacci-Zahlen in Pyramidenform
                     AusgabePyramide(fibonacciZahlen);
                 }
                 else
                 {
                     Console.WriteLine("Bitte geben Sie eine gültige positive ganze Zahl ein.");
                 }
             }

             static List<int> BerechneFibonacci(int anzahl)
             {
                 List<int> fibonacciZahlen = new List<int> { 0, 1 };
                 for (int i = 2; i < anzahl; i++)
                 {
                     int naechsteZahl = fibonacciZahlen[i - 1] + fibonacciZahlen[i - 2];
                     fibonacciZahlen.Add(naechsteZahl);
                 }
                 return fibonacciZahlen;
             }

             static void AusgabePyramide(List<int> zahlen)
             {
                 int maxBreite = zahlen.Count;
                 for (int i = 0; i < zahlen.Count; i++)
                 {
                     // Berechnung der Leerzeichen für die Zentrierung
                     int leerzeichen = (maxBreite - i) * 2;
                     Console.Write(new string(' ', leerzeichen));
                     for (int j = 0; j <= i; j++)
                     {
                         Console.Write($"{zahlen[j]} ");
                     }
                     Console.WriteLine();
                 }
             }
         }
     }
     ```

3. **Programm ausführen:**
   - Speichern Sie alle Änderungen.
   - Drücken Sie die Taste `F5` oder klicken Sie auf "Starten", um das Programm auszuführen.
   - Geben Sie die Anzahl der gewünschten Fibonacci-Zahlen ein und beobachten Sie die Ausgabe in Pyramidenform.

## Hinweise

- **Listen:** Verwenden Sie die `List<int>`-Klasse, um die Fibonacci-Zahlen dynamisch zu speichern.
- **Schleifen:** Nutzen Sie `for`-Schleifen für die Berechnung und Ausgabe der Zahlen.
- **Formatierung:** Achten Sie darauf, die Pyramide korrekt zu formatieren, sodass sie zentriert und lesbar ist.

## Weiterführende Aufgaben

- Passen Sie das Programm so an, dass die Pyramide auch für größere Zahlenmengen übersichtlich bleibt.
- Implementieren Sie eine Funktion, die die Fibonacci-Zahlen rekursiv berechnet.
- Fügen Sie eine Möglichkeit hinzu, die Pyramide entweder aufsteigend oder absteigend darzustellen.
