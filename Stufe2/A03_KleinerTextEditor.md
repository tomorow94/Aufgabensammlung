# Aufgabe A03: Kleiner Text-Editor

## Ziel

Entwickeln Sie eine C#-Konsolenanwendung, die es dem Benutzer ermöglicht, Texte einzugeben, diese in einer Datei zu speichern und gespeicherte Texte wieder zu laden. Diese Aufgabe fördert den Umgang mit Dateioperationen und die Implementierung einer einfachen Benutzerführung in C#.

## Anleitung

1. **Neues Projekt erstellen:**
   - Starten Sie Visual Studio.
   - Wählen Sie "Neues Projekt erstellen" aus.
   - Wählen Sie den Projekttyp "Konsolenanwendung" aus.
   - Geben Sie dem Projekt einen aussagekräftigen Namen, z. B. "KleinerTextEditor".

2. **Programmstruktur:**
   - Das Programm sollte dem Benutzer ein Menü mit folgenden Optionen bieten:
     1. Neuen Text schreiben und speichern.
     2. Gespeicherten Text laden und anzeigen.
     3. Programm beenden.
   - Basierend auf der Auswahl des Benutzers sollte das Programm die entsprechende Funktion ausführen.

3. **Funktionen im Detail:**
   - **Neuen Text schreiben und speichern:**
     - Fordern Sie den Benutzer auf, den gewünschten Text einzugeben.
     - Speichern Sie den eingegebenen Text in einer Datei. Verwenden Sie hierfür die `System.IO`-Klassen wie `StreamWriter`.
   - **Gespeicherten Text laden und anzeigen:**
     - Laden Sie den Inhalt der zuvor gespeicherten Datei. Verwenden Sie hierfür Klassen wie `StreamReader`.
     - Geben Sie den geladenen Text in der Konsole aus.

4. **Hinweise zur Implementierung:**
   - **Fehlerbehandlung:** Stellen Sie sicher, dass das Programm ungültige Eingaben erkennt und den Benutzer entsprechend informiert.
   - **Dateipfade:** Speichern Sie die Datei im Arbeitsverzeichnis der Anwendung oder fragen Sie den Benutzer nach einem spezifischen Dateipfad.
   - **Encoding:** Achten Sie darauf, beim Lesen und Schreiben der Datei das gleiche Encoding zu verwenden, um Zeichenkodierungsprobleme zu vermeiden.

## Weiterführende Aufgaben

- **Dateiauswahl:** Erweitern Sie das Programm so, dass der Benutzer den Namen der Datei angeben kann, in der der Text gespeichert oder aus der der Text geladen werden soll.
- **Textbearbeitung:** Fügen Sie Funktionen hinzu, die es dem Benutzer ermöglichen, einen geladenen Text zu bearbeiten und die Änderungen zu speichern.
- **Formatierung:** Ermöglichen Sie dem Benutzer, einfache Formatierungen wie Zeilenumbrüche oder Absätze einzufügen.

<details>
<summary><strong>Lösungsvorschlag anzeigen</strong></summary>

```csharp
using System;
using System.IO;

namespace KleinerTextEditor
{
    class Program
    {
        static void Main(string[] args)
        {
            string dateiPfad = "textdatei.txt";
            while (true)
            {
                Console.WriteLine("Kleiner Text-Editor");
                Console.WriteLine("1. Neuen Text schreiben und speichern");
                Console.WriteLine("2. Gespeicherten Text laden und anzeigen");
                Console.WriteLine("3. Programm beenden");
                Console.Write("Wählen Sie eine Option (1-3): ");
                string eingabe = Console.ReadLine();

                switch (eingabe)
                {
                    case "1":
                        NeuenTextSchreibenUndSpeichern(dateiPfad);
                        break;
                    case "2":
                        GespeichertenTextLadenUndAnzeigen(dateiPfad);
                        break;
                    case "3":
                        Console.WriteLine("Programm wird beendet.");
                        return;
                    default:
                        Console.WriteLine("Ungültige Eingabe. Bitte wählen Sie eine Option zwischen 1 und 3.");
                        break;
                }
                Console.WriteLine();
            }
        }

        static void NeuenTextSchreibenUndSpeichern(string pfad)
        {
            Console.WriteLine("Geben Sie den Text ein (beenden mit einer leeren Zeile):");
            string text = "";
            string zeile;
            while ((zeile = Console.ReadLine()) != "")
            {
                text += zeile + Environment.NewLine;
            }

            try
            {
                File.WriteAllText(pfad, text);
                Console.WriteLine($"Text wurde erfolgreich in '{pfad}' gespeichert.");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Fehler beim Speichern der Datei: {ex.Message}");
            }
        }

        static void GespeichertenTextLadenUndAnzeigen(string pfad)
        {
            try
            {
                if (File.Exists(pfad))
                {
                    string text = File.ReadAllText(pfad);
                    Console.WriteLine("Gespeicherter Text:");
                    Console.WriteLine("-------------------");
                    Console.WriteLine(text);
                }
                else
                {
                    Console.WriteLine($"Die Datei '{pfad}' wurde nicht gefunden.");
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Fehler beim Laden der Datei: {ex.Message}");
            }
        }
    }
}
</details> ```
