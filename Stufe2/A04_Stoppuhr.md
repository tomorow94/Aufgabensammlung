# Aufgabe A04: Stoppuhr

## Ziel

Entwickeln Sie eine C#-Konsolenanwendung, die eine Stoppuhr simuliert. Der Benutzer soll die Möglichkeit haben, die Zeitmessung zu starten, zu stoppen, sich die verstrichene Zeit anzeigen zu lassen und die Stoppuhr zurückzusetzen. Diese Aufgabe dient dazu, die Arbeit mit Zeitmessungen in C# mithilfe der `Stopwatch`-Klasse aus dem `System.Diagnostics`-Namespace zu üben.

## Anforderungen

1. **Neues Projekt erstellen:**
   - Starten Sie Visual Studio.
   - Wählen Sie "Neues Projekt erstellen".
   - Wählen Sie als Projekttyp "Konsolenanwendung".
   - Geben Sie dem Projekt den Namen `Stoppuhr`.

2. **Funktionen der Stoppuhr:**
   - **Starten der Zeitmessung**: Der Benutzer kann die Stoppuhr starten.
   - **Stoppen der Zeitmessung**: Die Stoppuhr kann angehalten werden.
   - **Anzeige der verstrichenen Zeit**: Die verstrichene Zeit soll formatiert auf der Konsole angezeigt werden.
   - **Zurücksetzen der Stoppuhr**: Die gemessene Zeit kann auf null gesetzt werden.
   - **Menüsteuerung**: Die Anwendung soll ein Menü mit den genannten Optionen bereitstellen.

3. **Technische Umsetzung:**
   - Verwenden Sie die `Stopwatch`-Klasse für die Zeitmessung.
   - Nutzen Sie eine `while`-Schleife, um das Menü solange anzuzeigen, bis der Benutzer das Programm beendet.
   - Verwenden Sie `if`- oder `switch`-Anweisungen, um die Benutzereingaben zu verarbeiten.
   - Formatieren Sie die Zeitausgabe im Format `hh:mm:ss.fff`.

## Hinweise zur Implementierung

- **Fehlerbehandlung**: Stellen Sie sicher, dass ungültige Eingaben abgefangen werden.
- **Statusprüfung**: Überprüfen Sie, ob die Stoppuhr bereits läuft oder gestoppt ist, bevor Sie Aktionen ausführen.
- **Nutzerführung**: Das Programm soll dem Benutzer klar kommunizieren, welche Aktionen verfügbar sind.

## Erweiterungen (Optional)

- **Rundenzeiten**: Der Benutzer kann Zwischenzeiten erfassen, die separat gespeichert werden.
- **Speicherung der Zeiten**: Gespeicherte Zeiten werden in einer Datei abgelegt und können später erneut geladen werden.
- **Grafische Oberfläche**: Optional kann eine einfache GUI mit `Windows Forms` oder `WPF` erstellt werden.

<details>
<summary><strong>Lösungsvorschlag anzeigen</strong></summary>

```csharp
using System;
using System.Diagnostics;

namespace Stoppuhr
{
    class Program
    {
        static void Main(string[] args)
        {
            Stopwatch stoppuhr = new Stopwatch();
            bool laeuft = true;

            while (laeuft)
            {
                Console.WriteLine("Stoppuhr - Menü:");
                Console.WriteLine("1. Starten");
                Console.WriteLine("2. Stoppen");
                Console.WriteLine("3. Zeit anzeigen");
                Console.WriteLine("4. Zurücksetzen");
                Console.WriteLine("5. Beenden");
                Console.Write("Wählen Sie eine Option: ");
                string eingabe = Console.ReadLine();

                switch (eingabe)
                {
                    case "1":
                        if (!stoppuhr.IsRunning)
                        {
                            stoppuhr.Start();
                            Console.WriteLine("Stoppuhr gestartet.");
                        }
                        else
                        {
                            Console.WriteLine("Die Stoppuhr läuft bereits.");
                        }
                        break;
                    case "2":
                        if (stoppuhr.IsRunning)
                        {
                            stoppuhr.Stop();
                            Console.WriteLine("Stoppuhr gestoppt.");
                        }
                        else
                        {
                            Console.WriteLine("Die Stoppuhr ist nicht gestartet.");
                        }
                        break;
                    case "3":
                        TimeSpan zeit = stoppuhr.Elapsed;
                        Console.WriteLine($"Verstrichene Zeit: {zeit:hh\\:mm\\:ss\\.fff}");
                        break;
                    case "4":
                        stoppuhr.Reset();
                        Console.WriteLine("Stoppuhr wurde zurückgesetzt.");
                        break;
                    case "5":
                        laeuft = false;
                        Console.WriteLine("Programm beendet.");
                        break;
                    default:
                        Console.WriteLine("Ungültige Eingabe, bitte erneut versuchen.");
                        break;
                }
                Console.WriteLine();
            }
        }
    }
}
</details> ```
