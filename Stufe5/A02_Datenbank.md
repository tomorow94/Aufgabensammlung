# 🟣 Aufgabe A02: Adressbuch mit SQL Server und ADO.NET

## Einordnung und Lernziele

**Status:** Pflicht im Lernfaden.

**Voraussetzungen:** [Sortieralgorithmen fair vergleichen](A01_Sortieralgorithmen.md)

**Intention:** Dasselbe Kontaktmodell in einer relationalen Datenbank speichern.

**Lernziele:**

- Du kannst SQL-CRUD und parametrisierte ADO.NET-Befehle ausführen.
- Du kannst Datenbank-ID, Persistenz und Eingabeprüfung getrennt erklären.

**Weiter im Pflichtpfad:** [Dasselbe Adressbuch mit EF Core und LINQ](A03_ORMundLINQ.md)

## Ziel und Voraussetzungen

Das Adressbuch aus Stufe 3 speichert bisher eine JSON-Datei. Jetzt speicherst du **dieselben Kontakte mit denselben Eigenschaften** in einer relationalen Datenbank. Du lernst SQL zunächst direkt und danach aus C# über ADO.NET.

Installiere SQL Server Express und SSMS getrennt. SSMS ist ein Verwaltungsprogramm, nicht die Datenbank-Engine. Ein üblicher Instanzname ist `localhost\SQLEXPRESS`; prüfe den tatsächlich installierten Namen. Verbinde dich lokal mit Windows-Authentifizierung. Die Befehle laufen im Terminal; `Install-Package` wäre dagegen ein Befehl der Visual-Studio-Paket-Manager-Konsole.

## Datenmodell

`Contacts` enthält `Id`, `Name`, `Age`, `Gender`, `PhoneNumber`, `Email`. Eine Zeile entspricht einer `Person`. `Id` ist der Primärschlüssel und wird durch `IDENTITY(1,1)` von SQL Server vergeben. Telefonnummern sind Text; E-Mail und Name sind ebenfalls Text. `NVARCHAR` unterstützt Unicode.

Ein Fremdschlüssel wäre beispielsweise `Notes.ContactId`, der auf `Contacts.Id` verweist. Beziehungen sind eine spätere Erweiterung; zunächst genügt eine Tabelle.

## Anforderungen und Vorgehen

1. Lege in SSMS eine Datenbank **AddressBook** an und wähle sie als aktive Datenbank.
2. Führe [schema.sql](../Beispiele/Adressbuch/schema.sql) genau einmal aus. Es enthält dieselben Spalten wie das Modell in Stufe 3; Pflichtfelder sind auch in der Datenbank `NOT NULL`.
3. Übe `INSERT`, `SELECT`, `UPDATE`, `DELETE` zunächst in SSMS mit erfundenen Kontakten.
4. Erstelle ein Konsolenprojekt mit .NET 10 und installiere den SQL-Server-Treiber im festgelegten Beispielstand:

```shell
dotnet new console -n AddressBook.Sql --framework net10.0
dotnet add AddressBook.Sql package Microsoft.Data.SqlClient --version 6.1.1
```

5. Übernimm `Person` und die Eingabeprüfung aus Stufe 3. Ersetze Dateioperationen durch Datenbankzugriffe.
6. Nutze Parameter statt zusammengebauter SQL-Zeichenketten. Prüfe bei UPDATE/DELETE die Anzahl geänderter Zeilen.
7. Halte Verbindungen mit `using` kurz offen. Fange `SqlException` im Menü ab und zeige verständliche Fehlermeldungen.

## Verbindung

Für die lokale Windows-Instanz:

```csharp
string connectionString = "Server=localhost\\SQLEXPRESS;Database=AddressBook;Integrated Security=True;Encrypt=True;TrustServerCertificate=True";
```

`TrustServerCertificate=True` ist hier eine Vereinfachung für den lokalen Entwicklungsserver mit selbstsigniertem Zertifikat. Für einen veröffentlichten Server verwende ein gültiges Zertifikat und `TrustServerCertificate=False`. Passwörter gehören in Umgebungsvariablen oder User Secrets, nicht in Quellcode. Der API-Teil zeigt beide Konfigurationswege.

## SQL ausprobieren

```sql
INSERT INTO Contacts (Name, Age, Gender, PhoneNumber, Email)
VALUES (N'Alice', 30, 0, N'+49 0123', N'alice@example.com');
SELECT Id, Name, Age, Gender, PhoneNumber, Email FROM Contacts ORDER BY Name;
UPDATE Contacts SET Email = N'alice.neu@example.com' WHERE Id = 1;
DELETE FROM Contacts WHERE Id = 1;
```

Die Beispieldatei verwendet in allen Teilen `Id`, nicht wechselnd `CustomerID` oder `ID`. Passe `1` an die tatsächlich vergebene ID an.

## Gestufte Hinweise

Versuche zuerst eine eigene Lösung. Öffne bei Bedarf zunächst Hinweis 1 und erst danach Hinweis 2; die vorhandenen Beispiele bzw. Referenzen dienen anschließend zum Vergleichen.

<details>
<summary>Hinweis 1: Denkanstoß</summary>

Wer vergibt die ID und wie gelangt ein Name sicher in eine SQL-Abfrage?

</details>

<details>
<summary>Hinweis 2: Vorgehensweise</summary>

IDENTITY vergibt die ID; übergib Eingaben als Parameter und prüfe das Ergebnis nach einem Programmneustart.

</details>

<details>
<summary>Vollständiges kleines ADO.NET-Beispiel für Program.cs</summary>

Das Beispiel fügt einen Kontakt hinzu, liest ihn, ändert ihn und löscht ihn. Prüfe die Daten in SSMS mit einem Haltepunkt zwischen den Schritten. Baue danach dein Menü darum.

```csharp
using System;
using System.Data;
using Microsoft.Data.SqlClient;
class Program
{
    static void Main()
    {
        string connectionString = Environment.GetEnvironmentVariable("ADDRESSBOOK_CONNECTION")
            ?? "Server=localhost\\SQLEXPRESS;Database=AddressBook;Integrated Security=True;Encrypt=True;TrustServerCertificate=True";
        try
        {
            using var connection = new SqlConnection(connectionString);
            connection.Open();
            using var insert = new SqlCommand("INSERT INTO Contacts (Name, Age, Gender, PhoneNumber, Email) OUTPUT INSERTED.Id VALUES (@name, @age, @gender, @phone, @email)", connection);
            insert.Parameters.Add("@name", SqlDbType.NVarChar, 100).Value = "Alice";
            insert.Parameters.Add("@age", SqlDbType.Int).Value = 30;
            insert.Parameters.Add("@gender", SqlDbType.Int).Value = 0;
            insert.Parameters.Add("@phone", SqlDbType.NVarChar, 50).Value = "+49 0123";
            insert.Parameters.Add("@email", SqlDbType.NVarChar, 200).Value = "alice@example.com";
            int id = (int)insert.ExecuteScalar()!;
            using (var read = new SqlCommand("SELECT Id, Name, PhoneNumber, Email FROM Contacts WHERE Id = @id", connection))
            {
                read.Parameters.Add("@id", SqlDbType.Int).Value = id;
                using var reader = read.ExecuteReader();
                while (reader.Read()) Console.WriteLine($"{reader.GetInt32(0)}: {reader.GetString(1)}, {reader.GetString(2)}, {reader.GetString(3)}");
            }
            using var update = new SqlCommand("UPDATE Contacts SET Email = @email WHERE Id = @id", connection);
            update.Parameters.Add("@email", SqlDbType.NVarChar, 200).Value = "alice.neu@example.com";
            update.Parameters.Add("@id", SqlDbType.Int).Value = id;
            Console.WriteLine($"Geändert: {update.ExecuteNonQuery()}");
            using var delete = new SqlCommand("DELETE FROM Contacts WHERE Id = @id", connection);
            delete.Parameters.Add("@id", SqlDbType.Int).Value = id;
            Console.WriteLine($"Gelöscht: {delete.ExecuteNonQuery()}");
        }
        catch (SqlException ex) { Console.WriteLine($"Datenbankzugriff fehlgeschlagen: {ex.Message}"); }
    }
}
```

</details>

## Selbst prüfen

Nach Hinzufügen existiert der Kontakt mit positiver ID. Änderungen sind nach einem Neustart vorhanden. Ein Name mit Apostroph (`O'Connor`) funktioniert als Parameter. Eine fehlende ID verändert null Zeilen. Telefonnummern behalten führende Nullen. Ungültige Eingaben werden vor dem SQL-Aufruf abgewiesen. Stoppe den SQL-Server-Dienst und prüfe die Fehlermeldung.

## Bonus: Import und Beziehungen

**Intention:** Erweitere die Datenhaltung über eine einzelne Kontakttabelle hinaus.

**Lernziel:** Du kannst einen JSON-Import mit neuen Datenbank-IDs und später eine Beziehung mit Fremdschlüssel nachvollziehen.

Importiere JSON-Kontakte aus Stufe 3, wobei die Datenbank neue IDs vergibt. Ergänze anschließend eine zweite Tabelle mit Fremdschlüssel und untersuche `JOIN`.

Referenz: [Microsoft.Data.SqlClient](https://learn.microsoft.com/en-us/sql/connect/ado-net/introduction-microsoft-data-sqlclient-namespace).

## Passende Lernquellen

[Leseempfehlung für diesen Lernschritt](../Referenzen/Lernquellen.md#stufe-5-daten-und-abfragen). Wähle den dort genannten Abschnitt zur aktuellen Aufgabe und probiere ihn in deinem eigenen Programm aus.
