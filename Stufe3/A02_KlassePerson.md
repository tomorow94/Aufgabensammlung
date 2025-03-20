# Aufgabe A02: Erstellung einer Klasse "Person" – Einführung in Objekte und Enums

## Ziel

In dieser Aufgabe erstellen Sie eine **Klasse `Person`**, um die Grundlagen der **objektorientierten Programmierung (OOP)** in C# zu erlernen. Sie werden die Konzepte von **Klassen, Objekten, Eigenschaften und Methoden** kennenlernen.

Zusätzlich wird ein **Enum** eingeführt, um den Umgang mit vordefinierten Kategorien innerhalb einer Klasse zu üben.

---

## Anforderungen

1. **Klasse `Person` erstellen**
   - Die Klasse soll die folgenden Eigenschaften besitzen:
     - `Name` (string) – Name der Person.
     - `Age` (int) – Alter der Person.
     - `Gender` (GenderType) – Geschlecht der Person (Enum).
   - Eine Methode `Greet()`, die eine personalisierte Begrüßung ausgibt.

2. **Enum `GenderType` hinzufügen**
   - Definieren Sie ein Enum namens `GenderType` mit den Werten:
     - `Male`
     - `Female`
     - `Diverse`
     - `Unknown`
   - Diese Werte sollen als Geschlechtsangabe für eine `Person` genutzt werden.

3. **Objekte der Klasse `Person` erstellen**
   - Instanziieren Sie **mehrere Personen** mit unterschiedlichen Eigenschaften.
   - Rufen Sie die Metho

## 2. Die Person-Klasse

```csharp
public class Person
{
    public string Name { get; set; }
    public int Age { get; set; }
    public GenderType Gender { get; set; }

    public Person(string name, int age, GenderType gender)
    {
        Name = name;
        Age = age;
        Gender = gender;
    }

    public void Greet()
    {
        string genderText = Gender switch
        {
            GenderType.Male => "Mr.",
            GenderType.Female => "Ms.",
            GenderType.Diverse => "Mx.",
            _ => ""
        };

        Console.WriteLine($"Hello {genderText} {Name}, you are {Age} years old.");
    }
}
```

## 3. Nutzung der Klasse Person
```csharp
class Program
{
    static void Main()
    {
        Person person1 = new Person("Alice", 30, GenderType.Female);
        Person person2 = new Person("Bob", 25, GenderType.Male);
        Person person3 = new Person("Charlie", 29, GenderType.Diverse);
        Person person4 = new Person("Eve", 40, GenderType.Unknown);

        person1.Greet();
        person2.Greet();
        person3.Greet();
        person4.Greet();
    }
}
```

## Erweiterungsmöglichkeiten
- Zusätzliche Methoden hinzufügen: Erstellen Sie eine Methode Describe(), die weitere Details über die Person ausgibt.
- Vergleichsmethoden implementieren: Überladen Sie die Methode ToString(), um ein einfaches Textformat für die Ausgabe der Person zu erhalten.
- Weitere Enums integrieren: Erstellen Sie z. B. ein OccupationType-Enum, das verschiedene Berufe speichert.
  
Diese Aufgabe vermittelt ein Grundverständnis für Klassen, Objekte, Konstruktoren und Enums und bereitet auf komplexere OOP-Konzepte vor.
