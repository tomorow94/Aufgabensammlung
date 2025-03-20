# Aufgabe A02: Hangman (Galgenmännchen)

## Ziel

In dieser Aufgabe entwickeln Sie das klassische Spiel **Hangman (Galgenmännchen)** als Konsolenanwendung in C#.  
Dabei lernen Sie:
- **Zeichenkettenmanipulation** zur Darstellung des gesuchten Wortes.
- **Benutzereingaben zu verarbeiten und zu prüfen**.
- **Spielmechaniken**, wie das Zeichnen des Hängemännchens und das Verwalten von Versuchen.

---

## Anforderungen

1. **Wortauswahl und Darstellung**
   - Das Programm wählt ein zufälliges Wort aus einer **Liste von Wörtern**.
   - Das Wort wird als eine Reihe von **`_` (Unterstrichen)** dargestellt, wobei nur erratene Buchstaben sichtbar sind.

2. **Benutzereingaben verarbeiten**
   - Der Spieler gibt **einen Buchstaben pro Versuch** ein.
   - Falls der Buchstabe im Wort enthalten ist, wird er an den richtigen Stellen angezeigt.
   - Falls nicht, wird das Hängemännchen **schrittweise aufgebaut**.

3. **Spielregeln**
   - Der Spieler hat **maximal 7 Fehlversuche**, bevor das Spiel verloren ist.
   - Das Spiel endet, wenn:
     - Der Spieler das Wort vollständig erraten hat → **Gewonnen**.
     - Der Spieler alle Versuche aufgebraucht hat → **Verloren**.

4. **Visualisierung des Hängemännchens**
   - Verwenden Sie eine einfache **ASCII-Grafik**, um den Fortschritt des Spiels anzuzeigen.
   - Nach jedem falschen Versuch wird ein weiterer Teil des Galgens gezeichnet.

---

## Hinweise

- Nutzen Sie eine **Liste oder ein Array**, um mehrere Wörter zur Auswahl zu haben.
- Verwenden Sie **Schleifen und Methoden**, um den Code übersichtlich zu halten.
- Implementieren Sie eine **Methode, die das Hängemännchen je nach Anzahl der Fehlversuche anzeigt**.

---

## Erweiterungsmöglichkeiten

- **Mehrspieler-Modus:** Ein Spieler gibt ein Wort ein, das der andere erraten muss.
- **Themenbezogene Wörter:** Lassen Sie den Spieler zwischen Kategorien wie „Tiere“, „Länder“ oder „Technologie“ wählen.
- **Grafische Oberfläche:** Erstellen Sie eine einfache GUI mit **Windows Forms oder WPF**.

---

<details>
<summary><strong>Lösungsvorschlag anzeigen</strong></summary>

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

class Hangman
{
    static string[] words = { "computer", "programming", "developer", "software", "keyboard" };
    static string chosenWord;
    static char[] guessedWord;
    static List<char> guessedLetters = new List<char>();
    static int attemptsLeft = 7;

    static void Main()
    {
        Random rand = new Random();
        chosenWord = words[rand.Next(words.Length)];
        guessedWord = new string('_', chosenWord.Length).ToCharArray();

        while (attemptsLeft > 0 && guessedWord.Contains('_'))
        {
            Console.Clear();
            DrawHangman();
            Console.WriteLine($"\nWord: {new string(guessedWord)}");
            Console.WriteLine($"Attempts left: {attemptsLeft}");
            Console.Write("Guess a letter: ");

            char guess = Console.ReadKey().KeyChar;
            Console.WriteLine();

            if (guessedLetters.Contains(guess))
            {
                Console.WriteLine("You already guessed this letter. Try again.");
                continue;
            }

            guessedLetters.Add(guess);

            if (chosenWord.Contains(guess))
            {
                for (int i = 0; i < chosenWord.Length; i++)
                {
                    if (chosenWord[i] == guess)
                    {
                        guessedWord[i] = guess;
                    }
                }
            }
            else
            {
                attemptsLeft--;
            }
        }

        Console.Clear();
        DrawHangman();
        Console.WriteLine($"\nWord: {chosenWord}");

        if (attemptsLeft > 0)
        {
            Console.WriteLine("Congratulations! You won!");
        }
        else
        {
            Console.WriteLine("Game over! You lost.");
        }
    }

    static void DrawHangman()
    {
        string[] hangmanStages = {
            "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n=========",
        };

        Console.WriteLine(hangmanStages[7 - attemptsLeft]);
    }
}
```

</details> 
