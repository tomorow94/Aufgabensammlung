# 📌 C# Cheat Sheet – Grundlagen & Syntax

## 📚 Inhaltsverzeichnis
- [✫️ Grundstruktur eines Programms](#️-grundstruktur-eines-programms)
- [🟢 Variablen & Datentypen](#-variablen--datentypen)
- [🔁 Kontrollstrukturen](#-kontrollstrukturen)
  - [if / else](#if--else)
  - [switch](#switch)
- [🔁 Schleifen](#-schleifen)
  - [for](#for)
  - [while](#while)
  - [foreach](#foreach)
- [🔧 Methoden (Funktionen)](#-methoden-funktionen)
- [📆 Arrays & Listen](#-arrays--listen)
  - [Array](#array)
  - [List<T>](#listt)
- [📒 Dictionary & HashSet](#-dictionary--hashset)
- [🧱 Klassen & Objekte](#-klassen--objekte)
- [🥪 Einfache Fehlerbehandlung](#-einfache-fehlerbehandlung)
- [🕒 Zeit & Timer](#-zeit--timer)
- [💬 Konsole](#-konsole)
- [💪 Tipp zu LINQ](#-tipp-zu-linq)
- [ℹ️ Weitere Ressourcen](#️-weitere-ressourcen)

---

# 📌 C# Cheat Sheet – Grundlagen & Syntax

## ✫️ Grundstruktur eines Programms
```csharp
using System;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Hallo Welt!");
    }
}
```

---

## 🟢 Variablen & Datentypen
```csharp
int zahl = 42;
double preis = 19.99;
string name = "Olaf";
bool istAktiv = true;
char buchstabe = 'A';
```

---

## 🔁 Kontrollstrukturen

### if / else
```csharp
if (zahl > 10)
{
    Console.WriteLine("Groß");
}
else
{
    Console.WriteLine("Klein");
}
```

### switch
```csharp
switch (tag)
{
    case "Montag":
        Console.WriteLine("Wochenstart");
        break;
    default:
        Console.WriteLine("Irgendein Tag");
        break;
}
```

---

## 🔁 Schleifen

### for
```csharp
for (int i = 0; i < 5; i++)
{
    Console.WriteLine(i);
}
```

### while
```csharp
int i = 0;
while (i < 5)
{
    Console.WriteLine(i);
    i++;
}
```

### foreach
```csharp
string[] namen = { "Anna", "Ben", "Clara" };
foreach (string n in namen)
{
    Console.WriteLine(n);
}
```

---

## 🔧 Methoden (Funktionen)
```csharp
static int Addiere(int a, int b)
{
    return a + b;
}
```

---

## 📆 Arrays & Listen

### Array
```csharp
int[] zahlen = { 1, 2, 3, 4 };
```

### List<T>
```csharp
using System.Collections.Generic;

List<string> namen = new List<string>();
namen.Add("Anna");
```

---

## 📒 Dictionary & HashSet
```csharp
Dictionary<string, int> punkte = new Dictionary<string, int>();
punkte["Alice"] = 10;

HashSet<int> uniqueZahlen = new HashSet<int> { 1, 2, 3 };
```

---

## 🧱 Klassen & Objekte
```csharp
class Person
{
    public string Name;
    public int Alter;

    public void Begruessen()
    {
        Console.WriteLine($"Hallo, ich bin {Name}");
    }
}

// Nutzung
Person p = new Person();
p.Name = "Olaf";
p.Begruessen();
```

---

## 🥪 Einfache Fehlerbehandlung
```csharp
try
{
    int zahl = int.Parse("abc");
}
catch (FormatException)
{
    Console.WriteLine("Keine gültige Zahl!");
}
```

---

## 🕒 Zeit & Timer
```csharp
var start = DateTime.Now;
// ... etwas machen ...
var dauer = DateTime.Now - start;
Console.WriteLine($"Dauer: {dauer.TotalSeconds} Sekunden");
```

---

## 💬 Konsole
```csharp
Console.WriteLine("Text ausgeben");
string eingabe = Console.ReadLine();
Console.WriteLine($"Du hast '{eingabe}' eingegeben.");
```

---

💪 **Tipp:** Nutze `using System.Linq;` für LINQ-Methoden wie `Where`, `FirstOrDefault`, `Any`, `Select`.

---

### ℹ️ Weitere Ressourcen
- [Microsoft C# Doku](https://learn.microsoft.com/de-de/dotnet/csharp/)
- [dotnetfiddle.net](https://dotnetfiddle.net) – C# im Browser testen

