# C# Cheat Sheet – Grundlagen & Syntax

## Inhaltsverzeichnis

- [Grundlagen](#grundlagen)
  - [Grundstruktur eines Programms](#grundstruktur-eines-programms)
  - [Variablen & Datentypen](#variablen--datentypen)
  - [Operatoren](#operatoren)
  - [Ganzzahl- und Gleitkommadivision](#ganzzahl--und-gleitkommadivision)
- [Eingaben und Texte](#eingaben-und-texte)
  - [Konsole](#konsole)
  - [Nullwerte](#nullwerte)
  - [Sichere Zahleneingabe](#sichere-zahleneingabe)
  - [Zeichenketten](#zeichenketten)
- [Kontrollfluss und Methoden](#kontrollfluss-und-methoden)
  - [if / else](#if--else)
  - [switch](#switch)
  - [for](#for)
  - [while](#while)
  - [foreach](#foreach)
  - [break & continue](#break--continue)
  - [Methoden](#methoden)
- [Sammlungen und LINQ](#sammlungen-und-linq)
  - [Arrays](#arrays)
  - [List<T>](#listt)
  - [Dictionary<TKey, TValue>](#dictionarytkey-tvalue)
  - [HashSet<T>](#hashsett)
  - [LINQ](#linq)
- [Objektorientierung](#objektorientierung)
  - [Klassen, Konstruktoren & Eigenschaften](#klassen-konstruktoren--eigenschaften)
  - [Objekte erstellen](#objekte-erstellen)
  - [Schnittstellen](#schnittstellen)
  - [Enums](#enums)
  - [Enums einlesen](#enums-einlesen)
- [Dateien und Datenformate](#dateien-und-datenformate)
  - [Dateipfade](#dateipfade)
  - [Dateien lesen & schreiben](#dateien-lesen--schreiben)
  - [JSON](#json)
- [Fehler und Tests](#fehler-und-tests)
  - [Fehlerbehandlung](#fehlerbehandlung)
  - [xUnit](#xunit)
- [Zeitmessung und Asynchronität](#zeitmessung-und-asynchronität)
  - [Zeitmessung](#zeitmessung)
  - [async / await](#async--await)

## Grundlagen

### Grundstruktur eines Programms

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

### Variablen & Datentypen

```csharp
int zahl = 42;
double messwert = 1.25;
decimal preis = 19.99m;
string name = "Olaf";
bool istAktiv = true;
char buchstabe = 'A';
```

### Operatoren

```csharp
int a = 7;
int b = 3;
int rest = a % b;
bool gleich = a == b;
bool verschieden = a != b;
bool beidePositiv = a > 0 && b > 0;
bool mindestensEinerPositiv = a > 0 || b > 0;
bool nichtGleich = !gleich;
```

### Ganzzahl- und Gleitkommadivision

```csharp
int ganzzahlig = 7 / 2;
double gleitkomma = 7.0 / 2.0;
double umgewandelt = (double)7 / 2;
Console.WriteLine($"{ganzzahlig}; {gleitkomma}; {umgewandelt}");
```

## Eingaben und Texte

### Konsole

```csharp
Console.Write("Name: ");
string? eingabe = Console.ReadLine();
Console.WriteLine($"Eingabe: {eingabe}");
```

### Nullwerte

```csharp
string? text = Console.ReadLine();
string anzeige = text ?? "Keine Eingabe";
int? laenge = text?.Length;
if (text is not null)
{
    Console.WriteLine(text.Length);
}
```

### Sichere Zahleneingabe

```csharp
if (int.TryParse(Console.ReadLine(), out int zahl))
{
    Console.WriteLine(zahl);
}
else
{
    Console.WriteLine("Keine gültige ganze Zahl.");
}
```

### Zeichenketten

```csharp
string text = "  Hallo Welt  ";
string bereinigt = text.Trim();
bool leer = string.IsNullOrWhiteSpace(text);
bool gleich = string.Equals(bereinigt, "hallo welt", StringComparison.OrdinalIgnoreCase);
string[] woerter = bereinigt.Split(' ');
Console.WriteLine($"{bereinigt}: {bereinigt.Length}");
```

## Kontrollfluss und Methoden

### if / else

```csharp
int zahl = 12;
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
string tag = "Montag";
switch (tag)
{
    case "Montag":
        Console.WriteLine("Wochenstart");
        break;
    default:
        Console.WriteLine("Anderer Tag");
        break;
}
```

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
foreach (string name in namen)
{
    Console.WriteLine(name);
}
```

### break & continue

```csharp
for (int i = 0; i < 10; i++)
{
    if (i == 2) continue;
    if (i == 5) break;
    Console.WriteLine(i);
}
```

### Methoden

```csharp
static int Addiere(int a, int b)
{
    return a + b;
}

static void ZeigeNachricht(string text)
{
    Console.WriteLine(text);
}
```

## Sammlungen und LINQ

### Arrays

```csharp
int[] zahlen = { 1, 2, 3, 4 };
zahlen[0] = 10;
int anzahl = zahlen.Length;
Console.WriteLine(zahlen[0]);
```

### List<T>

```csharp
using System.Collections.Generic;

var namen = new List<string> { "Anna", "Ben" };
namen.Add("Clara");
bool gefunden = namen.Contains("Anna");
bool entfernt = namen.Remove("Ben");
int anzahl = namen.Count;
Console.WriteLine(namen[0]);
```

### Dictionary<TKey, TValue>

```csharp
using System.Collections.Generic;

var punkte = new Dictionary<string, int>();
punkte["Alice"] = 10;
if (punkte.TryGetValue("Alice", out int wert))
{
    Console.WriteLine(wert);
}
bool entfernt = punkte.Remove("Alice");
```

### HashSet<T>

```csharp
using System.Collections.Generic;

var zahlen = new HashSet<int> { 1, 2, 3 };
bool hinzugefuegt = zahlen.Add(2);
bool enthalten = zahlen.Contains(3);
bool entfernt = zahlen.Remove(1);
int anzahl = zahlen.Count;
```

### LINQ

```csharp
using System.Linq;

string[] namen = { "Clara", "Anna", "Ben" };
var sortiert = namen.OrderBy(name => name).ToList();
var gefiltert = namen.Where(name => name.Length > 3).ToList();
var grossgeschrieben = namen.Select(name => name.ToUpperInvariant()).ToArray();
bool vorhanden = namen.Any(name => name.StartsWith("A"));
string? ersterTreffer = namen.FirstOrDefault(name => name.StartsWith("A"));
```

## Objektorientierung

### Klassen, Konstruktoren & Eigenschaften

```csharp
class Product
{
    private decimal price;
    public string Name { get; }
    public decimal Price
    {
        get { return price; }
        set { price = value; }
    }

    public Product(string name, decimal price)
    {
        Name = name;
        Price = price;
    }
}
```

### Objekte erstellen

```csharp
Product product = new Product("Stift", 1.50m);
product.Price = 2.00m;
Console.WriteLine($"{product.Name}: {product.Price}");
```

### Schnittstellen

```csharp
interface ILabel
{
    string GetText();
}

class Label : ILabel
{
    public string GetText() => "Beispiel";
}
```

### Enums

```csharp
enum WorkStatus
{
    Pending = 0,
    Active = 1,
    Done = 2
}
```

### Enums einlesen

```csharp
string? text = Console.ReadLine();
if (Enum.TryParse<WorkStatus>(text, true, out var status)
    && Enum.IsDefined(status))
{
    Console.WriteLine(status);
}
```

## Dateien und Datenformate

### Dateipfade

```csharp
using System.IO;

string ordner = Directory.GetCurrentDirectory();
string pfad = Path.Combine(ordner, "notiz.txt");
Console.WriteLine(Path.GetFullPath(pfad));
```

### Dateien lesen & schreiben

```csharp
using System.IO;

string pfad = "notiz.txt";
File.WriteAllText(pfad, "Hallo");
File.AppendAllText(pfad, Environment.NewLine + "Welt");
if (File.Exists(pfad))
{
    string text = File.ReadAllText(pfad);
    Console.WriteLine(text);
}
```

### JSON

```csharp
using System.Text.Json;

string[] namen = { "Anna", "Ben" };
string json = JsonSerializer.Serialize(namen);
string[]? geladen = JsonSerializer.Deserialize<string[]>(json);
Console.WriteLine(json);
```

## Fehler und Tests

### Fehlerbehandlung

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

### xUnit

```csharp
using Xunit;

public class MathTests
{
    [Fact]
    public void AbsoluteValueIsPositive()
    {
        Assert.Equal(3, Math.Abs(-3));
    }

    [Theory]
    [InlineData(-2, 2)]
    [InlineData(0, 0)]
    public void AbsoluteValueMatches(int input, int expected)
    {
        Assert.Equal(expected, Math.Abs(input));
    }
}
```

## Zeitmessung und Asynchronität

### Zeitmessung

```csharp
using System.Diagnostics;

int[] zahlen = { 4, 1, 3, 2 };
var stopwatch = Stopwatch.StartNew();
Array.Sort(zahlen);
stopwatch.Stop();
Console.WriteLine($"Dauer: {stopwatch.Elapsed.TotalMilliseconds:F3} ms");
```

### async / await

```csharp
using System.IO;
using System.Threading.Tasks;

static async Task<string> LeseTextAsync(string pfad)
{
    string text = await File.ReadAllTextAsync(pfad);
    return text;
}
```
