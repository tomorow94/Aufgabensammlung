# 🔴 Aufgabe A01: Adressbuch als REST-API mit ASP.NET Core

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
6. Dokumentiere die API mit OpenAPI. Die Sammlung nutzt `Microsoft.AspNetCore.OpenApi` passend zu .NET 10; ein zusätzliches interaktives Swagger-UI ist optional.

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

Zusatz: Suchparameter, Paginierung, Logging und später Authentifizierung. Die folgende Aufgabe automatisiert zunächst die vorhandenen Verträge.
