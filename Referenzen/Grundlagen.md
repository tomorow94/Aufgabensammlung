# 📘 C# Einstieg – Grundlagen für absolute Beginner

Dieses Dokument beantwortet grundlegende Fragen zum Aufbau und Verhalten eines einfachen C#-Programms. Es richtet sich an Personen ohne Programmiererfahrung und erklärt auch Dinge, die viele Fortgeschrittene als selbstverständlich ansehen.

---

## 📚 Was ist ein Programm?

Ein Programm ist eine Folge von Anweisungen, die der Computer **Schritt für Schritt** ausführt.

Beispielhafte Aufgaben eines Programms:

* Benutzer begrüßen
* Eingaben vom Benutzer entgegennehmen
* Rechnen, prüfen, vergleichen
* Etwas auf dem Bildschirm anzeigen

---

## 🔄 Wie läuft ein Programm ab? (Ablaufdiagramm)

Ein einfaches Ablaufdiagramm für ein typisches Konsolenprogramm:

```
[Start]
   ↓
[Code beginnt mit Main() Methode]
   ↓
[Variablen werden deklariert]
   ↓
[Benutzereingabe abfragen]
   ↓
[Verarbeitung: rechnen, prüfen, speichern]
   ↓
[Ergebnis ausgeben]
   ↓
[Ende]
```

---

## 📜 Kommentare in C\#

Kommentare helfen dir (oder anderen), den Code später besser zu verstehen. Sie werden vom Computer **ignoriert**.

### Einzeiliger Kommentar:

```csharp
// Das ist ein Kommentar
```

### Mehrzeiliger Kommentar:

```csharp
/*
   Das ist ein
   mehrzeiliger Kommentar
*/
```

Tipp: Nutze Kommentare, um Ideen, Fragen oder Zwischenstände festzuhalten!

---

## 🥪 Was sind Variablen?

Variablen sind **Platzhalter für Werte**, die sich im Laufe des Programms ändern können.

Beispiel:

```csharp
int alter = 25; // Die Variable heißt "alter" und speichert die Zahl 25
```

Du kannst dir Variablen wie **beschriftete Schubladen** vorstellen: In jeder Schublade liegt ein bestimmter Wert.

---

## 📊 Wichtige Datentypen in C\#

| Typ      | Beschreibung               | Beispiel                |
| -------- | -------------------------- | ----------------------- |
| `int`    | Ganze Zahl                 | `int x = 42;`           |
| `double` | Kommazahl                  | `double pi = 3.14;`     |
| `string` | Text (Zeichenkette)        | `string name = "Anna";` |
| `bool`   | Wahrheitswert (true/false) | `bool aktiv = true;`    |
| `char`   | Einzelnes Zeichen          | `char buchstabe = 'A';` |

Ein `string` ist also eine Zeichenkette (Text), `bool` kann nur „true“ oder „false“ sein, `char` ist ein einzelnes Zeichen.

---

## 🟡 Warum muss ich Variablen initialisieren?

In C# muss man einer Variable **einen Startwert geben**, bevor man sie verwendet. Das nennt man "initialisieren".

Beispiel:

```csharp
int x = 0; // x hat jetzt einen gültigen Wert und kann verwendet werden
```

Wenn du versuchst, mit einer nicht initialisierten Variable zu arbeiten, meldet der Compiler einen Fehler.

---

## 📏 Einfache Namensregeln (Konventionen)

In C# hält man sich meistens an folgende Regeln, damit der Code **gut lesbar** ist:

* **Variablennamen** beginnen klein, z. B. `anzahl`, `benutzerName`, `istFertig`
* **Methoden** beginnen groß, z. B. `BerechneSumme()`
* Namen sollen **beschreibend** sein – lieber `benutzerAlter` als nur `b` oder `x`
* Keine Leerzeichen oder Sonderzeichen in Namen (stattdessen CamelCase: `meinNameIst`)
* Verwende **aussagekräftige Namen**, auch wenn sie länger sind
* ✅ **Faustregel:** *So kurz wie möglich, aber so lang wie nötig!*

---

## 🥿 Gültigkeitsbereiche (Scopes)

Der sogenannte **Scope** bestimmt, wo eine Variable gültig ist. Eine Variable, die **innerhalb eines Blocks** (zum Beispiel einer `if`-Bedingung) deklariert wird, ist **nur innerhalb dieses Blocks sichtbar**.

Beispiel:

```csharp
if (x > 0)
{
    int y = 5; // y ist nur hier verfügbar
}
// Console.WriteLine(y); // Fehler! y existiert hier nicht mehr
```

Wenn du eine Variable in mehreren Blöcken brauchst, deklariere sie **außerhalb** der Blöcke:

```csharp
int y;
if (x > 0)
{
    y = 5;
}
Console.WriteLine(y); // funktioniert
```

---

## 🔁 Was bedeutet "return"?

`return` gibt einen Wert **zurück** – meist das Ergebnis einer Berechnung.

Beispiel:

```csharp
static int Addiere(int a, int b)
{
    return a + b;
}
```

Hier wird das Ergebnis der Addition zurückgegeben, damit es an anderer Stelle weiterverwendet werden kann.

---

## 🤍 Wofür brauche ich geschweifte Klammern `{}`?

In C# geben geschweifte Klammern an, **wo ein Block von Code beginnt und endet**. Zum Beispiel:

```csharp
if (x > 5)
{
    Console.WriteLine("x ist größer als 5");
}
```

Ohne die Klammern wüsste C# nicht, welche Zeile zur Bedingung gehört.

---

## 📌 Was bedeutet "static void Main"?

* `static` bedeutet: Die Methode gehört zur Klasse selbst, nicht zu einem Objekt.
* `void` bedeutet: Die Methode gibt **nichts zurück**.
* `Main` ist der Startpunkt deines Programms – hier beginnt die Ausführung.

```csharp
static void Main(string[] args)
{
    Console.WriteLine("Hallo Welt");
}
```

---

## 🧲 Beispiel: Gültigkeit und Sichtbarkeit von Variablen

```csharp
int globaleZahl = 100; // sichtbar in der ganzen Methode

if (globaleZahl > 50)
{
    int lokaleZahl = 10; // nur innerhalb dieser if-Klammer sichtbar
    Console.WriteLine(lokaleZahl); // OK
}

// Console.WriteLine(lokaleZahl); // Fehler: lokaleZahl existiert hier nicht mehr
```

Visualisierung:

```
Main-Methode
├ globalVariable
└ if-Block
   └ lokaleVariable
```

---

## 🔎 Sichtbarkeit & Lebensdauer – Übersicht (Diagramm)

```
+-------------------------------+
|      Sichtbarkeit & Scope     |
+-------------------------------+
| Globale Variable (z. B. Feld) | → im gesamten Code der Klasse verfügbar
| Lokale Variable               | → nur im Block (z. B. Schleife, if) gültig
| Parameter einer Methode       | → nur innerhalb der Methode sichtbar
+-------------------------------+
```

Lebensdauer = wie lange die Variable im Speicher bleibt:

* Lokale Variable: nur während der Methode oder des Blocks
* Objektvariable (z. B. in Klasse): solange das Objekt existiert

---