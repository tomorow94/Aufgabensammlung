# Aufgabe A02: Texteingabe und -ausgabe

## Ziel

Erstellen Sie ein C#-Programm, das den Benutzer nach seinem Namen fragt und anschließend eine personalisierte Begrüßung auf der Konsole ausgibt. Diese Aufgabe dient dazu, den Umgang mit Benutzereingaben und -ausgaben in C# zu erlernen.

## Anleitung

1. **Neues Projekt erstellen:**
   - Starten Sie Visual Studio.
   - Wählen Sie "Neues Projekt erstellen" aus.
   - Wählen Sie unter den verfügbaren Projekttypen "Konsolenanwendung" aus.
   - Geben Sie dem Projekt einen aussagekräftigen Namen, z. B. "TexteingabeAusgabe".

2. **Programmcode schreiben:**
   - Ersetzen Sie den automatisch generierten Code durch folgenden Inhalt:

     ```csharp
     using System;

     namespace TexteingabeAusgabe
     {
         class Program
         {
             static void Main(string[] args)
             {
                 // Aufforderung zur Eingabe des Namens
                 Console.Write("Bitte geben Sie Ihren Namen ein: ");
                 
                 // Einlesen der Benutzereingabe und Speichern in einer Variable
                 string benutzerName = Console.ReadLine();
                 
                 // Ausgabe der personalisierten Begrüßung
                 Console.WriteLine($"Hallo, {benutzerName}!");
             }
         }
     }
     ```

     In diesem Programm wird der Benutzer aufgefordert, seinen Namen einzugeben. Die Eingabe wird mit `Console.ReadLine()` erfasst und in der Variable `benutzerName` gespeichert. Anschließend wird der Benutzer mit seinem Namen begrüßt.

3. **Programm ausführen:**
   - Speichern Sie alle Änderungen.
   - Drücken Sie die Taste `F5` oder klicken Sie auf "Starten", um das Programm auszuführen.
   - Geben Sie im Konsolenfenster Ihren Namen ein und überprüfen Sie, ob die personalisierte Begrüßung korrekt angezeigt wird.

## Hinweise

- **Eingabeaufforderung:** Die Methode `Console.Write` wird verwendet, um eine Eingabeaufforderung ohne Zeilenumbruch anzuzeigen, sodass der Benutzer seine Eingabe direkt daneben tätigen kann.
- **Zeichenketteninterpolation:** Mit `$"{variable}"` können Sie Variablen direkt in Zeichenketten einfügen, was den Code lesbarer macht.
- **Ressourcen:** Weitere Informationen zur Benutzereingabe und -ausgabe in C# finden Sie in der offiziellen Microsoft-Dokumentation: [Ein-/Ausgabe in der Konsole](https://docs.microsoft.com/de-de/dotnet/csharp/programming-guide/concepts/linq/basic-console-i-o).

## Weiterführende Aufgaben

- Erweitern Sie das Programm, sodass es den Benutzer nach seinem Alter fragt und dieses ebenfalls ausgibt.
- Lassen Sie das Programm den ersten Buchstaben des Namens in Großbuchstaben ausgeben, unabhängig davon, wie der Benutzer ihn eingegeben hat.
- Implementieren Sie eine Schleife, die den Benutzer so lange nach seinem Namen fragt, bis er eine gültige Eingabe tätigt (d. h. die Eingabe sollte nicht leer sein).

Diese Aufgabe hilft Ihnen, den Umgang mit Benutzereingaben und -ausgaben in C# zu verstehen und bereitet Sie auf komplexere Interaktionen in zukünftigen Programmen vor.
