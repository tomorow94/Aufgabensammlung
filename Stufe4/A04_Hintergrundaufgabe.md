# 🟡 Bonus A04: Hintergrundberechnung mit Fortschritt

## Einordnung und Lernziele

**Status:** Bonus (optional; keine Voraussetzung für spätere Pflichtaufgaben).

**Voraussetzungen:** [Primzahlenprüfung](../Stufe2/A02_Primzahlen.md), [Hangman](A02_Hangman.md)

**Intention:** Nebenläufigkeit an einer zusätzlichen längeren Berechnung untersuchen.

**Lernziele:**

- Du kannst CPU-Arbeit, Fortschritt und kooperativen Abbruch unterscheiden.
- Du kannst erklären, weshalb async allein eine Rechnung nicht verlagert.

**Weiter im Pflichtpfad:** [Einfaches Bankkonto-System](A03_Bankkonto.md)

## Ziel und Voraussetzungen

Zwei Spieler ziehen bei Tic-Tac-Toe nacheinander; dafür sind keine zusätzlichen Threads nötig. Untersuche Nebenläufigkeit stattdessen an einer **längeren CPU-Berechnung**, während die Oberfläche Fortschritt zeigt und eine Abbruchmöglichkeit anbietet.

Diese Aufgabe ist optional. Du brauchst Methoden, Primzahlprüfung und Verständnis für gemeinsam genutzte Zustände. Ein Thread ist ein Ausführungsstrang; `Task` beschreibt eine Arbeit, die etwa auf einem Threadpool-Thread laufen kann. `await` wartet, ohne den wartenden Thread blockieren zu müssen. `async` allein verlagert keine CPU-Arbeit in den Hintergrund.

## Anforderungen

1. Zähle Primzahlen in einer Hintergrundaufgabe mit `Task.Run`.
2. Zeige auf dem Hauptablauf regelmäßig den Fortschritt an.
3. Erlaube Abbruch über `q` mit `CancellationToken`.
4. Teile nur einen Fortschrittswert. Aktualisiere ihn mit `Interlocked`, lies ihn mit `Volatile`.
5. Warte am Ende auf die Aufgabe und behandle Abbruch gezielt. Halte keine Sperre während einer Eingabe und verwende keine Schleife ohne Wartepause zum Warten auf einen Zustand.

## Gestufte Hinweise

Versuche zuerst eine eigene Lösung. Öffne bei Bedarf zunächst Hinweis 1 und erst danach Hinweis 2; die vorhandenen Beispiele bzw. Referenzen dienen anschließend zum Vergleichen.

<details>
<summary>Hinweis 1: Denkanstoß</summary>

Welche Arbeit dauert lange und wann kann sie einen Abbruch bemerken?

</details>

<details>
<summary>Hinweis 2: Vorgehensweise</summary>

Verlagere CPU-Arbeit bewusst und prüfe das CancellationToken regelmäßig; speichere keine unbeaufsichtigten gemeinsamen Zustände.

</details>

<details>
<summary>Lösungsvorschlag für Program.cs (.NET 10)</summary>

```csharp
using System;
using System.Threading;
using System.Threading.Tasks;
class Program
{
    static int progress;
    static async Task Main()
    {
        using var cancellation = new CancellationTokenSource();
        Task<int> work = Task.Run(() => CountPrimes(2_000_000, cancellation.Token));
        Console.WriteLine("Primzahlen zählen; q bricht ab.");
        while (!work.IsCompleted)
        {
            Console.Write($"\rFortschritt: {Volatile.Read(ref progress),3}% ");
            if (!Console.IsInputRedirected && Console.KeyAvailable && Console.ReadKey(true).Key == ConsoleKey.Q)
                cancellation.Cancel();
            await Task.Delay(100);
        }
        try
        {
            int count = await work;
            Console.WriteLine($"\nFertig: {count} Primzahlen.");
        }
        catch (OperationCanceledException) { Console.WriteLine("\nBerechnung abgebrochen."); }
    }
    static int CountPrimes(int limit, CancellationToken token)
    {
        int count = 0;
        for (int number = 2; number <= limit; number++)
        {
            token.ThrowIfCancellationRequested();
            if (IsPrime(number)) count++;
            if (number % 1000 == 0) Interlocked.Exchange(ref progress, (int)(number * 100L / limit));
        }
        Interlocked.Exchange(ref progress, 100);
        return count;
    }
    static bool IsPrime(int number)
    {
        if (number < 2) return false;
        for (int divisor = 2; divisor <= number / divisor; divisor++)
            if (number % divisor == 0) return false;
        return true;
    }
}
```

</details>

## Selbst prüfen

Mit Grenze `10` ist das Ergebnis `4`, mit `100` ist es `25`. Bei großer Grenze bleibt die Anzeige aktiv; `q` beendet die Arbeit geordnet. Wiederholte vollständige Läufe liefern denselben Wert. Mit umgeleiteter Eingabe wird kein Konsolentastenzugriff versucht. Setze Haltepunkte in Hintergrund- und Hauptablauf und vergleiche die Threads im Debugger.

## Bonus: Weitere Fortschrittsmechanismen

**Intention:** Untersuche eine zusätzliche Abstraktion für Fortschritt und gemeinsamen Zustand.

**Lernziel:** Du kannst IProgress-Meldungen einem Ausführungskontext zuordnen; lock und Monitor sind weitere spätere Vertiefungen.

Verwende `IProgress<int>` für Fortschrittsmeldungen; untersuche dann, auf welchem Kontext die Meldungen verarbeitet werden. Raw `Thread`, `lock` und `Monitor.Wait/Pulse` sind eine spätere Vertiefung, wenn tatsächlich mehrere Ausführungsstränge einen gemeinsamen Zustand koordinieren müssen.

## Passende Lernquellen

[Leseempfehlung für diesen Lernschritt](../Referenzen/Lernquellen.md#stufe-4-zustand-und-geschäftsregeln). Wähle den dort genannten Abschnitt zur aktuellen Aufgabe und probiere ihn in deinem eigenen Programm aus.
