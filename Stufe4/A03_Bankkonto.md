# Aufgabe A03: Einfaches Bankkonto-System

## Einordnung und Lernziele

**Status:** Pflicht im Lernfaden.

**Voraussetzungen:** [Hangman](A02_Hangman.md)

**Intention:** Geschäftsregeln innerhalb einer Klasse schützen.

**Lernziele:**

- Du kannst Ein- und Auszahlungen über Methoden mit Erfolgswert steuern.
- Du kannst negative Beträge und Überziehung abweisen, ohne den Kontostand zu verändern.

**Weiter im Pflichtpfad:** [Sortieralgorithmen fair vergleichen](../Stufe5/A01_Sortieralgorithmen.md)

## Ziel

In dieser Aufgabe entwickeln Sie ein **einfaches Bankkonto-System** als Konsolenanwendung in C#.  
Dabei lernen Sie:
- **Objektorientierte Programmierung (OOP)** durch die Modellierung eines Bankkontos.
- **Datenkapselung** durch den Einsatz von **`private`** und **`public`** Zugriffsmodifikatoren.
- **Methoden für Kontoverwaltung**, um Einzahlungen und Abhebungen durchzuführen.

---

## Anforderungen

1. **Klasse `BankAccount` erstellen**
   - Die Klasse benötigt die folgenden Attribute:
     - `AccountHolder` (string) – Name des Kontoinhabers.
     - `Balance` (decimal) – Der aktuelle Kontostand.
     - `AccountNumber` (string) – Eine eindeutige Kontonummer (generiert).
   - Implementieren Sie Methoden:
     - `Deposit(decimal amount)`: Fügt Guthaben zum Konto hinzu.
     - `Withdraw(decimal amount)`: Hebt Guthaben ab, falls genügend Guthaben vorhanden ist.
     - `ShowBalance()`: Zeigt den aktuellen Kontostand an.

2. **Benutzermenü zur Kontoverwaltung**
   - Der Benutzer soll ein **Konto erstellen** können.
   - Danach kann er zwischen folgenden Aktionen wählen:
     - Geld einzahlen
     - Geld abheben
     - Kontostand anzeigen
     - Programm beenden

3. **Eingabevalidierung**
   - Es soll sichergestellt werden, dass keine negativen Beträge eingezahlt oder abgehoben werden.
   - Das Konto darf nicht ins **Minus** fallen.

---

## Hinweise

- Nutzen Sie einen **Konstruktor**, um das Konto zu initialisieren.
- Verwenden Sie **`decimal`** statt `double`, da `decimal` besser für Finanzwerte geeignet ist.
- Erstellen Sie eine Methode zur **Generierung einer Kontonummer** (z. B. zufällig oder fortlaufend).

---

## Gestufte Hinweise

Versuche zuerst eine eigene Lösung. Öffne bei Bedarf zunächst Hinweis 1 und erst danach Hinweis 2; die vorhandenen Beispiele bzw. Referenzen dienen anschließend zum Vergleichen.

<details>
<summary>Hinweis 1: Denkanstoß</summary>

Welche Änderung darf nur nach bestandener Prüfung stattfinden?

</details>

<details>
<summary>Hinweis 2: Vorgehensweise</summary>

Der Kontostand wird gekapselt; prüfe Betrag und Deckung vor der Mutation und liefere dem Menü einen Erfolgswert.

</details>

<details>
<summary><strong>Lösungsvorschlag anzeigen</strong></summary>

```csharp
using System;

class BankAccount
{
    public string AccountHolder { get; }
    public decimal Balance { get; private set; }
    public string AccountNumber { get; }

    private static int accountCounter = 1000;

    public BankAccount(string holder)
    {
        AccountHolder = holder;
        AccountNumber = "BA" + accountCounter++;
        Balance = 0m;
    }

    public bool Deposit(decimal amount)
    {
        if (amount > 0 && amount <= decimal.MaxValue - Balance)
        {
            Balance += amount;
            return true;
        }
        else
        {
            return false;
        }
    }

    public bool Withdraw(decimal amount)
    {
        if (amount > 0 && amount <= Balance)
        {
            Balance -= amount;
            return true;
        }
        else
        {
            return false;
        }
    }

    public void ShowBalance()
    {
        Console.WriteLine($"Account Holder: {AccountHolder}");
        Console.WriteLine($"Account Number: {AccountNumber}");
        Console.WriteLine($"Current Balance: {Balance:C}");
    }
}

class Program
{
    static void Main()
    {
        Console.Write("Enter account holder name: ");
        string name = Console.ReadLine() ?? "";
        BankAccount account = new BankAccount(name);

        bool running = true;
        while (running)
        {
            Console.WriteLine("\n===== Bank Account Menu =====");
            Console.WriteLine("1. Deposit Money");
            Console.WriteLine("2. Withdraw Money");
            Console.WriteLine("3. Show Balance");
            Console.WriteLine("4. Exit");
            Console.Write("Select an option: ");

            string? choice = Console.ReadLine();
            if (choice is null) return;
            switch (choice)
            {
                case "1":
                    Console.Write("Enter amount to deposit: ");
                    if (decimal.TryParse(Console.ReadLine(), out decimal depositAmount))
                    {
                        Console.WriteLine(account.Deposit(depositAmount) ? "Deposit successful." : "Invalid deposit.");
                    }
                    else
                    {
                        Console.WriteLine("Invalid amount.");
                    }
                    break;
                case "2":
                    Console.Write("Enter amount to withdraw: ");
                    if (decimal.TryParse(Console.ReadLine(), out decimal withdrawAmount))
                    {
                        Console.WriteLine(account.Withdraw(withdrawAmount) ? "Withdrawal successful." : "Invalid amount or insufficient funds.");
                    }
                    else
                    {
                        Console.WriteLine("Invalid amount.");
                    }
                    break;
                case "3":
                    account.ShowBalance();
                    break;
                case "4":
                    running = false;
                    Console.WriteLine("Exiting program...");
                    break;
                default:
                    Console.WriteLine("Invalid choice. Please try again.");
                    break;
            }
        }
    }
}
```

</details>

## Selbst prüfen: Geschäftslogik

`Deposit` und `Withdraw` geben einen Erfolgswert zurück; das Menü erzeugt die Meldung. Prüfe mit einem frischen Konto: Einzahlung `100` ergibt `100`, Einzahlung `-1` und `0` ändern nichts, Abhebung `101` ändert nichts, Abhebung `100` ergibt `0`. Eine weitere Abhebung wird abgewiesen. Die Kontonummer ist nur innerhalb dieses laufenden Beispiels eindeutig; für dauerhaft gespeicherte Konten benötigst du eine dauerhafte ID-Vergabe.

## Bonus: Mehrere Konten und Historie

**Intention:** Wende Kapselung auf zusätzliche Konten und dokumentierte Vorgänge an.

**Lernziel:** Du kannst Transaktionen zuordnen und mehrere Konten verwalten, ohne den Kontostand direkt von außen zu setzen.


- **Mehrere Konten verwalten:** Lassen Sie den Benutzer mehrere Konten erstellen und auswählen.
- **Transaktionshistorie:** Speichern Sie alle Ein- und Auszahlungen und lassen Sie den Benutzer diese einsehen.
- **Zinsen berechnen:** Implementieren Sie eine Methode, die monatliche Zinsen auf das Guthaben anwendet.

---

## Bonus: Frühe Kontotests

**Intention:** Automatisiere bestehende Geschäftsregeln als Vorgriff auf Stufe 6.

**Lernziel:** Du kannst Kontostand und Erfolgswert in xUnit prüfen; die Testeinrichtung ist hier optional.

Lege schon jetzt ein xUnit-Projekt an (`dotnet new xunit -n BankAccount.Tests --framework net10.0`), referenziere das Konto-Projekt und automatisiere diese Fälle. Teste den Erfolgswert und den Kontostand, ohne Konsolenausgaben abzufangen. Stufe 6 erklärt das Vorgehen ausführlicher.

## Passende Lernquellen

[Leseempfehlung für diesen Lernschritt](../Referenzen/Lernquellen.md#stufe-4-zustand-und-geschäftsregeln). Wähle den dort genannten Abschnitt zur aktuellen Aufgabe und probiere ihn in deinem eigenen Programm aus.
