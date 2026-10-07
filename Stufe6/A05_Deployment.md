# 🔴 Aufgabe A05: Adressbuch mit Datenbank bereitstellen

## Einordnung und Lernziele

**Status:** Pflicht im Lernfaden.

**Voraussetzungen:** [Bestehendes GitHub-Projekt und CI weiterentwickeln](A04_GitHub.md)

**Intention:** Die fertige Anwendung mit nachvollziehbarer Konfiguration lokal bereitstellen.

**Lernziele:**

- Du kannst App, Migration und SQL Server im beschriebenen Containerweg starten.
- Du kannst Persistenz bei Neustart und Fehlerursachen anhand von Logs prüfen.

**Weiter im Pflichtpfad:** Abschlussreflexion dieser Aufgabe und Dokumentation des fertigen Adressbuchs.

## Ziel und Voraussetzungen

Du hast API, Tests und Frontend. Jetzt stellst du dieselbe Anwendung reproduzierbar bereit. Wähle zunächst **einen vollständigen Weg**: API und statische Webseite im selben Container, SQL Server als separater Dienst. Dadurch bleibt die API-Adresse im Frontend relativ und die Datenhaltung dauerhaft.

Voraussetzungen: Docker mit Linux-Containern (unter Windows etwa Docker Desktop mit WSL 2), ausreichender Speicher für SQL Server und ein Rechner, auf dem die SQL-Server-Linux-Container unterstützt werden. Die Developer Edition der Datenbank in diesem Beispiel ist für Entwicklung und Tests vorgesehen.

## Anforderungen

1. Erzeuge das Publish-Ergebnis mit .NET 10 und starte die passende Runtime.
2. Binde API-Port und Frontend konsistent ein.
3. Erstelle das Datenbankschema durch eine Migration, bevor die Anwendung startet.
4. Speichere die Datenbank in einem Volume, damit Daten Containerneustarts überleben.
5. Konfiguriere Verbindung und Passwort außerhalb des Quellcodes.
6. Prüfe Hinzufügen, Neustart, Lesen und Löschen über die Webseite. Prüfe Bearbeiten mit einem PUT-Request aus [A01](./A01_REST_API.md); die Bearbeitungsoberfläche aus dem Bonus zu A03 ist dafür keine Voraussetzung.

## Vollständiger lokaler Weg

Wechsle vom Repository-Wurzelordner nach `Beispiele/Adressbuch`. Erstelle in PowerShell die lokale Konfigurationsdatei:

```powershell
Copy-Item .env.example .env
```

Ersetze in `.env` `SQL_PASSWORD` durch ein eigenes Entwicklungspasswort mit mindestens acht Zeichen, Groß-/Kleinbuchstaben, Ziffer und Sonderzeichen. Verwende im Beispiel keine Semikolons, da der Wert in einen Connection String eingesetzt wird. `.env` steht in `.gitignore`.

```shell
docker compose up --build -d
docker compose ps
docker compose logs migrate app
```

Öffne `http://localhost:5000`. Compose startet zuerst SQL Server, wartet auf dessen Healthcheck, führt einen einmaligen Migrationsdienst aus und startet danach die App. Der Port ist ausdrücklich **5000 außen → 8080 im Container**. Der Browser greift relativ auf `/api/contacts` zu. Die Datenbank hat keinen veröffentlichten Host-Port; Dienste erreichen sie intern über `db`.

Wenn du Anwendungsänderungen veröffentlichen willst, baue die App neu; für neue Migrationen muss auch der Migrationsdienst erneut ausgeführt werden:

```shell
docker compose up --build -d
```

Bei Fehlern schaue in die Logs des betroffenen Dienstes. Fehlende `.env`, ein unzulässiges Passwort, Portkonflikte und zu wenig Datenbankspeicher sind unterschiedliche Ursachen.

## Gestufte Hinweise

Versuche zuerst eine eigene Lösung. Öffne bei Bedarf zunächst Hinweis 1 und erst danach Hinweis 2; die vorhandenen Beispiele bzw. Referenzen dienen anschließend zum Vergleichen.

<details>
<summary>Hinweis 1: Denkanstoß</summary>

Welcher Dienst muss bereit sein, bevor Schema und Anwendung starten können?

</details>

<details>
<summary>Hinweis 2: Vorgehensweise</summary>

Prüfe erst den Datenbank-Healthcheck, dann den Migrationsdienst und die App; Kontakte liegen im benannten Datenbank-Volume.

</details>

<details>
<summary>Dateien und Buildschritte</summary>

- [Dockerfile](../Beispiele/Adressbuch/Dockerfile): mehrstufiger Build mit SDK 10 und Runtime 10.
- [compose.yaml](../Beispiele/Adressbuch/compose.yaml): Datenbank, Migration, App, Volume und feste Portzuordnung.
- [.env.example](../Beispiele/Adressbuch/.env.example): lokale Konfigurationsvorlage.
- [Migrationen](../Beispiele/Adressbuch/Data/Migrations/): initiales Schema für frische Datenbanken.

Das Dockerfile führt `dotnet publish` beim Build aus. Der letzte Container enthält das Publish-Ergebnis einschließlich `wwwroot` und liefert API und Webseite gemeinsam aus.

Die Migration verwendet dieselben Kontaktfelder wie SQL, EF und API. Das Compose-Beispiel startet eine eigene frische Datenbank, deren Schema vollständig durch Migrationen verwaltet wird.

</details>

## Selbst prüfen

1. Erstelle einen Kontakt und merke dir seine ID.
2. Führe `docker compose restart app` aus: Der Kontakt bleibt erhalten.
3. Beende mit `docker compose down` und starte erneut: Das benannte Datenbank-Volume bleibt erhalten und der Kontakt ist weiterhin da.
4. Prüfe HTTP 400 für ungültige Daten und HTTP 404 für fehlende IDs.
5. Prüfe die Webseite in einem zweiten Browserfenster.

`docker compose down --volumes` entfernt auch die gespeicherten Daten. Nutze es nur, wenn du die Entwicklungsdaten ausdrücklich verwerfen willst.

## Abschlussreflexion

Dokumentiere den Weg eines Kontakts vom Formular über HTTP und EF zur Tabelle. Welche Prüfungen laufen im Browser, welche im Server? Welche Daten bleiben bei Neustart erhalten? Welche Tests benötigen SQL Server? Halte Startbefehle, verwendete Versionen und offene Erweiterungen in deiner README fest.

## Bonus: Öffentliches Hosting

**Intention:** Untersuche die zusätzlichen Anforderungen einer öffentlich erreichbaren Bereitstellung.

**Lernziel:** Du kannst HTTPS, Host-Konfiguration, Datenbankzugriff und Sicherung vom lokalen Containerstart unterscheiden. Dies ist keine Voraussetzung für den Abschluss des Pflichtpfads.


Lokales Docker-Hosting ist noch keine öffentlich erreichbare Anwendung. Für einen eigenen Server benötigst du zusätzlich eine Domain, einen Reverse Proxy mit HTTPS, korrekt konfigurierte öffentliche Ports und eine Produktionsdatenbank mit geeigneter Lizenz. Verwende dort einen eingeschränkten Datenbankbenutzer, gültige Zertifikate, Backups und eine getestete Wiederherstellung. Das lokale Beispiel bindet absichtlich nur an `127.0.0.1`.

Azure App Service kann die ASP.NET-Core-Anwendung ausführen; Azure SQL ist eine mögliche passende Datenbank. Netlify oder Vercel können das statische Frontend übernehmen, benötigen für diese Architektur aber zusätzlich einen geeigneten ASP.NET-Core-API-Host. Bei getrennten Hosts musst du die öffentliche HTTPS-API-URL und die erlaubte CORS-Origin konfigurieren. Diese Alternativen sind Vertiefungen und ersetzen nicht die vollständige lokale Startanleitung.

## Passende Lernquellen

[Leseempfehlung für diesen Lernschritt](../Referenzen/Lernquellen.md#stufe-6-http-tests-und-webseite). Wähle den dort genannten Abschnitt zur aktuellen Aufgabe und probiere ihn in deinem eigenen Programm aus.
