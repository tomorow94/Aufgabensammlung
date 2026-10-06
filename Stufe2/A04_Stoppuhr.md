# 🔵 Aufgabe A04: Stoppuhr

## Ziel der Aufgabe

Erstelle ein einfaches Konsolenprogramm, das wie eine **Stoppuhr** funktioniert. Du lernst, wie du mit **Zeitmessung**, **Menüsteuerung** und **Methoden** arbeitest.

Diese Aufgabe verlangt, dass du den Code **selbst schreibst**. Orientiere dich an bekannten Mustern oder recherchiere gezielt nach passenden Befehlen in C#.

Das Programm soll dem Benutzer folgende Optionen bieten:

1. Stoppuhr starten
2. Stoppuhr stoppen
3. Verstrichene Zeit anzeigen
4. Stoppuhr zurücksetzen
5. Programm beenden

Die Auswahl erfolgt über eine Menüführung mit `switch` und wird in einer Schleife so lange wiederholt, bis der Benutzer das Programm beendet.

---

## Was du lernst

* Wie du mit der Klasse `Stopwatch` eine Zeitmessung implementierst
* Wie du eine einfache **Menüführung** mit Benutzerinteraktion aufbaust
* Wie du durch Methoden deinen Code **strukturiert und wiederverwendbar** machst
* Wie man **Zustände prüft**, z. B. ob eine Stoppuhr läuft

💡 Die Stopwatch-Klasse eignet sich auch hervorragend zur Performance-Messung einzelner Programmabschnitte. Wenn du z. B. herausfinden möchtest, warum dein Programm langsam ist oder ob eine Optimierung tatsächlich einen Unterschied macht, kannst du gezielt Zeitmessungen einbauen und die Ergebnisse in Log-Dateien schreiben.

---

## Vorgehen & Tipps

1. **Plane dein Programm zuerst in Stichpunkten.** Das hilft dir, den Überblick zu behalten.

   Beispiel:

   ```csharp
   // Menü anzeigen
   // Benutzereingabe verarbeiten
   // Option 1: Stoppuhr starten
   // Option 2: Stoppuhr stoppen
   // Option 3: Zeit anzeigen
   // Option 4: Stoppuhr zurücksetzen
   // Option 5: Programm beenden
   ```

2. **Nutze die Klasse `Stopwatch`:**

   ```csharp
   Stopwatch sw = new Stopwatch();
   sw.Start();
   sw.Stop();
   Console.WriteLine(sw.Elapsed);
   sw.Reset();
   ```

3. **Formatierte Zeitausgabe:**

   ```csharp
   Console.WriteLine($"Verstrichene Zeit: {sw.Elapsed:hh\\:mm\\:ss\\.fff}");
   ```

   Alternativ geht auch:

   ```csharp
   Console.WriteLine("Verstrichene Zeit: " + sw.Elapsed.ToString(@"hh\:mm\:ss\.fff"));
   ```

   🔎 **Hinweis:** Beispiel 1 verwendet einen interpolierten Format-String, was funktioniert, da es sich bei der `Elapsed`-Zeit von `Stopwatch` um den Datentyp `TimeSpan` handelt. Beispiel 2 verwendet eine weiter verbreitete Lösung, die die Methode `ToString()` aufruft, der ein Format-String übergeben werden muss. Der Format-String bestimmt, wie die Zeit dargestellt wird. Eine andere Formatierung wäre beispielsweise `@"hh\:mm\:ss"`.

4. **Zustand prüfen:**

   ```csharp
   if (sw.IsRunning)
   {
       Console.WriteLine("Die Stoppuhr läuft.");
   }
   else
   {
       Console.WriteLine("Die Stoppuhr ist gestoppt.");
   }
   ```

5. **Strukturiere deinen Code in Methoden:**

   * `StarteStoppuhr()`
   * `StoppeStoppuhr()`
   * `ZeigeZeit()`
   * `Zuruecksetzen()`

---

## Weiterführende Ideen


* Gib dem Benutzer die Möglichkeit **Zwischenzeiten** zu erfassen, die separat in einer Liste gespeichert werden
* Gib dem Benutzer die Möglichkeit, die **Zwischenzeiten** einzusehen
* Ermögliche das Speichern der Zeitwerte in einer Datei
* Implementiere eine Funktion, die nach einer gewissen Zeit automatisch stoppt (Timer)
* Baue eine einfache **GUI** mit **Windows Forms** oder **WPF**

---

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
                string? eingabe = Console.ReadLine();
                if (eingabe is null) return;

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
```

</details>

## Selbst prüfen

Start → kurz warten → Stop → Anzeige ergibt eine positive Zeit. Während Stop verändert sich die Zeit nicht. Ein weiterer Start setzt die Messung fort. Reset setzt Zeit auf null und stoppt die Uhr. Doppelter Start/Stop führt nicht zum Absturz. Für einen Neustart mit sofortiger Messung gibt es `Restart()`.
