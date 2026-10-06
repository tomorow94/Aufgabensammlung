# 🔴 Aufgabe A01: Adressbuch als REST-API mit ASP.NET Core

## Einordnung und Lernziele

**Status:** Pflicht im Lernfaden.

**Voraussetzungen:** [Dasselbe Adressbuch mit EF Core und LINQ](../Stufe5/A03_ORMundLINQ.md)

**Intention:** Die vorhandene Kontaktverwaltung über einen HTTP-Vertrag zugänglich machen.

**Lernziele:**

- Du kannst CRUD-Endpunkte mit passenden Statuscodes und validierten Eingaben bauen.
- Du kannst Modell, Context und asynchrone Datenzugriffe weiterverwenden.

**Weiter im Pflichtpfad:** [Unit- und Integrationstests für das Adressbuch](A02_Testing.md)

## Ziel und Voraussetzungen

Stelle das Adressbuch aus Stufe 5 über HTTP bereit. Du verwendest **Person und AddressBookContext weiter**; die Kontakte bleiben in SQL Server. Das neue API-Projekt übernimmt die HTTP-Kommunikation, nicht eine zweite Kontaktliste im Speicher.

Neu sind HTTP, JSON, Controller, Dependency Injection und `async`/`await`. Ein Controller erhält seinen Context über den Konstruktor. EF Core führt Datenbankzugriffe asynchron aus; `await` wartet auf das Ergebnis. Anders als bei CPU-Arbeit ist dafür kein `Task.Run` nötig.

## Anforderungen

1. Erstelle ein ASP.NET-Core-Projekt mit .NET 10 und Controller-Unterstützung.
2. Referenziere dein Datenprojekt mit dem Modell und Context.
3. Implementiere die folgenden Endpunkte:

| Methode | Pfad | Ergebnis |
|---|---|---|
| GET | `/api/contacts` | 200, Liste (auch leer) |
| GET | `/api/contacts/{id}` | 200 mit Kontakt oder 404 |
| POST | `/api/contacts` | 201 mit neuer Datenbank-ID und Location-Header |
| PUT | `/api/contacts/{id}` | 204 oder 404 |
| DELETE | `/api/contacts/{id}` | 204 oder 404 |

4. Verwende einen eigenen `ContactInput` für Eingaben. IDs vergibt die Datenbank; Clients können keine ID festlegen.
5. Validiere Name, Alter, Enum, Telefonnummer und E-Mail. `[ApiController]` gibt bei ungültigen Eingaben automatisch HTTP 400 zurück.
6. Dokumentiere die API mit OpenAPI. Die Sammlung nutzt `Microsoft.AspNetCore.OpenApi` passend zu .NET 10; ein interaktives UI steht unter „Bonus“.

## Referenzanwendung starten

Vom Repository-Wurzelordner:

```shell
dotnet restore Beispiele/Adressbuch/Adressbuch.slnx
dotnet run --project Beispiele/Adressbuch/Api -- --urls http://localhost:5000
```

Die Tabelle aus Stufe 5 muss existieren; alternativ richte eine frische Datenbank mit der mitgelieferten Migration ein. Stelle sicher, dass deine SQL-Server-Instanz dem lokalen Connection String entspricht. Wenn du nur die automatisierten Tests ausführen willst, brauchst du keinen SQL Server: Die Tests konfigurieren eine eigene SQLite-Datenbank.

Der Port ist in diesem Befehl ausdrücklich festgelegt. Überprüfe bei eigenen Startprofilen immer die ausgegebene Adresse. Für OpenAPI aktiviere in PowerShell die Entwicklungsumgebung:

```powershell
$env:ASPNETCORE_ENVIRONMENT = "Development"
dotnet run --project Beispiele/Adressbuch/Api -- --urls http://localhost:5000
```

Dann liefert `http://localhost:5000/openapi/v1.json` das OpenAPI-Dokument. Teste mit Postman, einer REST-Datei im Editor oder dem Browser (GET).

## Konfiguration

Der lokale Connection String steht in [appsettings.json](../Beispiele/Adressbuch/Api/appsettings.json). Für andere Verbindungen überschreibst du `ConnectionStrings:AddressBook` über User Secrets oder `ConnectionStrings__AddressBook` als Umgebungsvariable. Im Terminal aus `Beispiele/Adressbuch`:

```shell
dotnet user-secrets set "ConnectionStrings:AddressBook" "DEIN_CONNECTION_STRING" --project Api
```

User Secrets werden im Development-Modus gelesen. Für das lokale SQL-Zertifikat ist `TrustServerCertificate=True` erklärt in Stufe 5; veröffentlichte Datenbanken verwenden ein gültiges Zertifikat. Fehlerdetails und Passwörter gehören nicht in HTTP-Antworten.

## Gestufte Hinweise

Versuche zuerst eine eigene Lösung. Öffne bei Bedarf zunächst Hinweis 1 und erst danach Hinweis 2; die vorhandenen Beispiele bzw. Referenzen dienen anschließend zum Vergleichen.

<details>
<summary>Hinweis 1: Denkanstoß</summary>

Welche Daten liefert der Client und welche vergibt der Server?

</details>

<details>
<summary>Hinweis 2: Vorgehensweise</summary>

POST enthält ContactInput ohne ID; das gleiche Datenmodell wird gespeichert und der Server liefert 201 mit Location.

</details>

<details>
<summary>Vollständige Lösung und Dateiaufteilung</summary>

- [Person.cs](../Beispiele/Adressbuch/Core/Person.cs): gemeinsames Datenmodell.
- [ContactInput.cs](../Beispiele/Adressbuch/Core/ContactInput.cs): validierte Eingaben, keine ID.
- [AddressBookContext.cs](../Beispiele/Adressbuch/Data/AddressBookContext.cs): dieselbe Kontakttabelle wie in Stufe 5.
- [Program.cs](../Beispiele/Adressbuch/Api/Program.cs): DI, OpenAPI, CORS und statische Dateien.
- [ContactsController.cs](../Beispiele/Adressbuch/Api/Controllers/ContactsController.cs): vollständiges CRUD mit EF Core.

Die Datenbank erzeugt IDs unabhängig von der aktuellen Anzahl von Kontakten. Jeder HTTP-Request erhält einen eigenen Context. Es gibt keine gemeinsame ungeschützte `static List` und keinen Ersatz von Datenbank-IDs durch `Count + 1`.

</details>

## Beispielrequest

```json
{"name":"Alice","age":30,"gender":0,"phoneNumber":"+49 0123","email":"alice@example.com"}
```

In Postman: POST an `http://localhost:5000/api/contacts`, Body als JSON, Header `Content-Type: application/json`. Verwende die zurückgegebene ID für weitere Requests.

## Selbst prüfen

Neuer Kontakt → 201; gültiger Abruf → 200; Änderung/Löschung → 204; fehlende ID → 404. Leerer Name, Alter `-1`, Gender `99`, fehlende Telefonnummer oder fehlende/ungültige E-Mail → 400. Lösche einen älteren Kontakt und füge einen neuen hinzu: Keine vorhandene ID darf doppelt vergeben werden. Starte die API neu und prüfe die gespeicherten Daten.

## Bonus: Weitere API-Funktionen

**Intention:** Erweitere einen bestehenden HTTP-Vertrag gezielt.

**Lernziel:** Du kannst Suchparameter und Paginierung definieren; Logging und Authentifizierung sind zusätzliche eigene Lernschritte.

Suchparameter, Paginierung, Logging und später Authentifizierung. Die folgende Aufgabe automatisiert zunächst die vorhandenen Verträge.

## Bonus: Interaktive API-Dokumentation

**Intention:** Probiere eine zusätzliche Oberfläche für den vorhandenen OpenAPI-Vertrag aus. **Lernziel:** Du kannst eine passende UI einrichten und erklären, dass sie den API-Vertrag anzeigt, aber keine fachlichen Tests ersetzt. Die konkrete UI-Bibliothek und ihre kompatible Version recherchierst du zusätzlich; die Pflichtaufgabe funktioniert mit OpenAPI und REST-Client.

## Passende Lernquellen

[Leseempfehlung für diesen Lernschritt](../Referenzen/Lernquellen.md#stufe-6-http-tests-und-webseite). Wähle den dort genannten Abschnitt zur aktuellen Aufgabe und probiere ihn in deinem eigenen Programm aus.
