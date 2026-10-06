# 🟢 Aufgabe A07: Division

## Ziel der Aufgabe

In dieser Aufgabe wirst du zwei Zahlen eingeben, sie **dividieren** und das **Ergebnis anzeigen**.  
Zusätzlich lernst du, wie man mit Sonderfällen wie der **Division durch 0** umgeht.

---

## Was du lernst

- Wie man durch Eingaben dividiert (`a / b`)
- Wie man Division durch 0 verhindert
- Wie man Benutzerfeedback bei Fehlern gibt

---

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

## 💡 Probiere selbst:

- Was passiert bei Kommazahlen?
- Was passiert, wenn `b` negativ ist?
- Gib eine Fehlermeldung aus, wenn die Eingabe ungültig ist (z. B. kein Zahlentext).

---

> 🧠 Diese Aufgabe zeigt dir, wie wichtig es ist, **Eingaben zu überprüfen**, bevor du mit ihnen rechnest!


## Selbst prüfen

`7` und `2` ergeben `3,5` in einer deutschen Umgebung; `-6` und `2` ergeben `-3`. Nenner `0` ergibt eine Meldung, keine Berechnung. Das Einstiegsbeispiel setzt Zahlen als Eingabe voraus; ergänze die aus A05 bekannte `TryParse`-Prüfung und prüfe `abc` sowie eine leere Eingabe.
