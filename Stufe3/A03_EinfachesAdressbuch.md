# 🟠 Aufgabe A03: Adressbuch mit Kontakten und Dateispeicherung

## Einordnung und Lernziele

**Status:** Pflicht im Lernfaden.

**Voraussetzungen:** [Person, Eigenschaften, Konstruktor und Enum](A02_KlassePerson.md)

**Intention:** Objekte in einer Sammlung verwalten und gemeinsam dauerhaft speichern.

**Lernziele:**

- Du kannst Kontakte hinzufügen, suchen und als JSON wieder laden.
- Du kannst fachliche Prüfung und eindeutige IDs über einen Neustart erhalten.

**Weiter im Pflichtpfad:** [Gemeinsame Schnittstelle und Menü](A04_BesseresMenu.md)

## Ziel und Voraussetzungen

Erweitere die Personenklasse aus A02 zu einem Adressbuch. Ab hier bleibt dieses Datenmodell bis zum Abschlussprojekt gleich:

| Eigenschaft | Typ und Bedeutung |
|---|---|
| `Id` | `int`, von der Anwendung bzw. später der Datenbank vergeben |
| `Name` | `string`, Pflichtfeld, höchstens 100 Zeichen |
| `Age` | `int`, 0–130 |
| `Gender` | `GenderType`, 0 = Unknown, 1 = Male, 2 = Female, 3 = Diverse |
| `PhoneNumber` | `string`, Pflichtfeld, höchstens 50 Zeichen; kein Zahlentyp wegen `+` und führender Nullen |
| `Email` | `string`, gültige Adresse, höchstens 200 Zeichen |

Du brauchst Listen, Dateizugriffe und Methoden. Neu ist **JSON**, ein Textformat zum Speichern strukturierter Daten. `System.Text.Json` gehört zu .NET 10.

## Anforderungen

1. Erstelle `AddressBook` mit `AddPerson`, `FindPerson` und `DisplayAll`.
2. Trenne die Kontaktliste von der Menüführung. Suchmethoden geben Daten zurück; das Menü zeigt sie an.
3. Ergänze `PhoneNumber`, `Email` und `Id`. Verwende für diese bearbeitbaren Kontakte Eigenschaften mit `get; set;`.
4. Prüfe Eingaben, einschließlich Name, Alter, Telefonnummer, E-Mail und Enum. `Enum.TryParse` allein akzeptiert auch undefinierte numerische Werte; prüfe zusätzlich `Enum.IsDefined`.
5. Speichere Kontakte in `contacts.json` und lade sie beim Start. Zeige den vollständigen Pfad an.
6. Bei ungültigen Eingaben frage erneut oder kehre ins Menü zurück; ersetze ungültiges Alter nicht still durch `0`.

## Vorgehen

Implementiere zuerst Hinzufügen und Anzeigen ohne Datei. Danach Suche, dann Speichern und Laden. Die Datei befindet sich relativ zum **Arbeitsverzeichnis**, das du mit `Directory.GetCurrentDirectory()` prüfen kannst.

## Gestufte Hinweise

Versuche zuerst eine eigene Lösung. Öffne bei Bedarf zunächst Hinweis 1 und erst danach Hinweis 2; die vorhandenen Beispiele bzw. Referenzen dienen anschließend zum Vergleichen.

<details>
<summary>Hinweis 1: Denkanstoß</summary>

Welche Verantwortung hat das Menü und welche die Kontaktverwaltung?

</details>

<details>
<summary>Hinweis 2: Vorgehensweise</summary>

Suchmethoden geben Kontakte zurück; beim Laden wird der nächste ID-Wert aus dem größten vorhandenen Wert abgeleitet.

</details>

<details>
<summary>Lösungsskizze: Datenmodell und Sammlung</summary>

Das vollständige Datenmodell liegt in [Person.cs](../Beispiele/Adressbuch/Core/Person.cs). Kopiere es und entferne für dein einfaches Konsolenprojekt gegebenenfalls die Namespace-Zeile sowie `using AddressBook.Core;` aus der folgenden Skizze. Wenn du den Namespace beibehältst, bleibt auch das `using` erhalten. `GenderType` ersetzt die Definition aus A02; definiere das Enum nur einmal.

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;
using System.Text.Json;
using AddressBook.Core;

public class AddressBook
{
    private List<Person> contacts = [];
    private int nextId = 1;
    public void AddPerson(Person person)
    {
        person.Id = nextId++;
        contacts.Add(person);
    }
    public Person? FindPerson(string name) => contacts.FirstOrDefault(p =>
        string.Equals(p.Name, name, StringComparison.OrdinalIgnoreCase));
    public IReadOnlyList<Person> GetAll() => contacts.AsReadOnly();
    public void Save(string path) => File.WriteAllText(path, JsonSerializer.Serialize(contacts));
    public void Load(string path)
    {
        if (!File.Exists(path)) return;
        var loaded = JsonSerializer.Deserialize<List<Person>>(File.ReadAllText(path))
            ?? throw new InvalidDataException("Kontaktliste fehlt.");
        if (loaded.Any(p => p is null || p.Id <= 0) || loaded.Select(p => p.Id).Distinct().Count() != loaded.Count)
            throw new InvalidDataException("Ungültige oder doppelte Kontakt-IDs.");
        contacts = loaded;
        nextId = checked(contacts.Select(p => p.Id).DefaultIfEmpty(0).Max() + 1);
    }
}
```

Diese Skizze ergänzt du um das Menü und die fachliche Eingabeprüfung. Eine Telefonnummer darf nicht leer sein. Prüfe die E-Mail etwa mit `EmailAddressAttribute` aus `System.ComponentModel.DataAnnotations`. Vor dem Hinzufügen und nach dem Laden müssen die Kontakte dieselben Regeln erfüllen. Fehler beim Lesen (`IOException`, `JsonException`, `InvalidDataException`) werden im Menü sichtbar angezeigt; eine beschädigte Datei soll nicht still überschrieben werden.

`DisplayAll()` kann über `GetAll()` iterieren. Für Menü-Aktionen nutzt du bereits seit A01 `Start()` statt zusätzlicher `Main`-Methoden; A04 ergänzt dafür die gemeinsame Schnittstelle. Neue Kontakte erhalten IDs durch `AddressBook`; bei Datenbanken übernimmt dies später `IDENTITY`.

</details>

## Selbst prüfen

| Ablauf | Erwartung |
|---|---|
| Alice hinzufügen, nach `alice` suchen | Alice wird gefunden |
| zweimal denselben Namen hinzufügen | zwei Kontakte mit unterschiedlichen IDs; Suche findet den ersten |
| Telefonnummer `+49 0123` | Zeichen bleiben erhalten |
| leere Telefonnummer, ungültige E-Mail, Alter `-1`, Gender `99` | Eingabe abgewiesen |
| speichern, Programm neu starten | Kontakte und IDs bleiben erhalten |
| weitere Person nach Neustart hinzufügen | keine doppelte ID |
| Datei fehlt | leeres Adressbuch |
| beschädigtes JSON | verständliche Meldung; Datei nicht überschreiben |

Setze einen Haltepunkt beim Hinzufügen und beobachte die Liste.

## Bonus: Weitere Kontaktaktionen

**Intention:** Erweitere die vorhandene Kontaktverwaltung bei gleichen Regeln.

**Lernziel:** Du kannst mehrere Suchtreffer, Bearbeiten oder Löschen implementieren und die ID-Vergabe nach dem Neustart prüfen.

Suche mit mehreren Treffern, Bearbeiten und Löschen. Wenn du IDs auch nach dem Löschen niemals wiederverwenden willst, speichere den fortlaufenden Zähler zusammen mit der Liste. Die spätere SQL-Datenbank erledigt dies selbst.

## Passende Lernquellen

[Leseempfehlung für diesen Lernschritt](../Referenzen/Lernquellen.md#stufe-3-struktur-und-versionsgeschichte). Wähle den dort genannten Abschnitt zur aktuellen Aufgabe und probiere ihn in deinem eigenen Programm aus.
