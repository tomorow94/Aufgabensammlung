# 🟡 Aufgabe A02: Hangman

## Ziel und Voraussetzungen

Du kennst Arrays, Listen und Spielzustände aus Tic-Tac-Toe. Jetzt verarbeitest du Zeichenketten und einzelne Buchstaben. Der Computer wählt ein Wort; richtige Buchstaben werden aufgedeckt, falsche verringern die verbleibenden Versuche.

## Anforderungen

1. Wähle ein zufälliges Wort aus einer Liste und zeige zunächst `_` an.
2. Akzeptiere genau einen Buchstaben, unabhängig von Groß-/Kleinschreibung.
3. Bereits geratene Buchstaben und ungültige Eingaben verbrauchen keinen Versuch.
4. Erlaube sieben Fehlversuche. Dafür brauchst du **acht Bilder**: Anfangszustand plus sieben Fehlerzustände.
5. Nach Sieg oder Niederlage zeige das Wort an. Fehlermeldungen bleiben sichtbar.

<details>
<summary>Lösungsvorschlag für Program.cs (.NET 10)</summary>

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
class Hangman
{
    static readonly string[] words = { "computer", "programming", "developer", "software", "keyboard" };
    const int MaxMistakes = 7;
    static string chosenWord = "";
    static char[] guessedWord = [];
    static readonly HashSet<char> guessedLetters = [];
    static int attemptsLeft = MaxMistakes;
    static readonly string[] stages =
    {
        "\n\n\n\n\n\n=========",
        "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n========="
    };
    static void Main()
    {
        chosenWord = words[Random.Shared.Next(words.Length)];
        guessedWord = new string('_', chosenWord.Length).ToCharArray();
        guessedLetters.Clear();
        attemptsLeft = MaxMistakes;
        while (attemptsLeft > 0 && guessedWord.Contains('_'))
        {
            DrawHangman();
            Console.WriteLine($"Wort: {new string(guessedWord)}; übrig: {attemptsLeft}");
            Console.Write("Ein Buchstabe: ");
            string? input = Console.ReadLine()?.Trim();
            if (input is null) return;
            if (input.Length != 1 || !char.IsLetter(input[0]))
            {
                Console.WriteLine("Bitte genau einen Buchstaben eingeben.");
                continue;
            }
            char guess = char.ToLowerInvariant(input[0]);
            if (!guessedLetters.Add(guess))
            {
                Console.WriteLine("Dieser Buchstabe wurde bereits versucht.");
                continue;
            }
            if (chosenWord.Contains(guess))
            {
                for (int i = 0; i < chosenWord.Length; i++)
                    if (chosenWord[i] == guess) guessedWord[i] = guess;
            }
            else attemptsLeft--;
        }
        DrawHangman();
        Console.WriteLine($"{(attemptsLeft > 0 ? "Gewonnen" : "Verloren")}: {chosenWord}");
    }
    static void DrawHangman() => Console.WriteLine(stages[MaxMistakes - attemptsLeft]);
}
```

</details>

## Selbst prüfen

Verwende zunächst das feste Wort `computer`, bevor du die Zufallsauswahl einschaltest. Sieben falsche unterschiedliche Buchstaben (`a b f g h i j`) ergeben eine Niederlage ohne Absturz. `C` deckt `c` auf; ein zweites `c` kostet nichts. `1`, eine leere Zeile und `ab` kosten keinen Versuch. Mit `c o m p u t e r` gewinnst du.

Setze einen Haltepunkt in `DrawHangman()` und beobachte die Indizes `0–7`. Zusatz: Kategorien, mehrere Runden oder ein von einem zweiten Spieler eingegebenes Wort.
