# Referenzanwendung: Adressbuch

.NET 10, SQL Server, EF Core, ASP.NET Core, HTML/CSS/JavaScript und xUnit. `Core` enthält das gemeinsame Kontaktmodell und die Eingabevalidierung, `Data` den Context und Migrationen, `Api` die Controller und Webseite, `Tests` isolierte Unit- und HTTP-Tests.

## Tests ohne SQL Server

Vom Repository-Wurzelordner:

```shell
dotnet test Beispiele/Adressbuch/Adressbuch.slnx --configuration Release
```

Jeder HTTP-Test verwendet eine eigene SQLite-Datenbank. Das prüft die API-Verträge, aber keine SQL-Server-spezifischen Migrationen.

## Lokal mit SQL Server Express

Voraussetzung: SQL Server Express läuft als `localhost\SQLEXPRESS`. Die Verbindung nutzt Windows-Authentifizierung; ändere `Api/appsettings.json` für eine andere Instanz.

```shell
cd Beispiele/Adressbuch
dotnet tool restore
dotnet ef database update --project Data --startup-project Api
dotnet run --project Api -- --urls http://localhost:5000
```

Der Migrationsbefehl ist für eine **frische Datenbank AddressBook** vorgesehen. Wenn du `Contacts` bereits mit `schema.sql` aus Stufe 5 angelegt hast, überspringe die Initialmigration und starte die API direkt. Für spätere Migrationen braucht dieser manuelle Datenbestand zuerst eine geprüfte Baseline. Übe den mitgelieferten Migrationsweg an einer frischen Datenbank, nicht auf der manuell erstellten Tabelle.

Öffne `http://localhost:5000`. Das Formular verwendet `/api/contacts` und alle Pflichtfelder des API-Modells. Für OpenAPI starte in PowerShell mit `$env:ASPNETCORE_ENVIRONMENT = "Development"`; dann ist `/openapi/v1.json` erreichbar.

Alternativ führt ein einmaliger Aufruf die mitgelieferten Migrationen aus, ohne den Webserver zu starten:

```shell
dotnet run --project Api -- --ApplyMigrations=true
```

Nutze auch diesen Befehl nur für den beschriebenen Migrationsweg mit einer frischen bzw. bereits durch Migrationen verwalteten Datenbank.

## Docker

Im Ordner `Beispiele/Adressbuch`:

```powershell
Copy-Item .env.example .env
```

Ändere das Entwicklungspasswort in `.env`, danach:

```shell
docker compose up --build -d
```

Webseite: `http://localhost:5000`. SQL Server speichert in einem benannten Volume. Die App startet erst nach erfolgreicher Schema-Migration. `docker compose down` erhält die Daten; `--volumes` würde sie entfernen. Docker verwendet eine eigene Datenbank, nicht die Windows-Express-Instanz. Details und Prüfschritte stehen in [Deployment](../../Stufe6/A05_Deployment.md).

## Datenmodell und Endpunkte

Ein Kontakt hat `Id`, `Name`, `Age`, `Gender`, `PhoneNumber`, `Email`. Gender wird als Zahl übertragen: 0 Unknown, 1 Male, 2 Female, 3 Diverse. Beispiel für POST:

```json
{"name":"Alice","age":30,"gender":0,"phoneNumber":"+49 0123","email":"alice@example.com"}
```

| Methode | Pfad | Antwort |
|---|---|---|
| GET | /api/contacts | 200, Liste |
| GET | /api/contacts/{id} | 200 oder 404 |
| POST | /api/contacts | 201 oder 400 |
| PUT | /api/contacts/{id} | 204, 400 oder 404 |
| DELETE | /api/contacts/{id} | 204 oder 404 |

Für eine separat auf `http://localhost:5500` gestartete Webseite erlaubt die lokale CORS-Policy Requests. Beim gemeinsamen Hosting ist keine separate Origin nötig. Der lokale TrustServerCertificate-Schalter dient nur dem selbstsignierten Entwicklungszertifikat; veröffentlichte Datenbanken verwenden gültige Zertifikate und eigene Zugangsdaten außerhalb des Repositories.
