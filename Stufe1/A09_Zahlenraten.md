# 🟢 Aufgabe A09: Zahlenraten

## Einordnung und Lernziele

**Status:** Pflicht im Lernfaden.

**Voraussetzungen:** [Taschenrechner mit Menü](A08_Taschenrechner.md)

**Intention:** Schleifen, Zufall und Bedingungen an einem überschaubaren Spiel verbinden.

**Lernziele:**

- Du kannst eine Zufallszahl im Bereich 1–100 erzeugen und Hinweise ableiten.
- Du kannst gültige Versuche zählen und einen Gewinn von ausgeschöpften Versuchen unterscheiden.

**Weiter im Pflichtpfad:** [Fibonacci als Zahlenfolge](A10_Fibonacci.md)

## Ziel der Aufgabe

In dieser Aufgabe programmierst du ein kleines Spiel: Der Computer denkt sich eine Zahl zwischen 1 und 100 aus, und du musst sie erraten. Nach jedem Versuch bekommst du einen Hinweis, ob du zu hoch oder zu niedrig liegst. Du hast maximal 10 Versuche.

Dabei lernst du, wie man mit **Zufallszahlen**, **Schleifen**, **Vergleichen** und **Benutzereingaben** arbeitet.

---

## Was du lernst

- Wie man mit der Klasse `Random` Zufallszahlen erzeugt
- Wie man eine Schleife nutzt, um wiederholt Benutzereingaben zu verarbeiten
- Wie man mit `if`-Bedingungen reagiert und Feedback gibt
- Wie man mit `int.TryParse()` Eingaben sicher verarbeitet

---

## Gestufte Hinweise

Versuche zuerst eine eigene Lösung. Öffne bei Bedarf zunächst Hinweis 1 und erst danach Hinweis 2; die vorhandenen Beispiele bzw. Referenzen dienen anschließend zum Vergleichen.

<details>
<summary>Hinweis 1: Denkanstoß</summary>

Wann darf der Versuchszähler steigen und wann endet die Runde?

</details>

<details>
<summary>Hinweis 2: Vorgehensweise</summary>

Ungültiger Text verbraucht keinen Versuch; vergleiche gültige Werte mit dem Ziel und prüfe die Grenze von zehn Versuchen.

</details>

## Schritt-für-Schritt-Anleitung

### 🔧 1. Projekt erstellen

1. Starte Visual Studio.
2. Neues Projekt: **Konsolenanwendung (C#)**.
3. Projektname: z. B. `Zahlenraten`

---

### 💻 2. Code eingeben

```csharp
using System;

class Program
{
    static void Main(string[] args)
    {
        Random zufall = new Random();
        int geheimzahl = zufall.Next(1, 101); // Zahl von 1 bis 100

        int versuche = 0;
        int maxVersuche = 10;
        bool erraten = false;

        Console.WriteLine("Ich habe eine Zahl zwischen 1 und 100 im Kopf.");
        Console.WriteLine($"Du hast {maxVersuche} Versuche. Viel Glück!\n");

        while (versuche < maxVersuche && !erraten)
        {
            Console.Write($"Versuch {versuche + 1}: Deine Zahl? ");
            string? eingabe = Console.ReadLine();
            if (eingabe is null) return;

            if (int.TryParse(eingabe, out int tipp) && tipp >= 1 && tipp <= 100)
            {
                versuche++;

                if (tipp < geheimzahl)
                {
                    Console.WriteLine("Zu niedrig!");
                }
                else if (tipp > geheimzahl)
                {
                    Console.WriteLine("Zu hoch!");
                }
                else
                {
                    erraten = true;
                    Console.WriteLine($"Richtig! Die Zahl war {geheimzahl}.");
                    Console.WriteLine($"Du hast {versuche} Versuch(e) gebraucht.");
                }
            }
            else
            {
                Console.WriteLine("Bitte gib eine ganze Zahl zwischen 1 und 100 ein.");
            }
        }

        if (!erraten)
        {
            Console.WriteLine($"Leider verloren. Die Zahl war {geheimzahl}.");
        }

        Console.WriteLine("\nSpiel beendet. Danke fürs Mitmachen!");
    }
}
```

---

### ▶️ 3. Ausführen

- Starte das Spiel mit `F5`.
- Gib verschiedene Zahlen ein und beachte die Hinweise.
- Probiere aus, was passiert, wenn du ungültige Eingaben machst (z. B. Buchstaben).

---

## 🔍 Erklärt

| Konzept             | Beschreibung |
|---------------------|--------------|
| `Random`            | Erstellt eine Zufallszahl mit `Next(1, 101)` für Bereich 1–100 |
| `TryParse()`        | Verhindert Programmabsturz bei ungültiger Eingabe (z. B. "abc") |
| `while`             | Wiederholt den Spielablauf, solange Versuche < max und nicht erraten |
| `bool`              | Der Typ für Wahr/Falsch-Werte (z. B. `bool erraten = false`) |
| `if / else if`      | Unterscheidet verschiedene Bedingungen: zu hoch, zu niedrig, richtig |

---

## Selbst prüfen

Setze zum Prüfen vorübergehend `geheimzahl = 50`. `25` ergibt „zu niedrig“, `75` „zu hoch“, `50` den Gewinn. Zehn falsche gültige Tipps ergeben eine Niederlage. Ungültiger Text und Zahlen außerhalb 1–100 verbrauchen keinen Versuch. Setze danach die Zufallsauswahl wieder ein.

## Bonus: Spielvarianten

**Intention:** Verändere gezielt die Spielregeln und untersuche zusätzliche Speicherung.

**Lernziel:** Du kannst Schwierigkeit durch Zahlenbereich und Versuchslimit steuern; eine Highscore-Datei setzt Stufe 2, A03 voraus.


- Zeige an, **wie viele Versuche übrig sind**.
- Erlaube dem Benutzer, den **Schwierigkeitsgrad** zu wählen (z. B. Zahlenbereich und Versuche).
- Speichere den **Bestwert (wenigste Versuche)** in einer Datei oder als Highscore-Liste.

---

> 🧠 Dieses Spiel verbindet Benutzereingabe, Logik, Schleifen und Bedingungen zu einem kleinen, unterhaltsamen Projekt!

## Passende Lernquellen

[Leseempfehlung für diesen Lernschritt](../Referenzen/Lernquellen.md#stufe-1-eingaben-und-ablauf). Wähle den dort genannten Abschnitt zur aktuellen Aufgabe und probiere ihn in deinem eigenen Programm aus.
