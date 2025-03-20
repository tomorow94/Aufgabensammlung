# Aufgabe A03: Einfaches Adressbuch – Erweiterung der `Person`-Klasse

## Ziel

In dieser Aufgabe erweitern Sie die bestehende `Person`-Klasse, um ein einfaches **Adressbuch** zu erstellen. Das Adressbuch soll es ermöglichen, **Personen mit Namen und Telefonnummern zu speichern und wieder abzurufen**. Dies vertieft die Arbeit mit **Listen, Suchfunktionen und Benutzerinteraktionen**.

---

## Anforderungen

1. **Erweiterung der `Person`-Klasse**
   - Fügen Sie ein **Feld für die Telefonnummer** (`PhoneNumber`) hinzu.
   - Erweitern Sie den Konstruktor, um die Telefonnummer zu speichern.
   - Aktualisieren Sie die `Greet()`-Methode, sodass sie nun auch die Telefonnummer anzeigt.

2. **Adressbuch-Klasse erstellen**
   - Erstellen Sie eine **neue Klasse `AddressBook`**, die eine **Liste von `Person`-Objekten** verwaltet.
   - Implementieren Sie folgende Methoden:
     - `AddPerson(Person person)`: Fügt eine Person zum Adressbuch hinzu.
     - `FindPerson(string name)`: Sucht eine Person nach ihrem Namen und gibt deren Informationen aus.
     - `DisplayAll()`: Gibt alle gespeicherten Kontakte aus.

3. **Menü für Benutzerinteraktion**
   - Erstellen Sie eine **Benutzerschnittstelle** in der Konsole, die folgende Aktionen ermöglicht:
     - Eine neue Person hinzufügen.
     - Eine Person nach Namen suchen.
     - Alle gespeicherten Kontakte anzeigen.
     - Programm beenden.

---

## Hinweise

- Verwenden Sie eine **`List<Person>`**, um die Personen im Adressbuch zu speichern.
- Nutzen Sie **Schleifen und `Console.ReadLine()`**, um Benutzereingaben zu verarbeiten.
- Implementieren Sie **eine einfache Suchfunktion**, um eine Person anhand ihres Namens zu finden.

---

## Beispielhafter Lösungsansatz

### **1. Erweiterung der `Person`-Klasse**
```csharp
public class Person
{
    public string Name { get; set; }
    public int Age { get; set; }
    public GenderType Gender { get; set; }
    public string PhoneNumber { get; set; }

    public Person(string name, int age, GenderType gender, string phoneNumber)
    {
        Name = name;
        Age = age;
        Gender = gender;
        PhoneNumber = phoneNumber;
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

        Console.WriteLine($"Hello {genderText} {Name}, you are {Age} years old. Phone: {PhoneNumber}");
    }
}
```

### **2. Neue Klasse `AddressBook`**
```csharp
using System;
using System.Collections.Generic;
using System.Linq;

public class AddressBook
{
    private List<Person> contacts = new List<Person>();

    public void AddPerson(Person person)
    {
        contacts.Add(person);
        Console.WriteLine($"{person.Name} has been added to the address book.");
    }

    public void FindPerson(string name)
    {
        var person = contacts.FirstOrDefault(p => p.Name.Equals(name, StringComparison.OrdinalIgnoreCase));
        if (person != null)
        {
            Console.WriteLine($"Found: {person.Name}, Age: {person.Age}, Phone: {person.PhoneNumber}");
        }
        else
        {
            Console.WriteLine("Person not found.");
        }
    }

    public void DisplayAll()
    {
        if (contacts.Count == 0)
        {
            Console.WriteLine("The address book is empty.");
            return;
        }

        Console.WriteLine("Address Book:");
        foreach (var person in contacts)
        {
            Console.WriteLine($"- {person.Name}, Age: {person.Age}, Phone: {person.PhoneNumber}");
        }
    }
}
```

### **3. Menü für die Benutzerinteraktion**
```csharp
class Program
{
    static void Main()
    {
        AddressBook addressBook = new AddressBook();
        bool running = true;

        while (running)
        {
            Console.WriteLine("\n===== Address Book Menu =====");
            Console.WriteLine("1. Add a new person");
            Console.WriteLine("2. Search for a person");
            Console.WriteLine("3. Display all contacts");
            Console.WriteLine("4. Exit");
            Console.Write("Choose an option: ");

            string choice = Console.ReadLine();
            switch (choice)
            {
                case "1":
                    Console.Write("Enter name: ");
                    string name = Console.ReadLine();
                    Console.Write("Enter age: ");
                    int age = int.TryParse(Console.ReadLine(), out int parsedAge) ? parsedAge : 0;
                    Console.Write("Enter gender (Male, Female, Diverse, Unknown): ");
                    GenderType gender = Enum.TryParse(Console.ReadLine(), out GenderType parsedGender) ? parsedGender : GenderType.Unknown;
                    Console.Write("Enter phone number: ");
                    string phone = Console.ReadLine();

                    addressBook.AddPerson(new Person(name, age, gender, phone));
                    break;

                case "2":
                    Console.Write("Enter the name of the person: ");
                    string searchName = Console.ReadLine();
                    addressBook.FindPerson(searchName);
                    break;

                case "3":
                    addressBook.DisplayAll();
                    break;

                case "4":
                    running = false;
                    Console.WriteLine("Exiting program...");
                    break;

                default:
                    Console.WriteLine("Invalid input. Please try again.");
                    break;
            }
        }
    }
}
```

## Erweiterungsmöglichkeiten
- Speicherung in einer Datei: Erweitern Sie das Programm so, dass Kontakte in einer Datei gespeichert und beim Start geladen werden.
- Löschen von Kontakten: Fügen Sie eine Funktion hinzu, um Personen aus dem Adressbuch zu entfernen.
- Erweiterte Suchfunktionen: Implementieren Sie eine Suche nach Telefonnummer oder Alter.

Dieses Adressbuch ermöglicht eine **erste praktische Nutzung von Klassen und Listen**, bietet **eine einfache Interaktion mit Benutzereingaben** und kann später durch weitere Funktionen ergänzt werden.
