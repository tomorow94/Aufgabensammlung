# 🟢 Aufgabe A06: Multiplikation und Wiederholung

## Einordnung und Lernziele

**Status:** Pflicht im Lernfaden.

**Voraussetzungen:** [Subtraktion und sichere Zahleneingabe](A05_Subtraktion.md)

**Intention:** Eine geprüfte Berechnung kontrolliert wiederholen.

**Lernziele:**

- Du kannst eine while-Schleife mit einer Beenden-Option steuern.
- Du kannst erklären, wann break und continue den Ablauf verändern.

**Weiter im Pflichtpfad:** [Division](A07_Division.md)

## Ziel und Voraussetzungen

Du kannst bereits Zahlen einlesen, vergleichen und mit `TryParse` prüfen. Jetzt wiederholst du eine Berechnung mit einer **`while`-Schleife**. Eine Schleife führt ihren Block erneut aus, solange ihre Bedingung wahr ist.

## Anforderungen

1. Lies zwei Zahlen ein und gib ihr Produkt aus.
2. Bei ungültigen Eingaben beginne einen neuen Durchlauf.
3. Nach einer Berechnung fragt das Programm, ob du weiterrechnen möchtest.

`continue` startet den nächsten Schleifendurchlauf. `break` beendet die Schleife. Der Vergleich mit `OrdinalIgnoreCase` akzeptiert `j` und `J`.

## Gestufte Hinweise

Versuche zuerst eine eigene Lösung. Öffne bei Bedarf zunächst Hinweis 1 und erst danach Hinweis 2; die vorhandenen Beispiele bzw. Referenzen dienen anschließend zum Vergleichen.

<details>
<summary>Hinweis 1: Denkanstoß</summary>

Welche Eingabe soll die Wiederholung beenden, welche nur den aktuellen Versuch?

</details>

<details>
<summary>Hinweis 2: Vorgehensweise</summary>

Prüfe Beenden vor der Rechnung; ungültige Eingabe überspringt den Versuch, gültige Eingabe führt zur Multiplikation.

</details>

<details>
<summary>Lösungsvorschlag für Program.cs (.NET 10)</summary>

```csharp
using System;
class Program
{
    static void Main()
    {
        while (true)
        {
            Console.Write("Erste Zahl (oder Ende der Eingabe zum Beenden): ");
            string? text = Console.ReadLine();
            if (text is null) break;
            if (!double.TryParse(text, out double a) || !double.IsFinite(a))
            {
                Console.WriteLine("Ungültige Zahl.");
                continue;
            }
            Console.Write("Zweite Zahl: ");
            if (!double.TryParse(Console.ReadLine(), out double b) || !double.IsFinite(b))
            {
                Console.WriteLine("Ungültige Zahl.");
                continue;
            }
            double product = a * b;
            Console.WriteLine(double.IsFinite(product) ? $"Produkt: {product}" : "Ergebnis außerhalb des Zahlenbereichs.");
            Console.Write("Noch einmal? (j/n): ");
            if (!string.Equals(Console.ReadLine()?.Trim(), "j", StringComparison.OrdinalIgnoreCase)) break;
        }
    }
}
```

</details>

## Selbst prüfen

| Ablauf | Erwartung |
|---|---|
| `3`, `4`, `n` | `12`, Programm endet |
| `-3`, `4`, `j`, `0`, `9`, `n` | `-12`, dann `0` |
| `abc`, danach gültige Zahlen | Meldung, anschließend neue Eingabe |
| Antwort `J` | weitere Berechnung |

Setze einen Haltepunkt am Schleifenanfang. Verfolge, wohin `continue` und `break` springen.

## Bonus: Berechnungen zählen

**Intention:** Speichere zusätzliche Informationen über Schleifendurchläufe.

**Lernziel:** Du kannst nur erfolgreiche Rechnungen zählen und den Zähler nach mehreren Versuchen prüfen.

Zähle die erfolgreichen Berechnungen.

## Passende Lernquellen

[Leseempfehlung für diesen Lernschritt](../Referenzen/Lernquellen.md#stufe-1-eingaben-und-ablauf). Wähle den dort genannten Abschnitt zur aktuellen Aufgabe und probiere ihn in deinem eigenen Programm aus.
