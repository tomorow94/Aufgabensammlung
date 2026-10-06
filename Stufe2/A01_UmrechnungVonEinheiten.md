# 🔵 Aufgabe A01: Umrechnung von Einheiten

## Ziel der Aufgabe

In dieser Aufgabe wirst du ein Programm erstellen, das verschiedene Einheiten umrechnen kann, z. B. **Celsius in Fahrenheit** oder **Kilometer in Meilen**. Dabei vertiefst du dein Wissen über **Benutzereingaben**, **mathematische Formeln** und die Strukturierung von Programmen in **Methoden**.

Diese Aufgabe ist bewusst so gestaltet, dass du **nicht einfach Copy+Paste verwenden kannst**, sondern selbst aktiv nachdenken oder recherchieren musst, wie die Formeln und Methoden aussehen. Das fördert das Verständnis für eigenständiges Arbeiten und strukturiertes Vorgehen.

Für den Anfang könntest du dir überlegen, wie dein Programm aussehen soll, und dies stichpunktartig festhalten, z. B. als **Kommentare** direkt in deinem neuen Projekt. 
So kannst du die Aufgabe in kleinere Einzelschritte aufteilen und sicherstellen, dass du keine wichtigen Schritte vergisst.

**Beispiel:**
```csharp
// Benutzer nach Umrechnung fragen

// Eingabewert einlesen

// Umrechnungsformel anwenden

// Ergebnis ausgeben

// Wiederholung anbieten
```

In C# schreibst du Kommentare mit zwei Schrägstrichen `//` – alles, was rechts davon steht, wird vom Programm ignoriert und dient nur zur Erklärung oder Planung.

---

## Was du lernst

- Wie du mit Methoden deinen Code strukturierst
- Wie man mathematische Umrechnungen in Code übersetzt
- Wie man mehrere Funktionen in einem einfachen Konsolenprogramm anbietet

---

## Beispielaufgabe

### Dein Programm soll Folgendes können:

1. Den Benutzer fragen, welche Umrechnung gewünscht ist (z. B. Celsius zu Fahrenheit)
2. Die Eingabewerte vom Benutzer einlesen
3. Das Ergebnis berechnen und anzeigen
4. Wieder von vorn anfangen oder bei Wunsch das Programm beenden

Du kannst mit den folgenden Umrechnungen starten:

- Celsius → Fahrenheit:  `F = C * 9.0 / 5.0 + 32`
- Kilometer → Meilen:   `mi = km * 0.621371`

Optional kannst du später weitere Umrechnungen ergänzen (siehe unten).

---

## Hinweise

- Erstelle **für jede Umrechnung eine eigene Methode**.
- Nutze ein **einfaches Textmenü**, damit der Benutzer zwischen den Umrechnungen wählen kann.
- Verwende eine **Schleife**, damit der Benutzer mehrere Umrechnungen nacheinander machen kann.

---

## 🔍 Erklärt

| Konzept    | Beschreibung |
|------------|--------------|
| Methoden   | Ermöglichen es, Code logisch in Funktionen zu trennen. So wird der Code übersichtlicher und wiederverwendbar. |
| Benutzereingabe | Mit `Console.ReadLine()` wird ein Wert eingegeben, der dann verarbeitet wird. |
| `switch` oder `if` | Damit kannst du je nach Auswahl des Benutzers unterschiedliche Aktionen ausführen lassen. |

---

## 💡 Probiere selbst

- Füge weitere Umrechnungen hinzu, z. B.:
  - Kilogramm → Pfund (`kg * 2.20462`)
  - Liter → Gallonen (`l * 0.264172`)
- Sorge dafür, dass dein Menü sich wiederholt, bis der Benutzer "Beenden" auswählt
- Gib eine Fehlermeldung aus, wenn eine ungültige Option eingegeben wurde

---

<details>
<summary>📘 Tipp zur Struktur</summary>

Die folgende Skizze setzt `bool weiter = true;` und deine Methoden `CelsiusZuFahrenheit()` sowie `KilometerZuMeilen()` voraus. Ein einfaches Menü könnte so aussehen:

```csharp
while (weiter)
{
    Console.WriteLine("Was möchtest du umrechnen?");
    Console.WriteLine("1 = Celsius zu Fahrenheit");
    Console.WriteLine("2 = Kilometer zu Meilen");
    Console.WriteLine("0 = Beenden");
    
    string auswahl = Console.ReadLine() ?? "";
    switch (auswahl)
    {
        case "1": CelsiusZuFahrenheit(); break;
        case "2": KilometerZuMeilen(); break;
        case "0": weiter = false; break;
        default: Console.WriteLine("Ungültige Auswahl!"); break;
    }
}
```

</details>

---

> 🧠 Diese Aufgabe trainiert dein Verständnis für mathematische Zusammenhänge und Methodenstruktur – wichtig für wartbaren und gut organisierten Code!


## Selbst prüfen

`0 °C` ergibt `32 °F`, `100 °C` ergibt `212 °F`, `-40 °C` ergibt `-40 °F`. `1 km` ergibt ungefähr `0,621371 mi`. Ungültige Auswahl oder ungültiger Zahlentext ergibt eine Meldung; Beenden funktioniert auch nach mehreren Umrechnungen. Halte Berechnung und Eingabe getrennt, damit du die Methoden ohne Konsole testen kannst.

## Reine Methoden und frühe automatisierte Tests

Verwende für die Rechnung etwa `static double CelsiusToFahrenheit(double c) => c * 9.0 / 5.0 + 32;`. Eingabe und Ausgabe liegen außerhalb. `9 / 5` allein ist Ganzzahldivision und ergibt `1`; die Dezimalliterale vermeiden diesen Fehler unabhängig vom Typ des Eingabewerts. Liter → Gallonen bezieht sich bei Faktor `0.264172` auf US-Gallonen.

Zusatz: Automatisiere die drei Temperaturfälle schon jetzt in einem xUnit-Projekt. Für die beiden nicht exakt darstellbaren Umrechnungen prüfe mit einer Toleranz statt auf exakte Gleitkommagleichheit. Die Einrichtung wird in Stufe 6 wieder aufgegriffen.
