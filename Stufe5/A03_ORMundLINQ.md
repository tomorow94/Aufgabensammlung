# 🟣 Aufgabe A03: Dasselbe Adressbuch mit EF Core und LINQ

## Einordnung und Lernziele

**Status:** Pflicht im Lernfaden.

**Voraussetzungen:** [Adressbuch mit SQL Server und ADO.NET](A02_Datenbank.md)

**Intention:** Direkte Datenbankzugriffe mit einem ORM nachvollziehen.

**Lernziele:**

- Du kannst das bestehende Modell mit einem DbContext speichern und per LINQ abfragen.
- Du kannst eine vorhandene Tabelle von einem durch Migrationen verwalteten Schema unterscheiden.

**Weiter im Pflichtpfad:** [Adressbuch als REST-API mit ASP.NET Core](../Stufe6/A01_REST_API.md)

## Ziel und Voraussetzungen

Nach direktem SQL verwendest du **Entity Framework Core** als ORM. Es ordnet die Tabelle `Contacts` der Klasse `Person` zu. **LINQ** beschreibt Abfragen; Hinzufügen, Ändern und Löschen sind EF-Core-Operationen, keine LINQ-Abfragen.

Verwende die Kontaktfelder und den Tabellennamen aus A02 weiter. Du brauchst SQL-Grundlagen, Klassen, Listen und Methoden; Lambda-Ausdrücke wie `p => p.Name` bedeuten hier „für jedes p dessen Name“.

## Anforderungen

1. Installiere `Microsoft.EntityFrameworkCore.SqlServer` passend zu .NET 10.
2. Erstelle `AddressBookContext` und `DbSet<Person> Contacts`.
3. Verwende die vorhandene Tabelle aus A02 und dieselbe Verbindungszeichenfolge.
4. Implementiere CRUD und die bisherigen Eingabeprüfungen.
5. Suche mit `Where`, sortiere mit `OrderBy` und begrenze Ergebnisse mit `Take`.
6. Prüfe, dass Daten nach Programmneustart erhalten bleiben.

## Projekt vorbereiten

Für deine eigene Umsetzung erstellst du im Ordner deiner Projekte eine Konsolenanwendung und installierst das Paket. Übernimm dein Kontaktmodell aus Stufe 3 und lege den Context selbst an:

```shell
dotnet new console -n AddressBook.Ef --framework net10.0
dotnet add AddressBook.Ef package Microsoft.EntityFrameworkCore.SqlServer --version 10.0.0
```

Wenn du stattdessen das folgende Referenzbeispiel ausprobieren möchtest, erstelle `AddressBook.Ef` vom Wurzelordner **dieser Aufgabensammlung** aus und referenziere das mitgelieferte Datenprojekt:

```shell
dotnet add AddressBook.Ef reference Beispiele/Adressbuch/Data/Data.csproj
```

Die Referenz zum Datenprojekt stellt dessen EF-Paket und das Modell transitiv bereit. Die folgenden `using AddressBook.Core;` und `using AddressBook.Data;` beziehen sich auf diese Referenz; bei deiner eigenen Umsetzung verwendest du deine eigenen Namespaces.

## Gestufte Hinweise

Versuche zuerst eine eigene Lösung. Öffne bei Bedarf zunächst Hinweis 1 und erst danach Hinweis 2; die vorhandenen Beispiele bzw. Referenzen dienen anschließend zum Vergleichen.

<details>
<summary>Hinweis 1: Denkanstoß</summary>

Welche Teile ersetzt EF Core und welche fachlichen Regeln bleiben nötig?

</details>

<details>
<summary>Hinweis 2: Vorgehensweise</summary>

Der Context verwaltet dieselben Kontakte; entscheide vor der Schemaeinrichtung zwischen bestehender Tabelle und frischem Migrationsweg.

</details>

<details>
<summary>Context, Modell und Beispielabfragen</summary>

Das gleiche [Person-Modell](../Beispiele/Adressbuch/Core/Person.cs) und der [Context](../Beispiele/Adressbuch/Data/AddressBookContext.cs) werden später direkt von der API wiederverwendet. Der Context bekommt seine Optionen von außen; er enthält keine feste Serveradresse.

```csharp
using System;
using System.Linq;
using AddressBook.Core;
using AddressBook.Data;
using Microsoft.EntityFrameworkCore;
class Program
{
    static void Main()
    {
        var options = new DbContextOptionsBuilder<AddressBookContext>()
            .UseSqlServer("Server=localhost\\SQLEXPRESS;Database=AddressBook;Integrated Security=True;Encrypt=True;TrustServerCertificate=True")
            .Options;
        using var context = new AddressBookContext(options);
        var person = new Person { Name = "Alice", Age = 30, Gender = GenderType.Unknown,
            PhoneNumber = "+49 0123", Email = "alice@example.com" };
        context.Contacts.Add(person);
        context.SaveChanges(); // Die Datenbank setzt person.Id.
        var found = context.Contacts.Where(p => p.Name.StartsWith("A")).OrderBy(p => p.Name).Take(20).ToList();
        foreach (var contact in found) Console.WriteLine(contact);
        person.Email = "alice.neu@example.com";
        context.SaveChanges();
        context.Contacts.Remove(person);
        context.SaveChanges();
    }
}
```

Das Beispiel setzt die bereits angelegte Tabelle aus A02 voraus. Es erstellt und entfernt seinen Demonstrationskontakt. Für deine Menüaktionen verwende kurze Context-Lebensdauern; lade bei Bearbeiten/Löschen mit `Find(id)` und behandle `null` als „nicht gefunden“.

</details>

## Schemaerstellung und Migrationen

Ein ORM legt Tabellen **nicht allein durch die Klassendefinition** an. Die vorhandene Tabelle aus A02 kann ohne Neuerstellung verwendet werden. Für eine **frische** Datenbank enthält die Referenzanwendung eine Initialmigration und eine anschließende Migration für die Alters- und Enum-Regeln. `database update` wendet beide an. Vom Wurzelordner dieser Aufgabensammlung aus:

```shell
cd Beispiele/Adressbuch
dotnet tool restore
dotnet ef database update --project Data --startup-project Api
```

Führe die initiale Migration nicht auf der bereits manuell angelegten `Contacts`-Tabelle aus: Sie würde dieselbe Tabelle erneut anlegen wollen. Für das Testen der Referenzmigration wähle mit der Umgebungsvariable `ConnectionStrings__AddressBook` eine neue Datenbank, z. B. `AddressBookMigrationDemo`. Die API kann die vorhandene A02-Datenbank unabhängig davon normal verwenden.

**Bonus: Schemaänderung.** **Intention:** Untersuche die Weiterentwicklung einer bereits durch Migrationen verwalteten Datenbank. **Lernziel:** Du kannst eine Modelländerung als Migration erzeugen und auf eine Entwicklungsdatenbank anwenden. Wenn du beispielsweise ein Notizfeld ergänzen willst, ändere zuerst das Modell und dessen Konfiguration und lege dann eine weitere Migration an. Ohne Modelländerung würde die neue Migration keine entsprechende Spalte hinzufügen. Die folgenden Befehle laufen weiterhin in `Beispiele/Adressbuch`:

```shell
dotnet ef migrations add AddContactNote --project Data --startup-project Api
dotnet ef database update --project Data --startup-project Api
```

Bei einer bestehenden manuell verwalteten Datenbank ist zunächst eine geprüfte Baseline-Migration nötig, bevor du sie in diesen Migrationsweg überführst. Übe Schemaänderungen zuerst an einer neuen Entwicklungsdatenbank. `EnsureCreated()` ist für einfache, neu erstellte Wegwerfdatenbanken geeignet, etwa in Tests; es aktualisiert keine vorhandenen Tabellen und wird nicht mit Migrationen gemischt.

## Selbst prüfen

Ein Kontakt bekommt eine Datenbank-ID, Suche und Sortierung stimmen, Änderungen überleben Neustarts, eine fehlende ID wird behandelt. JSON-, SQL- und EF-Kontakte enthalten dieselben Eigenschaften. Schaue dir im Debugger den Zustand eines hinzugefügten und eines geänderten Objekts an. Prüfe die Suche auch bei null Treffern.

## Bonus: Beziehungen und größere Listen

**Intention:** Erweitere das bestehende EF-Modell und begrenze größere Ergebnismengen.

**Lernziel:** Du kannst Beziehungen und Paginierung untersuchen; zusätzliche SQL-Server-Testautomatisierung folgt in Bonus A08.

Ergänze eine Beziehung oder Paginierung, nachdem die Kernfälle auf SQL Server funktionieren. Die spätere automatische Prüfung providerspezifischer Datentypen, Constraints und Migrationen behandelt [Stufe 6, Bonus A08](../Stufe6/A08_SQLServerTests_Bonus.md).

Referenzen: [EF Core](https://learn.microsoft.com/en-us/ef/core/) und [Schemaerstellung](https://learn.microsoft.com/en-us/ef/core/managing-schemas/ensure-created).

## Passende Lernquellen

[Leseempfehlung für diesen Lernschritt](../Referenzen/Lernquellen.md#stufe-5-daten-und-abfragen). Wähle den dort genannten Abschnitt zur aktuellen Aufgabe und probiere ihn in deinem eigenen Programm aus.
