# 🟢 Aufgabe A03: Addieren

## Einordnung und Lernziele

**Status:** Pflicht im Lernfaden.

**Voraussetzungen:** [Texteingabe und -ausgabe](A02_TexteingabeUndAusgabe.md)

**Intention:** Text als Zahl verarbeiten und eine erste Rechnung nachvollziehen.

**Lernziele:**

- Du kannst zwei gültige Zahlen einlesen und ihre Summe berechnen.
- Du kannst erklären, warum Text und Zahlen unterschiedlich verarbeitet werden.

**Weiter im Pflichtpfad:** [Größere Zahl finden](A04_GroessereZahlFinden.md)

## Ziel der Aufgabe

In dieser Aufgabe wirst du zwei Zahlen vom Benutzer einlesen, ihre **Summe berechnen** und auf der Konsole ausgeben.  
Dabei lernst du, wie man **Zahlen als Eingabe verarbeitet**, um damit **Rechnungen durchzuführen**.

---

## Was du lernst

- Wie man mit `Convert.ToDouble` Zahlen von der Konsole einliest
- Wie man zwei Werte addiert
- Wie man das Ergebnis formatiert ausgibt

---

## Gestufte Hinweise

Versuche zuerst eine eigene Lösung. Öffne bei Bedarf zunächst Hinweis 1 und erst danach Hinweis 2; die vorhandenen Beispiele bzw. Referenzen dienen anschließend zum Vergleichen.

<details>
<summary>Hinweis 1: Denkanstoß</summary>

Was würde geschehen, wenn du zwei Eingabetexte ohne Umwandlung mit + verbindest?

</details>

<details>
<summary>Hinweis 2: Vorgehensweise</summary>

Wandle jede Eingabe in einen Zahlentyp um und addiere erst danach; sichere Eingabeprüfung folgt in A05.

</details>

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

## Weiterüben im Pflichtpfad

- Gib andere Werte ein: ganze Zahlen, Kommazahlen oder negative Zahlen.
- Tausche `double` gegen `int` aus – was passiert mit Kommazahlen?

## Selbst prüfen

`2` und `3` ergeben `5`, `-2` und `3` ergeben `1`. In einer deutschen Umgebung ergeben `4` und `5,5` den Wert `9,5`. Das Dezimaltrennzeichen richtet sich nach der Rechnerkultur. Das erste einfache Beispiel setzt gültige Zahlen voraus. Beim Typvergleich nutzt du für `int` zunächst `Convert.ToInt32` statt `Convert.ToDouble` und beobachtest das Ergebnis.

**Bonus-Prüfung nach A05:** Die Erweiterung mit `TryParse` weist `abc` und leere Eingaben ab. Nutze beim Wechsel zu `int` dann `int.TryParse` statt nur den Variablentyp zu ändern.

## Bonus: Sichere und wiederholte Eingaben (nach A05/A06)

**Intention:** Verbinde die erste Rechnung später mit Eingabeprüfung und Wiederholung.

**Lernziel:** Du kannst nach A05 ungültige Zahlentexte abweisen und nach A06 mehrere Zahlen summieren.

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

## Passende Lernquellen

[Leseempfehlung für diesen Lernschritt](../Referenzen/Lernquellen.md#stufe-1-eingaben-und-ablauf). Wähle den dort genannten Abschnitt zur aktuellen Aufgabe und probiere ihn in deinem eigenen Programm aus.
