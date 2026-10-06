# 🔴 Aufgabe A02: Unit- und Integrationstests für das Adressbuch

## Ziel und Voraussetzungen

Manuelle Grenzfallprüfungen begleiten die Sammlung bereits seit Stufe 1. Jetzt automatisierst du sie. **Unit-Tests** prüfen eine kleine Einheit ohne HTTP und Datenbank. **Integrationstests** prüfen das Zusammenspiel ausgewählter Teile, hier Routing, Validierung, Controller und relationale Speicherung über HTTP.

Ein Integrationstest muss nicht die gesamte reale Infrastruktur verwenden. Die mitgelieferten Tests benutzen SQLite im Speicher. Das ist eine echte relationale Datenbank, aber kein vollständiger Ersatz für SQL Server. Ergänze SQL-Server-Tests für migrations-, datentyp- oder serverspezifisches Verhalten.

## Anforderungen

1. Erstelle ein xUnit-Testprojekt mit .NET 10 und einer Referenz zum API-Projekt.
2. Teste Regeln für Name, Alter, Telefonnummer, E-Mail und Enum unabhängig von HTTP.
3. Verwende `Microsoft.AspNetCore.Mvc.Testing` und `WebApplicationFactory<Program>` für HTTP-Tests.
4. Stelle jeder Testmethode einen eigenen Host und Datenbestand bereit. Tests dürfen weder eine feste Reihenfolge noch gemeinsame statische Listen voraussetzen.
5. Prüfe CRUD, HTTP-Status, JSON-Inhalt und Location-Header; „nicht leer“ oder „Status erfolgreich“ allein reicht nicht.
6. Sichere die frühere ID-Kollision ab: einen älteren Kontakt löschen, einen neuen hinzufügen, IDs vergleichen.

## Vorbereitung für dein eigenes Projekt

```shell
dotnet new xunit -n AddressBook.Tests --framework net10.0
dotnet add AddressBook.Tests reference DEIN_API_PROJEKT.csproj
dotnet add AddressBook.Tests package Microsoft.AspNetCore.Mvc.Testing --version 10.0.0
dotnet add AddressBook.Tests package Microsoft.EntityFrameworkCore.Sqlite --version 10.0.0
```

Ersetze `DEIN_API_PROJEKT.csproj` durch den tatsächlichen Pfad. Das xUnit-Projekttemplate enthält Test-SDK und Test-Runner bereits; nur `xunit` zu installieren genügt bei einem gewöhnlichen Klassenbibliotheksprojekt nicht.

Die API benötigt am Ende von `Program.cs`:

```csharp
public partial class Program { }
```

Damit ist der Einstiegspunkt aus dem Testprojekt zugänglich. Bei Controller-Tests müssen Namespace und Referenzen zum eigenen Projekt passen; die Referenzanwendung verwendet `AddressBook.Api.Controllers`.

<details>
<summary>Vollständige Lösung</summary>

- [ContactInputTests.cs](../Beispiele/Adressbuch/Tests/ContactInputTests.cs): Pflichtfelder, Alter und Mapping.
- [ContactApiTests.cs](../Beispiele/Adressbuch/Tests/ContactApiTests.cs): eigener Host, SQLite, CRUD, ungültige Daten, fehlende IDs und CORS.
- [Tests.csproj](../Beispiele/Adressbuch/Tests/Tests.csproj): passende Pakete und Projektreferenzen.

Die Testfactory ersetzt die SQL-Server-Registrierung des Contexts durch SQLite. Die Verbindung bleibt während des Tests offen, damit die In-Memory-Datenbank erhalten bleibt. `EnsureCreated` erstellt nur dieses frische Testschema; die SQL-Server-Migrationen werden hier ausdrücklich nicht angewendet. Ein separater Testhost verhindert gegenseitige Beeinflussung.

</details>

## Tests ausführen

Vom Repository-Wurzelordner:

```shell
dotnet test Beispiele/Adressbuch/Adressbuch.slnx --configuration Release
```

## Selbst prüfen

Die Tests laufen ohne lokalen SQL Server. Verändere versuchsweise eine fachliche Regel, etwa die Altersobergrenze, und überprüfe, ob ein passender Test fehlschlägt. Stelle sie danach wieder her. Fehlende E-Mail muss HTTP 400 liefern, eine nicht existierende ID HTTP 404 und eine erfolgreiche Erstellung HTTP 201. Die Tests sind einzeln und gemeinsam ausführbar.

Zusatz: Schreibe zunächst einen fehlschlagenden Test für eine Suchfunktion, implementiere sie und räume anschließend den Code auf (TDD). Postman/Newman kann zusätzliche End-to-End-Tests gegen einen gestarteten Server ausführen; dafür muss der Server samt Testdaten in der Pipeline tatsächlich gestartet werden.

Referenz: [Integrationstests in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/test/integration-tests?view=aspnetcore-10.0).
