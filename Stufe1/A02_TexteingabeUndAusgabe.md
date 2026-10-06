# 🟢 Aufgabe A02: Texteingabe und -ausgabe

## Einordnung und Lernziele

**Status:** Pflicht im Lernfaden.

**Voraussetzungen:** [Hallo Welt](A01_HalloWelt.md)

**Intention:** Eine eingegebene Zeichenkette in einer Ausgabe wiederverwenden.

**Lernziele:**

- Du kannst einen Text einlesen, speichern und in eine Begrüßung einsetzen.
- Du kannst leere Eingabe und das Ende des Eingabestroms unterscheiden.

**Weiter im Pflichtpfad:** [Addieren](A03_Addieren.md)

## Ziel der Aufgabe

Du schreibst ein Programm, das eine **Benutzereingabe** abfragt und sie verwendet, um eine **personalisierte Begrüßung** auszugeben.
Diese Aufgabe zeigt dir, wie du Eingaben über die Konsole entgegennehmen und weiterverarbeiten kannst.

---

## Was du lernst

- Wie man Texte in C# einliest (`Console.ReadLine()`)
- Wie man Benutzereingaben speichert und ausgibt
- Wie man mit **Zeichenketten-Interpolation** arbeitet

---

## Gestufte Hinweise

Versuche zuerst eine eigene Lösung. Öffne bei Bedarf zunächst Hinweis 1 und erst danach Hinweis 2; die vorhandenen Beispiele bzw. Referenzen dienen anschließend zum Vergleichen.

<details>
<summary>Hinweis 1: Denkanstoß</summary>

Welche Information muss zwischen Eingabe und Ausgabe erhalten bleiben?

</details>

<details>
<summary>Hinweis 2: Vorgehensweise</summary>

Speichere ReadLine in einer Variablen; prüfe vor der Verarbeitung, ob die Eingabe null oder leer ist.

</details>

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
        string? name = Console.ReadLine();
        if (name is null) return;
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

## Weiterüben im Pflichtpfad

- Ändere die Begrüßung in einen anderen Satz.
- Füge eine zweite Frage hinzu (z. B. Alter) und gib diese auch aus:
  ```csharp
  Console.Write("Wie alt bist du? ");
  string alter = Console.ReadLine() ?? "";
  Console.WriteLine($"Du bist {alter} Jahre alt.");
  ```


## Selbst prüfen

`Anna` ergibt die Begrüßung mit Anna. Prüfe auch eine leere Eingabe, mehrere Leerzeichen und das Ende des Eingabestroms. Das Einstiegsbeispiel gibt für einen leeren Namen `Hallo, !` aus und beendet sich beim Ende des Eingabestroms. Beobachte `name` im Debugger.

**Bonus-Prüfung nach A06:** Die Erweiterung fragt bei einer leeren Eingabe erneut nach und beendet sich bei einem geschlossenen Eingabestrom.

## Bonus: Eingabe wiederholen (nach A06)

**Intention:** Erprobe später eine wiederholte Nachfrage.

**Lernziel:** Nach A06 kannst du eine leere Eingabe mit einer while-Schleife erneut abfragen.

- Sorge dafür, dass leere Eingaben nicht akzeptiert werden:
  ```csharp
  while (string.IsNullOrWhiteSpace(name))
  {
      Console.Write("Name darf nicht leer sein. Bitte erneut eingeben: ");
      name = Console.ReadLine();
      if (name is null) return;
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
        string? name = Console.ReadLine();
        if (name is null) return;

        while (string.IsNullOrWhiteSpace(name))
        {
            Console.Write("Name darf nicht leer sein. Bitte erneut eingeben: ");
            name = Console.ReadLine();
      if (name is null) return;
        }

        Console.WriteLine($"Hallo, {name}!");
    }
}
```

</details>

---

> 🧠 Mit dieser Aufgabe verstehst du, wie Programme mit dem Benutzer "sprechen". Du wirst das bald für Menüführung, Formulare und Spielsteuerung brauchen!

## Passende Lernquellen

[Leseempfehlung für diesen Lernschritt](../Referenzen/Lernquellen.md#stufe-1-eingaben-und-ablauf). Wähle den dort genannten Abschnitt zur aktuellen Aufgabe und probiere ihn in deinem eigenen Programm aus.
