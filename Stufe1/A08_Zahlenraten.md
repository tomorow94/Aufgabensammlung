# 🟢 Aufgabe A08: Zahlenraten

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
            string eingabe = Console.ReadLine();

            if (int.TryParse(eingabe, out int tipp))
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
                Console.WriteLine("Bitte gib eine gültige Zahl ein.");
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

## 💡 Probiere selbst:

- Zeige an, **wie viele Versuche übrig sind**.
- Erlaube dem Benutzer, den **Schwierigkeitsgrad** zu wählen (z. B. Zahlenbereich und Versuche).
- Speichere den **Bestwert (wenigste Versuche)** in einer Datei oder als Highscore-Liste.

---

> 🧠 Dieses Spiel verbindet Benutzereingabe, Logik, Schleifen und Bedingungen zu einem kleinen, unterhaltsamen Projekt!

