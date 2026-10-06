# Aufgabe A01: Tic Tac Toe – Einführung in Spielmechaniken, Arrays und Entscheidungslogik

## Einordnung und Lernziele

**Status:** Pflicht im Lernfaden.

**Voraussetzungen:** [Bestehenden Code schrittweise verbessern](../Stufe3/A05_Refactoring.md)

**Intention:** Ein Spiel durch Spielfeld, gültige Aktionen und Zustandsübergänge modellieren.

**Lernziele:**

- Du kannst ein zweidimensionales Brett und alle Gewinnlinien prüfen.
- Du kannst einen ungültigen Zug ohne Zustandsänderung behandeln.

**Weiter im Pflichtpfad:** [Hangman](A02_Hangman.md)

## Ziel

In dieser Aufgabe entwickeln Sie das klassische Spiel **Tic Tac Toe** als Konsolenanwendung in C#.  
Dabei lernen Sie:
- **Spiellogik** für ein rundenbasiertes Spiel zu erstellen.
- **Arrays** zur Speicherung des Spielfelds zu nutzen.
- **Benutzereingaben** zu verarbeiten und zu überprüfen.

---

## Anforderungen

1. **Spielfeld als Array verwalten**
   - Erstellen Sie ein **3x3-Array (`char[,] board`)**, das das Spielfeld repräsentiert.
   - Die Felder sollen mit `X`, `O` oder einer Zahl (Platzhalter für freie Felder) belegt sein.

2. **Spielerwechsel und Eingaben**
   - Zwei Spieler (`X` und `O`) spielen abwechselnd.
   - Der aktuelle Spieler gibt eine Zahl ein (1-9), um ein Feld zu wählen.
   - Das Programm prüft, ob das gewählte Feld frei ist.

3. **Gewinnlogik implementieren**
   - Das Spiel erkennt automatisch, wenn ein Spieler drei gleiche Symbole in einer Reihe, Spalte oder Diagonale hat.
   - Falls kein Feld mehr frei ist und kein Spieler gewonnen hat, endet das Spiel als Unentschieden.

4. **Spielablauf und Benutzerführung**
   - Das Spielfeld wird nach jedem Zug aktualisiert und angezeigt.
   - Falls eine ungültige Eingabe erfolgt (z. B. ein belegtes Feld), wird eine Fehlermeldung ausgegeben.
   - Nach Spielende wird der Gewinner oder ein Unentschieden ausgegeben.

---

## Hinweise

- Nutzen Sie eine **Schleife**, um das Spiel so lange laufen zu lassen, bis es beendet ist.
- Verwenden Sie **Methoden**, um wiederkehrende Abläufe (z. B. Spielfeld anzeigen, Eingabe prüfen) auszulagern.
- Denken Sie an eine **saubere Struktur**, um den Code später erweitern zu können.

---

## Gestufte Hinweise

Versuche zuerst eine eigene Lösung. Öffne bei Bedarf zunächst Hinweis 1 und erst danach Hinweis 2; die vorhandenen Beispiele bzw. Referenzen dienen anschließend zum Vergleichen.

<details>
<summary>Hinweis 1: Denkanstoß</summary>

Welche Bedingungen müssen vor einem Spielerwechsel erfüllt sein?

</details>

<details>
<summary>Hinweis 2: Vorgehensweise</summary>

Prüfe Bereich und freies Feld, setze dann den Zug; prüfe Sieg und Unentschieden vor dem Wechsel.

</details>

<details>
<summary><strong>Lösungsvorschlag anzeigen</strong></summary>

```csharp
using System;

class TicTacToe
{
    static char[,] board = { { '1', '2', '3' }, { '4', '5', '6' }, { '7', '8', '9' } };
    static char currentPlayer = 'X';

    static void Main()
    {
        int turns = 0;
        bool gameRunning = true;

        while (gameRunning)
        {
            PrintBoard();
            Console.Write($"\nPlayer {currentPlayer}, choose a field (1-9): ");
            
            string? input = Console.ReadLine();
            if (input is null) return;
            if (int.TryParse(input, out int choice) && choice >= 1 && choice <= 9)
            {
                int row = (choice - 1) / 3;
                int col = (choice - 1) % 3;

                if (board[row, col] != 'X' && board[row, col] != 'O')
                {
                    board[row, col] = currentPlayer;
                    turns++;

                    if (CheckWin())
                    {
                        PrintBoard();
                        Console.WriteLine($"\nPlayer {currentPlayer} wins!");
                        gameRunning = false;
                    }
                    else if (turns == 9)
                    {
                        PrintBoard();
                        Console.WriteLine("\nIt's a draw!");
                        gameRunning = false;
                    }
                    else
                    {
                        currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
                    }
                }
                else
                {
                    Console.WriteLine("Field is already occupied. Try again.");
                }
            }
            else
            {
                Console.WriteLine("Invalid input. Choose a number between 1 and 9.");
            }
        }
    }

    static void PrintBoard()
    {
        Console.WriteLine("\nTic Tac Toe Board:");
        for (int i = 0; i < 3; i++)
        {
            Console.WriteLine($" {board[i, 0]} | {board[i, 1]} | {board[i, 2]} ");
            if (i < 2) Console.WriteLine("---+---+---");
        }
    }

    static bool CheckWin()
    {
        for (int i = 0; i < 3; i++)
        {
            if ((board[i, 0] == board[i, 1] && board[i, 1] == board[i, 2]) || 
                (board[0, i] == board[1, i] && board[1, i] == board[2, i]))
                return true;
        }

        if ((board[0, 0] == board[1, 1] && board[1, 1] == board[2, 2]) || 
            (board[0, 2] == board[1, 1] && board[1, 1] == board[2, 0]))
            return true;

        return false;
    }
}
```

</details>



## Selbst prüfen

Züge `1,4,2,5,3` ergeben einen Sieg für X. `1,2,3,5,4,6,8,7,9` ergeben ein Unentschieden. Ein belegtes Feld und Zahlen außerhalb 1–9 ändern weder das Brett noch den Spieler. Prüfe alle acht Gewinnlinien und dass Fehlermeldungen vor der nächsten Eingabe sichtbar bleiben.

## Bonus: Spielvarianten

**Intention:** Verändere ein funktionierendes Spiel in abgegrenzten Schritten.

**Lernziel:** Du kannst mehrere Runden zurücksetzen oder einen Computerzug erzeugen, ohne die Prüfung gültiger Züge zu umgehen.


- **Computergegner (KI)**: Implementieren Sie eine einfache KI, die zufällig oder strategisch zieht.
- **Mehrere Runden**: Ermöglichen Sie es den Spielern, nach Spielende erneut zu spielen.
- **Erweiterte Darstellung**: Nutzen Sie ASCII-Grafiken für ein optisch ansprechenderes Spielfeld.

---

## Passende Lernquellen

[Leseempfehlung für diesen Lernschritt](../Referenzen/Lernquellen.md#stufe-4-zustand-und-geschäftsregeln). Wähle den dort genannten Abschnitt zur aktuellen Aufgabe und probiere ihn in deinem eigenen Programm aus.
