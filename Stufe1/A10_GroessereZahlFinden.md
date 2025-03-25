# 🟢 Aufgabe A10: Größere Zahl finden

## Ziel der Aufgabe

In dieser Aufgabe schreibst du ein Programm, das **zwei Zahlen vergleicht** und angibt, welche **größer** ist. Es zeigt dir, wie man **Benutzereingaben**, **Vergleichsoperatoren** und einfache **Verzweigungen** mit `if-else` verwendet.

---

## Was du lernst

- Wie man Benutzereingaben als Zahlen verarbeitet
- Wie man zwei Zahlen miteinander vergleicht
- Wie man mit Bedingungen unterschiedliche Ergebnisse erzeugt

---

## Schritt-für-Schritt-Anleitung

### 🔧 1. Projekt erstellen

1. Starte Visual Studio.
2. Neues Projekt: **Konsolenanwendung (C#)**
3. Projektname: z. B. `GroessereZahlFinden`

---

### 💻 2. Code eingeben

```csharp
using System;

class Program
{
    static void Main(string[] args)
    {
        try
        {
            Console.Write("Erste Zahl: ");
            double zahl1 = Convert.ToDouble(Console.ReadLine());

            Console.Write("Zweite Zahl: ");
            double zahl2 = Convert.ToDouble(Console.ReadLine());

            if (zahl1 > zahl2)
            {
                Console.WriteLine($"Die größere Zahl ist: {zahl1}");
            }
            else if (zahl2 > zahl1)
            {
                Console.WriteLine($"Die größere Zahl ist: {zahl2}");
            }
            else
            {
                Console.WriteLine("Beide Zahlen sind gleich groß.");
            }
        }
        catch (FormatException)
        {
            Console.WriteLine("Ungültige Eingabe! Bitte eine Zahl eingeben.");
        }
    }
}
```

---

### ▶️ 3. Ausführen

- Starte das Programm mit `F5`
- Gib zwei Zahlen ein
- Das Programm zeigt dir an, welche Zahl größer ist oder ob beide gleich sind

---

## 🔍 Erklärt

| Konzept             | Beschreibung |
|---------------------|--------------|
| `Convert.ToDouble`  | Wandelt Texteingabe in eine Gleitkommazahl um |
| `if`, `else if`, `else` | Vergleicht die beiden Zahlen und reagiert entsprechend |
| `try-catch`         | Behandelt Fehler wie Buchstaben statt Zahlen |

---

## 💡 Probiere selbst

- Erweitere das Programm, sodass es **drei oder mehr Zahlen** vergleicht
- Baue eine Methode `Max(double a, double b)`, die die größere Zahl zurückgibt
- Erlaube auch **negative Zahlen** oder **dezimale Eingaben** (z. B. 3,14)
- Lässt sich das Programm auch mit einem `switch` umsetzen?

---

> 🧠 Diese Aufgabe ist ideal, um erste Entscheidungen in deinem Code zu treffen. Du übst den Umgang mit Benutzereingaben und Bedingungen auf eine einfache, praktische Art.

