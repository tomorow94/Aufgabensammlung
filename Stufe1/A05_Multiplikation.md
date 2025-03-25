# 🟢 Aufgabe A05: Multiplikation

## Ziel der Aufgabe

Dieses Programm liest zwei Zahlen ein und berechnet ihr **Produkt** (also die Multiplikation).  
Du lernst, wie man zwei Zahlen miteinander multipliziert und das Ergebnis auf der Konsole ausgibt.

---

## Was du lernst

- Wie man Benutzereingaben verarbeitet
- Wie man zwei Zahlen multipliziert
- Wie man Ergebnisse formatiert ausgibt

---

## Schritt-für-Schritt-Anleitung

### 🔧 1. Projekt erstellen

1. Starte Visual Studio.
2. Neues Projekt: **Konsolenanwendung (C#)**.
3. Projektname: z. B. `Multiplikation`

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

        double produkt = a * b;

        Console.WriteLine($"{a} mal {b} ergibt {produkt}.");
    }
}
```

---

### ▶️ 3. Ausführen

- Starte das Programm mit `F5`.
- Gib z. B. `3` und `4` ein.
- Ausgabe: `3 mal 4 ergibt 12.`

---

## 🔍 Erklärt

| Code-Zeile | Bedeutung |
|-----------|-----------|
| `a * b` | Multipliziert zwei Zahlen |
| `Console.WriteLine(...)` | Gibt das Ergebnis formatiert aus |

---

## 💡 Probiere selbst:

- Was passiert mit negativen Zahlen?
- Was passiert, wenn eine Zahl 0 ist?
- Was passiert bei Kommazahlen?

---

> 🧠 Die Multiplikation ist die nächste Grundoperation – mit wenigen Änderungen kannst du bald auch Rechenmaschinen oder Taschenrechner bauen!

