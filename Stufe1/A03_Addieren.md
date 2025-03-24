# 🟢 Aufgabe A03: Addieren

## Ziel der Aufgabe

In dieser Aufgabe wirst du zwei Zahlen vom Benutzer einlesen, ihre **Summe berechnen** und auf der Konsole ausgeben.  
Dabei lernst du, wie man **Zahlen als Eingabe verarbeitet**, um damit **Rechnungen durchzuführen**.

---

## Was du lernst

- Wie man mit `Convert.ToDouble` Zahlen von der Konsole einliest
- Wie man zwei Werte addiert
- Wie man das Ergebnis formatiert ausgibt

---

## Schritt-für-Schritt-Anleitung

### 🔧 1. Projekt erstellen

1. Starte Visual Studio.
2. Klicke auf **„Neues Projekt erstellen“**.
3. Wähle **„Konsolenanwendung“** (C#) aus.
4. Projektname: z. B. `Addition`
5. Klicke auf **„Erstellen“**.

---

### 💻 2. Code eingeben

```csharp
using System;

class Program
{
    static void Main(string[] args)
    {
        Console.Write("Bitte gib die erste Zahl ein: ");
        double zahl1 = Convert.ToDouble(Console.ReadLine());

        Console.Write("Bitte gib die zweite Zahl ein: ");
        double zahl2 = Convert.ToDouble(Console.ReadLine());

        double summe = zahl1 + zahl2;

        Console.WriteLine($"Die Summe von {zahl1} und {zahl2} ist {summe}.");
    }
}
```

---

### ▶️ 3. Ausführen

- Drücke `F5` oder klicke auf **„Starten“**.
- Gib zwei Zahlen ein (z. B. 4 und 5,5).
- Du solltest sehen:  
  **Die Summe von 4 und 5,5 ist 9,5.**

---

## 🔍 Erklärt

| Code-Zeile | Bedeutung |
|-----------|-----------|
| `Convert.ToDouble(...)` | Wandelt die Eingabe (Text) in eine Zahl um |
| `zahl1 + zahl2` | Addiert beide Zahlen |
| `Console.WriteLine(...)` | Gibt das Ergebnis formatiert aus |

---

## 💡 Probiere selbst:

- Gib andere Werte ein: ganze Zahlen, Kommazahlen oder negative Zahlen.
- Tausche `double` gegen `int` aus – was passiert mit Kommazahlen?
- Baue eine Fehlerbehandlung ein:

```csharp
if (!double.TryParse(Console.ReadLine(), out double zahl))
{
    Console.WriteLine("Ungültige Eingabe!");
    return;
}
```

- Lasse den Benutzer in einer **Schleife** beliebig viele Zahlen eingeben und am Ende die Gesamtsumme anzeigen.

---

> 🧠 Diese Aufgabe ist ein wichtiger Baustein für alles, was mit Berechnungen zu tun hat. Du wirst das Prinzip bald für viele weitere Operationen nutzen!

