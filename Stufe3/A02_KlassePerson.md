# 🟠 Aufgabe A02: Person, Eigenschaften, Konstruktor und Enum

## Ziel und Voraussetzungen

Du kennst Methoden und das Menüprojekt. Eine **Klasse** beschreibt die Daten und das Verhalten ihrer **Objekte**. Eine Eigenschaft wie `Name` gehört zu einem bestimmten Objekt; eine Methode wie `Greet()` kann dessen Daten verwenden.

Ein **Konstruktor** wird beim Erstellen mit `new` aufgerufen. Ein **Enum** benennt eine begrenzte Menge von Werten. `Unknown` steht hier an Position `0`, damit ein noch nicht gesetzter Wert „keine Angabe“ bedeutet.

## Anforderungen

1. Erstelle `Person` mit `Name`, `Age` und `Gender`.
2. Definiere `GenderType` vollständig und erstelle mehrere Personen.
3. Lass jede Person `Greet()` ausführen. Überprüfe ein negatives Alter.
4. Trenne Dateien für `Person`, `GenderType` und das Programm, sobald das Beispiel läuft.

<details>
<summary>Vollständiges Einstiegsbeispiel für Program.cs (.NET 10)</summary>

```csharp
using System;
public enum GenderType { Unknown, Male, Female, Diverse }
public class Person
{
    public string Name { get; }
    public int Age { get; }
    public GenderType Gender { get; }
    public Person(string name, int age, GenderType gender)
    {
        if (string.IsNullOrWhiteSpace(name)) throw new ArgumentException("Name fehlt.", nameof(name));
        if (age < 0 || age > 130) throw new ArgumentOutOfRangeException(nameof(age));
        if (!Enum.IsDefined(gender)) throw new ArgumentOutOfRangeException(nameof(gender));
        Name = name.Trim();
        Age = age;
        Gender = gender;
    }
    public void Greet() => Console.WriteLine($"Hallo {Name}, du bist {Age} Jahre alt.");
    public override string ToString() => $"{Name} ({Age}, {Gender})";
}
class Program
{
    static void Main()
    {
        var alice = new Person("Alice", 30, GenderType.Female);
        var bob = new Person("Bob", 25, GenderType.Unknown);
        alice.Greet();
        bob.Greet();
        Console.WriteLine(alice);
        try { _ = new Person("Test", -1, GenderType.Unknown); }
        catch (ArgumentOutOfRangeException) { Console.WriteLine("Negatives Alter wurde abgewiesen."); }
    }
}
```

`get` erlaubt Lesen. Der Konstruktor weist den Anfangswert zu; außerhalb der Klasse können diese Eigenschaften nicht verändert werden. `override` **überschreibt** die vorhandene Methode `ToString()`; Überladen wäre eine weitere Methode gleichen Namens mit anderen Parametern.

</details>

## Selbst prüfen

Zwei Personen behalten unterschiedliche Namen und Alter. `Unknown` hat den Zahlenwert `0`. Leere Namen, Alter `-1` oder `131` und `(GenderType)99` werden abgewiesen. Beobachte im Debugger, welches Objekt `this` bezeichnet.

Das Adressbuch ergänzt im nächsten Schritt `Id`, `PhoneNumber` und `Email`. Für dessen bearbeitbare und serialisierbare Kontakte werden die Eigenschaften bewusst auf `get; set;` umgestellt; die Eingaben prüft dann die Anwendung. Erkläre den Unterschied zu den hier unveränderlichen Eigenschaften.

Zusatz: Ein neutrales Enum wie `ContactCategory` eignet sich für eigene Kategorien. Erweitere die Ausgabe oder untersuche zwei Referenzen auf dasselbe Objekt.
