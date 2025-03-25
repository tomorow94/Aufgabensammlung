# 🟢 Aufgabe A04: Subtraktion

## Ziel der Aufgabe

Dieses Programm liest zwei Zahlen ein und berechnet ihre **Differenz** (erste minus zweite Zahl).  
Du lernst dabei, wie du einfache mathematische Operationen mit Benutzereingaben kombinierst.

---

## Was du lernst

- Wie man Eingaben als `double` einliest
- Wie man eine Subtraktion durchführt
- Wie man das Ergebnis ausgibt

---

## Schritt-für-Schritt-Anleitung

### 🔧 1. Projekt erstellen

1. Starte Visual Studio.
2. Erstelle ein neues Projekt vom Typ **Konsolenanwendung**.
3. Projektname: z. B. `Subtraktion`

---

### 💻 2. Code eingeben

```csharp
using System;

class Program
{
    static void Main(string[] args)
    {
        Console.Write("Erste Zahl: ");
        double a = Convert.ToDouble(Console.ReadLine());

        Console.Write("Zweite Zahl: ");
        double b = Convert.ToDouble(Console.ReadLine());

        double differenz = a - b;

        Console.WriteLine($"{a} minus {b} ergibt {differenz}.");
    }
}
```

---

### ▶️ 3. Ausführen

- Starte das Programm mit `F5`.
- Gib z. B. `10` und `4` ein.
- Erwartete Ausgabe: `10 minus 4 ergibt 6.`

---

## 🔍 Erklärt

| Code-Zeile | Bedeutung |
|-----------|-----------|
| `a - b` | Subtrahiert zwei Zahlen |
| `Convert.ToDouble(...)` | Wandelt Eingabe-Text in Zahl um |

---

## 💡 Probiere selbst:

- Was passiert, wenn du zuerst eine kleinere und dann eine größere Zahl eingibst?
- Kannst du die Reihenfolge umkehren (zweite minus erste)?
- Baue eine Wiederholung mit Schleife ein, z. B. um mehrfach zu rechnen.

---

> 🧠 Diese Aufgabe zeigt dir: Rechnen mit Benutzereingaben ist einfach – und du kannst mit jeder neuen Rechenart dein Programm erweitern!

