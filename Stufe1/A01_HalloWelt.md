# 🟢 Aufgabe A01: Hallo Welt

## Ziel der Aufgabe

Diese Aufgabe soll dir zeigen, wie einfach es ist, ein Programm in C# zu schreiben – und auszuführen.  
Das Ziel: Du drückst `F5` – und siehst deine erste Nachricht im Konsolenfenster. 🎉

---

## Was du lernst

- Wie man ein neues Konsolenprogramm in Visual Studio anlegt
- Wie man mit `Console.WriteLine()` eine Ausgabe erzeugt
- Wie ein einfaches C#-Programm aufgebaut ist

---

## Schritt-für-Schritt-Anleitung

### 🔧 1. Projekt erstellen

1. Starte Visual Studio.
2. Klicke auf **„Neues Projekt erstellen“**.
3. Wähle **„Konsolenanwendung“** (C#) aus.
4. Gib dem Projekt einen Namen, z. B. `HalloWelt`.
5. Klicke auf **„Erstellen“**.

---

### 💻 2. Code eingeben

Ersetze den Beispielcode im Editor durch diesen Code:

```csharp
using System;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Hallo Welt!");
    }
}
```

---

### ▶️ 3. Ausführen

- Drücke `F5` oder klicke auf **„Starten“**.
- Ein Konsolenfenster öffnet sich.
- Du solltest die Ausgabe sehen:  
  **Hallo Welt!**

---

## 🔍 Erklärt

| Code-Zeile | Bedeutung |
|-----------|-----------|
| `using System;` | Importiert das System-Namensraum für Konsolenfunktionen |
| `class Program` | Definiert eine Klasse namens `Program` |
| `static void Main(...)` | Einstiegspunkt – hier beginnt das Programm |
| `Console.WriteLine(...)` | Gibt Text auf der Konsole aus |

---

## 💡 Probiere selbst:

- Ändere den Text in `Console.WriteLine` auf deinen eigenen Namen.
- Füge eine zweite Zeile hinzu, z. B.:  
  `Console.WriteLine("Schön, dass du programmierst!");`

---

<details>
<summary>💬 Lösungsvorschlag</summary>

```csharp
using System;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Hallo Welt!");
        Console.WriteLine("Schön, dass du programmierst!");
    }
}
```

</details>

---

> 🧠 Diese Aufgabe ist der perfekte Einstieg, weil du sofort etwas siehst und ausprobierst. Keine Theorie, kein Ballast – einfach machen. 😊


## Selbst prüfen

Ändere die Ausgabe, füge eine zweite Zeile hinzu und überprüfe die Reihenfolge. Setze einen Haltepunkt vor `WriteLine` und führe mit F10 jeweils eine Anweisung aus.
