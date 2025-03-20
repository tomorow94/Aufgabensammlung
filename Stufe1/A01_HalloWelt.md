# Aufgabe A01: Hallo Welt

## Ziel

Erstellen Sie ein einfaches C#-Programm, das die Nachricht "Hallo Welt!" auf der Konsole ausgibt. Diese Aufgabe dient dazu, Sie mit der grundlegenden Struktur eines C#-Programms und der Entwicklungsumgebung vertraut zu machen.

## Anleitung

1. **Entwicklungsumgebung einrichten:**
   - Stellen Sie sicher, dass auf Ihrem Computer eine aktuelle Version von Visual Studio installiert ist.
   - Falls noch nicht geschehen, laden Sie die Community Edition von Visual Studio von der [offiziellen Microsoft-Website](https://visualstudio.microsoft.com/de/vs/community/) herunter und installieren Sie diese.

2. **Neues Projekt erstellen:**
   - Starten Sie Visual Studio.
   - Wählen Sie "Neues Projekt erstellen" aus.
   - Wählen Sie unter den verfügbaren Projekttypen "Konsolenanwendung" aus.
   - Geben Sie dem Projekt einen aussagekräftigen Namen, z. B. "HalloWelt".

3. **Programmcode schreiben:**
   - Ersetzen Sie den automatisch generierten Code durch folgenden Inhalt:

     ```csharp
     using System;

     namespace HalloWelt
     {
         class Program
         {
             static void Main(string[] args)
             {
                 Console.WriteLine("Hallo Welt!");
             }
         }
     }
     ```

     Dieser Code nutzt die `Console.WriteLine`-Methode, um den Text "Hallo Welt!" auf der Konsole auszugeben.

4. **Programm ausführen:**
   - Speichern Sie alle Änderungen.
   - Drücken Sie die Taste `F5` oder klicken Sie auf "Starten", um das Programm auszuführen.
   - Überprüfen Sie, ob die Nachricht "Hallo Welt!" in der Konsole angezeigt wird.

## Hinweise

- **Namenskonventionen:** In C# ist es üblich, für Klassen und Methoden die PascalCase-Schreibweise zu verwenden.
- **Groß- und Kleinschreibung:** C# unterscheidet zwischen Groß- und Kleinschreibung. Achten Sie daher auf die korrekte Schreibweise von Befehlen und Bezeichnern.
- **Ressourcen:** Weitere Informationen zur Erstellung eines "Hallo Welt"-Programms in C# finden Sie in der offiziellen Microsoft-Dokumentation: [Einführung in C# - Interaktives Tutorial](https://learn.microsoft.com/de-de/dotnet/csharp/tour-of-csharp/tutorials/hello-world).

## Weiterführende Aufgaben

- Experimentieren Sie mit der `Console.WriteLine`-Methode, indem Sie verschiedene Nachrichten ausgeben.
- Fügen Sie zusätzliche `Console.WriteLine`-Aufrufe hinzu, um mehrere Zeilen Text anzuzeigen.
- Ersetzen Sie die Nachricht "Hallo Welt!" durch eine andere Zeichenkette Ihrer Wahl.

Diese Aufgabe bildet die Grundlage für weiterführende Übungen und soll Ihnen den Einstieg in die Programmierung mit C# erleichtern.
