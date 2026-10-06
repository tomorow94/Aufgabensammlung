# 🟢 Aufgabe A04: Größere Zahl finden

## Einordnung und Lernziele

**Status:** Pflicht im Lernfaden.

**Voraussetzungen:** [Addieren](A03_Addieren.md)

**Intention:** Den Programmablauf von einem Vergleich abhängig machen.

**Lernziele:**

- Du kannst mit if/else zwei Zahlen vergleichen.
- Du kannst die Fälle kleiner, größer und gleich getrennt prüfen.

**Weiter im Pflichtpfad:** [Subtraktion und sichere Zahleneingabe](A05_Subtraktion.md)

## Ziel der Aufgabe

In dieser Aufgabe schreibst du ein Programm, das **zwei Zahlen vergleicht** und angibt, welche **größer** ist. Es zeigt dir, wie man **Benutzereingaben**, **Vergleichsoperatoren** und einfache **Verzweigungen** mit `if-else` verwendet.

---

## Was du lernst

- Wie man Benutzereingaben als Zahlen verarbeitet
- Wie man zwei Zahlen miteinander vergleicht
- Wie man mit Bedingungen unterschiedliche Ergebnisse erzeugt

---

## Gestufte Hinweise

Versuche zuerst eine eigene Lösung. Öffne bei Bedarf zunächst Hinweis 1 und erst danach Hinweis 2; die vorhandenen Beispiele bzw. Referenzen dienen anschließend zum Vergleichen.

<details>
<summary>Hinweis 1: Denkanstoß</summary>

Wie viele unterschiedliche Ergebnisse kann der Vergleich zweier Zahlen haben?

</details>

<details>
<summary>Hinweis 2: Vorgehensweise</summary>

Prüfe zuerst a > b, dann a < b; im verbleibenden Fall sind die Werte gleich.

</details>

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

## Selbst prüfen

`2` und `3` ergeben `3`, `3` und `2` ebenfalls `3`, `2` und `2` die Gleichheitsmeldung. `-3` und `-2` ergeben `-2`; negative und dezimale Zahlen werden bereits akzeptiert. `abc` ergibt eine Meldung. Beobachte im Debugger, welcher `if`-Zweig gewählt wird.

## Bonus: Mehrere Zahlen vergleichen

**Intention:** Übertrage den bekannten Vergleich auf mehr Eingaben.

**Lernziel:** Du kannst nach Stufe 2, A01 einen Vergleich als Methode formulieren und nach Stufe 1, A06 mehrere Eingaben wiederholen.


- Erweitere das Programm, sodass es **drei oder mehr Zahlen** vergleicht
- Baue eine Methode `Max(double a, double b)`, die die größere Zahl zurückgibt
- Ergänze eine erneute Eingabe, wenn ungültiger Text eingegeben wird; negative und dezimale Zahlen werden bereits unterstützt.

---

> 🧠 Diese Aufgabe ist ideal, um erste Entscheidungen in deinem Code zu treffen. Du übst den Umgang mit Benutzereingaben und Bedingungen auf eine einfache, praktische Art.

## Passende Lernquellen

[Leseempfehlung für diesen Lernschritt](../Referenzen/Lernquellen.md#stufe-1-eingaben-und-ablauf). Wähle den dort genannten Abschnitt zur aktuellen Aufgabe und probiere ihn in deinem eigenen Programm aus.
