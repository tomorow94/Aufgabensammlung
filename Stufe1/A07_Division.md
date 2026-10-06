# 🟢 Aufgabe A07: Division

## Einordnung und Lernziele

**Status:** Pflicht im Lernfaden.

**Voraussetzungen:** [Multiplikation und Wiederholung](A06_Multiplikation.md)

**Intention:** Sonderfälle einer Rechnung vor der Ausführung erkennen.

**Lernziele:**

- Du kannst eine Division mit passenden Zahlentypen ausführen.
- Du kannst einen Nenner von null abweisen und den Grund erklären.

**Weiter im Pflichtpfad:** [Taschenrechner mit Menü](A08_Taschenrechner.md)

## Ziel der Aufgabe

In dieser Aufgabe wirst du zwei Zahlen eingeben, sie **dividieren** und das **Ergebnis anzeigen**.  
Zusätzlich lernst du, wie man mit Sonderfällen wie der **Division durch 0** umgeht.

---

## Was du lernst

- Wie man durch Eingaben dividiert (`a / b`)
- Wie man Division durch 0 verhindert
- Wie man Benutzerfeedback bei Fehlern gibt

---

## Gestufte Hinweise

Versuche zuerst eine eigene Lösung. Öffne bei Bedarf zunächst Hinweis 1 und erst danach Hinweis 2; die vorhandenen Beispiele bzw. Referenzen dienen anschließend zum Vergleichen.

<details>
<summary>Hinweis 1: Denkanstoß</summary>

Welche Eingabe ist für den Nenner unzulässig?

</details>

<details>
<summary>Hinweis 2: Vorgehensweise</summary>

Prüfe den Nenner vor dem Dividieren; mit double erhältst du auch Ergebnisse zwischen ganzen Zahlen.

</details>

## Schritt-für-Schritt-Anleitung

### 🔧 1. Projekt erstellen

1. Starte Visual Studio.
2. Erstelle ein neues Projekt vom Typ **Konsolenanwendung**.
3. Projektname: z. B. `Division`

---

### 💻 2. Code eingeben

```csharp
using System;

class Program
{
    static void Main(string[] args)
    {
        Console.Write("Zähler (oben): ");
        double zaehler = Convert.ToDouble(Console.ReadLine());

        Console.Write("Nenner (unten): ");
        double nenner = Convert.ToDouble(Console.ReadLine());

        if (nenner == 0)
        {
            Console.WriteLine("Fehler: Division durch 0 ist nicht erlaubt.");
        }
        else
        {
            double ergebnis = zaehler / nenner;
            Console.WriteLine($"{zaehler} geteilt durch {nenner} ergibt {ergebnis}.");
        }
    }
}
```

---

### ▶️ 3. Ausführen

- Starte das Programm mit `F5`.
- Teste sowohl mit gültigen als auch ungültigen Eingaben (z. B. Nenner = 0).

---

## 🔍 Erklärt

| Code-Zeile | Bedeutung |
|-----------|-----------|
| `a / b` | Division der beiden Zahlen |
| `if (b == 0)` | Prüft auf ungültige Division |

---

## Weiterüben im Pflichtpfad

- Was passiert bei Kommazahlen?
- Was passiert, wenn `b` negativ ist?
- Gib eine Fehlermeldung aus, wenn die Eingabe ungültig ist (z. B. kein Zahlentext).

---

> 🧠 Diese Aufgabe zeigt dir, wie wichtig es ist, **Eingaben zu überprüfen**, bevor du mit ihnen rechnest!


## Selbst prüfen

`7` und `2` ergeben `3,5` in einer deutschen Umgebung; `-6` und `2` ergeben `-3`. Nenner `0` ergibt eine Meldung, keine Berechnung. Das Einstiegsbeispiel setzt Zahlen als Eingabe voraus; ergänze die aus A05 bekannte `TryParse`-Prüfung und prüfe `abc` sowie eine leere Eingabe.

## Passende Lernquellen

[Leseempfehlung für diesen Lernschritt](../Referenzen/Lernquellen.md#stufe-1-eingaben-und-ablauf). Wähle den dort genannten Abschnitt zur aktuellen Aufgabe und probiere ihn in deinem eigenen Programm aus.
