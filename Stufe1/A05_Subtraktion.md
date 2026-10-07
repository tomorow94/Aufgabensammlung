# 🟢 Aufgabe A05: Subtraktion und sichere Zahleneingabe

## Einordnung und Lernziele

**Status:** Pflicht im Lernfaden.

**Voraussetzungen:** [Größere Zahl finden](A04_GroessereZahlFinden.md)

**Intention:** Ungültige Zahleneingaben kontrolliert behandeln.

**Lernziele:**

- Du kannst TryParse mit einem Erfolgswert und einer Ausgabevariablen verwenden.
- Du kannst ungültigen Text abweisen, ohne die Rechnung auszuführen.

**Weiter im Pflichtpfad:** [Multiplikation und Wiederholung](A06_Multiplikation.md)

## Ziel und Voraussetzungen

Nach Addition und Zahlenvergleich berechnest du eine Differenz. Neu ist die **Eingabeprüfung mit `TryParse`**: Bei ungültigem Text wie `abc` zeigt das Programm eine Meldung an und beendet die Berechnung. Erstelle eine C#-Konsolenanwendung mit .NET 10 und ersetze den Inhalt von `Program.cs`.

## Anforderungen

1. Lies zwei Zahlen ein und berechne erste minus zweite Zahl.
2. Prüfe beide Eingaben. Bei ungültigem Text gib eine Meldung aus und beende die Berechnung.
3. Nutze negative Zahlen und Kommazahlen. Das Dezimaltrennzeichen richtet sich nach der Spracheinstellung des Rechners, in einer deutschen Umgebung etwa `5,5`.

`TryParse(text, out zahl)` liefert `true`, wenn die Umwandlung gelingt. `out` schreibt den Zahlenwert in die Variable. `!` kehrt einen Wahrheitswert um; `||` bedeutet „oder“. `return` beendet hier die Methode `Main`.

## Gestufte Hinweise

Versuche zuerst eine eigene Lösung. Öffne bei Bedarf zunächst Hinweis 1 und erst danach Hinweis 2; die vorhandenen Beispiele bzw. Referenzen dienen anschließend zum Vergleichen.

<details>
<summary>Hinweis 1: Denkanstoß</summary>

Woran erkennst du, ob eine Umwandlung erfolgreich war?

</details>

<details>
<summary>Hinweis 2: Vorgehensweise</summary>

TryParse liefert bool; bei false wird der Rechenweg nicht betreten, bei true darfst du den gelesenen Wert verwenden.

</details>

<details>
<summary>Lösungsvorschlag</summary>

```csharp
using System;
class Program
{
    static void Main()
    {
        Console.Write("Erste Zahl: ");
        if (!double.TryParse(Console.ReadLine(), out double a) || !double.IsFinite(a))
        {
            Console.WriteLine("Bitte eine gültige, endliche Zahl eingeben.");
            return;
        }
        Console.Write("Zweite Zahl: ");
        if (!double.TryParse(Console.ReadLine(), out double b) || !double.IsFinite(b))
        {
            Console.WriteLine("Bitte eine gültige, endliche Zahl eingeben.");
            return;
        }
        Console.WriteLine($"{a} minus {b} ergibt {a - b}.");
    }
}
```

`IsFinite` schließt die Sonderwerte `NaN` und Unendlich aus. Die Zahlen sollen hier gewöhnliche Rechenwerte sein.

</details>

## Selbst prüfen

| Eingaben | Erwartung |
|---|---|
| `10`, `4` | `6` |
| `4`, `10` | `-6` |
| `5,5`, `2` (deutsche Umgebung) | `3,5` |
| `abc` oder leere Eingabe | Meldung, keine Berechnung |

Setze einen Haltepunkt an die erste `if`-Bedingung. Beobachte `a` bei gültiger und ungültiger Eingabe.

## Bonus: Zahleneingabe wiederholen

**Intention:** Vertiefe die Eingabeprüfung mit der nächsten Kontrollstruktur.

**Lernziel:** Nach A06 kannst du ungültige Eingaben in einer Schleife erneut abfragen.

Wiederhole die Eingabe, bis eine gültige Zahl vorliegt; dafür lernst du in der nächsten Aufgabe eine Schleife kennen.

## Passende Lernquellen

[Leseempfehlung für diesen Lernschritt](../Referenzen/Lernquellen.md#stufe-1-eingaben-und-ablauf). Wähle den dort genannten Abschnitt zur aktuellen Aufgabe und probiere ihn in deinem eigenen Programm aus.
