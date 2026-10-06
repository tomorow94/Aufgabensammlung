# 🟢 Aufgabe A08: Taschenrechner mit Menü

## Einordnung und Lernziele

**Status:** Pflicht im Lernfaden.

**Voraussetzungen:** [Division](A07_Division.md)

**Intention:** Bekannte Rechenoperationen in einem gemeinsamen Ablauf kombinieren.

**Lernziele:**

- Du kannst die Auswahl mit switch auf vier Rechenwege abbilden.
- Du kannst ungültige Auswahl, ungültige Zahl und Beenden getrennt behandeln.

**Weiter im Pflichtpfad:** [Zahlenraten](A09_Zahlenraten.md)

## Ziel und Voraussetzungen

Kombiniere Eingabeprüfung, Bedingungen und Schleifen zu einem Taschenrechner. Neu ist **`switch`**: abhängig von einer Auswahl wird genau ein passender Zweig ausgeführt.

## Anforderungen

1. Biete `+`, `-`, `*`, `/` und `0` zum Beenden an.
2. Prüfe beide Zahlen und verhindere die Division durch null.
3. Nach einer Rechnung erscheint wieder das Menü.

## Gestufte Hinweise

Versuche zuerst eine eigene Lösung. Öffne bei Bedarf zunächst Hinweis 1 und erst danach Hinweis 2; die vorhandenen Beispiele bzw. Referenzen dienen anschließend zum Vergleichen.

<details>
<summary>Hinweis 1: Denkanstoß</summary>

Welche Eingabe entscheidet über den Rechenweg, welche liefert die Operanden?

</details>

<details>
<summary>Hinweis 2: Vorgehensweise</summary>

Werte zuerst die Menüauswahl aus; lies Zahlen erst für eine gültige Operation und prüfe die Division gesondert.

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
            Console.Write("Operation (+, -, *, /; 0 = Ende): ");
            string? operation = Console.ReadLine()?.Trim();
            if (operation is null or "0") return;
            if (operation != "+" && operation != "-" && operation != "*" && operation != "/")
            {
                Console.WriteLine("Ungültige Operation.");
                continue;
            }
            Console.Write("Erste Zahl: ");
            if (!double.TryParse(Console.ReadLine(), out double a) || !double.IsFinite(a))
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
            if (operation == "/" && b == 0)
            {
                Console.WriteLine("Division durch null ist nicht erlaubt.");
                continue;
            }
            double result = 0;
            switch (operation)
            {
                case "+": result = a + b; break;
                case "-": result = a - b; break;
                case "*": result = a * b; break;
                case "/": result = a / b; break;
            }
            Console.WriteLine(double.IsFinite(result) ? $"Ergebnis: {result}" : "Ergebnis außerhalb des Zahlenbereichs.");
        }
    }
}
```

</details>

## Selbst prüfen

| Operation und Zahlen | Erwartung |
|---|---|
| `+`, `2`, `3` | `5` |
| `-`, `2`, `3` | `-1` |
| `*`, `2`, `3` | `6` |
| `/`, `7`, `2` | `3,5` in deutscher Umgebung |
| `/`, `2`, `0` | Fehlermeldung, danach Menü |
| `?`, `abc`, leere Zahleneingabe | Meldung, kein Absturz |
| `0` im Menü | Programm endet |

Setze einen Haltepunkt an `switch` und gehe mit F10 durch eine Division.

## Bonus: Rechnen als Methode

**Intention:** Bereite die Trennung von Rechnung und Konsole vor.

**Lernziel:** Nach Stufe 2, A01 kannst du die Rechenlogik mit Parametern und Rückgabewert unabhängig von Konsoleneingaben aufrufen.

Schreibe `static double Calculate(double a, double b, string operation)` und trenne reine Berechnung von Konsoleneingaben. Verwende gezielte Exceptions nur für unzulässige Methodenargumente; gewöhnliche Menüauswahl benötigt keine Exception.

## Passende Lernquellen

[Leseempfehlung für diesen Lernschritt](../Referenzen/Lernquellen.md#stufe-1-eingaben-und-ablauf). Wähle den dort genannten Abschnitt zur aktuellen Aufgabe und probiere ihn in deinem eigenen Programm aus.
