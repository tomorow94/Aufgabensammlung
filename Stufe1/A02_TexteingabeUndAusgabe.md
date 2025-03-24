# 🟢 Aufgabe A02: Texteingabe und -ausgabe

## Ziel der Aufgabe

Du schreibst ein Programm, das eine **Benutzereingabe** abfragt und sie verwendet, um eine **personalisierte Begrüßung** auszugeben.
Diese Aufgabe zeigt dir, wie du Eingaben über die Konsole entgegennehmen und weiterverarbeiten kannst.

---

## Was du lernst

- Wie man Texte in C# einliest (`Console.ReadLine()`)
- Wie man Benutzereingaben speichert und ausgibt
- Wie man mit **Zeichenketten-Interpolation** arbeitet

---

## Schritt-für-Schritt-Anleitung

### 🔧 1. Projekt erstellen

1. Starte Visual Studio.
2. Klicke auf **„Neues Projekt erstellen“**.
3. Wähle **„Konsolenanwendung“** (C#) aus.
4. Projektname: z. B. `TexteingabeAusgabe`
5. Klicke auf **„Erstellen“**.

---

### 💻 2. Code eingeben

```csharp
using System;

class Program
{
    static void Main(string[] args)
    {
        Console.Write("Bitte gib deinen Namen ein: ");
        string name = Console.ReadLine();
        Console.WriteLine($"Hallo, {name}!");
    }
}
```

---

### ▶️ 3. Ausführen

- Drücke `F5` oder klicke auf **„Starten“**.
- Gib im Konsolenfenster deinen Namen ein.
- Du solltest sehen:  
  **Hallo, [dein Name]!**

---

## 🔍 Erklärt

| Code-Zeile | Bedeutung |
|-----------|-----------|
| `Console.Write(...)` | Gibt eine Zeile ohne Zeilenumbruch aus |
| `Console.ReadLine()` | Liest die Eingabe von der Tastatur ein |
| `$"Hallo, {name}!"` | Fügt den Wert der Variable `name` in den Text ein |

---

## 💡 Probiere selbst:

- Ändere die Begrüßung in einen anderen Satz.
- Füge eine zweite Frage hinzu (z. B. Alter) und gib diese auch aus:
  ```csharp
  Console.Write("Wie alt bist du? ");
  string alter = Console.ReadLine();
  Console.WriteLine($"Du bist {alter} Jahre alt.");
  ```

- Sorge dafür, dass leere Eingaben nicht akzeptiert werden:
  ```csharp
  while (string.IsNullOrWhiteSpace(name))
  {
      Console.Write("Name darf nicht leer sein. Bitte erneut eingeben: ");
      name = Console.ReadLine();
  }
  ```

---

<details>
<summary>💬 Lösungsvorschlag</summary>

```csharp
using System;

class Program
{
    static void Main(string[] args)
    {
        Console.Write("Bitte gib deinen Namen ein: ");
        string name = Console.ReadLine();

        while (string.IsNullOrWhiteSpace(name))
        {
            Console.Write("Name darf nicht leer sein. Bitte erneut eingeben: ");
            name = Console.ReadLine();
        }

        Console.WriteLine($"Hallo, {name}!");
    }
}
```

</details>

---

> 🧠 Mit dieser Aufgabe verstehst du, wie Programme mit dem Benutzer "sprechen". Du wirst das bald für Menüführung, Formulare und Spielsteuerung brauchen!

