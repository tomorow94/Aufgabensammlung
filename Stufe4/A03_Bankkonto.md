# Aufgabe A03: Einfaches Bankkonto-System

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

## Erweiterungsmöglichkeiten

- **Mehrere Konten verwalten:** Lassen Sie den Benutzer mehrere Konten erstellen und auswählen.
- **Transaktionshistorie:** Speichern Sie alle Ein- und Auszahlungen und lassen Sie den Benutzer diese einsehen.
- **Zinsen berechnen:** Implementieren Sie eine Methode, die monatliche Zinsen auf das Guthaben anwendet.

---

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

    public void Deposit(decimal amount)
    {
        if (amount > 0)
        {
            Balance += amount;
            Console.WriteLine($"Deposited {amount:C}. New balance: {Balance:C}");
        }
        else
        {
            Console.WriteLine("Deposit amount must be positive.");
        }
    }

    public void Withdraw(decimal amount)
    {
        if (amount > 0 && amount <= Balance)
        {
            Balance -= amount;
            Console.WriteLine($"Withdrawn {amount:C}. New balance: {Balance:C}");
        }
        else
        {
            Console.WriteLine("Invalid withdrawal amount or insufficient funds.");
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
        string name = Console.ReadLine();
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

            switch (Console.ReadLine())
            {
                case "1":
                    Console.Write("Enter amount to deposit: ");
                    if (decimal.TryParse(Console.ReadLine(), out decimal depositAmount))
                    {
                        account.Deposit(depositAmount);
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
                        account.Withdraw(withdrawAmount);
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
