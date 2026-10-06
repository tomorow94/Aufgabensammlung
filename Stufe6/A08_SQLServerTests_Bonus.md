# 🔴 Bonus A08: Migrationen und Datenhaltung mit SQL Server testen

## Einordnung und Lernziele

**Status:** Bonus (optional; keine Voraussetzung für spätere Pflichtaufgaben).

**Voraussetzungen:** [Dasselbe Adressbuch mit EF Core und LINQ](../Stufe5/A03_ORMundLINQ.md), [Unit- und Integrationstests für das Adressbuch](A02_Testing.md)

**Intention:** Die Aussage schneller SQLite-Tests durch gezielte SQL-Server-Prüfungen ergänzen.

**Lernziele:**

- Du kannst Migrationen und Datenbankregeln auf isolierten SQL-Server-Testdatenbanken prüfen.
- Du kannst Einrichtung, Aufräumen und providerabhängige Ergebnisse erklären.

**Weiter im Pflichtpfad:** [Webseite für dasselbe Adressbuch](A03_Webentwicklung.md)

## Aufgabe und Voraussetzungen

Die Tests aus [A02](./A02_Testing.md) prüfen HTTP-Verträge und relationale Speicherung mit SQLite. In dieser Vertiefung untersuchst du zusätzlich das SQL-Server-Verhalten des gleichen Adressbuchs. Voraussetzung sind EF Core, SQL-Server-Migrationen und xUnit. Du brauchst eine lokale **Testinstanz** mit Berechtigung zum Anlegen und Entfernen eigener Testdatenbanken; Docker und [A05](./A05_Deployment.md) sind nur für die Container-Variante nötig.

## Anforderungen

1. Erstelle ein getrenntes xUnit-Projekt `AddressBook.SqlServer.Tests`, das die API referenziert und `Microsoft.AspNetCore.Mvc.Testing` passend zum vorhandenen Paketstand verwendet. Lass die bisherigen schnellen Tests bestehen.
2. Verwende einen eigenen Testhost nach dem Muster der [vorhandenen Factory](../Beispiele/Adressbuch/Tests/ContactApiTests.cs). Entferne die vorhandene Context-Registrierung wie dort und registriere den Context mit `UseSqlServer` statt `UseSqlite`.
3. Lies die Serververbindung aus `ADDRESSBOOK_TEST_SQLSERVER`. Erzeuge für jeden Test einen Datenbanknamen wie `AddressBookTests_<GUID>`. Setze ihn mit `SqlConnectionStringBuilder.InitialCatalog`; der Name wird nicht als beliebiger Text an eine SQL-Anweisung angehängt.
4. Initialisiere die frische Testdatenbank mit `Database.MigrateAsync()`. Verwende hier **kein `EnsureCreated`**, denn du möchtest die vorhandenen SQL-Server-Migrationen prüfen.
5. Teste Schema, CRUD und die Datenbankregeln unabhängig von der API-Validierung. Ein direkt über den Context gespeichertes Alter `-1` muss an der Datenbankregel scheitern.
6. Entferne nach jedem Test nur die für diesen Test erzeugte Datenbank, auch wenn eine Assertion fehlschlägt. Bewahre den erzeugten Namen in der Fixture auf und prüfe vor dem Entfernen sowohl den exakten Namen als auch das Präfix `AddressBookTests_`. Teile keine Testdatenbank zwischen parallel ausgeführten Tests.
7. Richte diese Tests als bewusst getrennten Lauf ein. Fehlt die Testverbindung beim ausdrücklichen Aufruf, schlägt die Einrichtung mit einer verständlichen Meldung fehl; ein Lauf ohne ausgeführte SQL-Server-Tests ist kein erfolgreicher Datenbanknachweis.

## Einstieg mit lokalem SQL Server

Vom Repository-Wurzelordner; passe die API-Referenz bei deinem eigenen Projekt an:

```shell
dotnet new xunit -n AddressBook.SqlServer.Tests --framework net10.0
dotnet add AddressBook.SqlServer.Tests reference Beispiele/Adressbuch/Api/Api.csproj
dotnet add AddressBook.SqlServer.Tests package Microsoft.AspNetCore.Mvc.Testing --version 10.0.0
```

Die SQL-Server-EF-Abhängigkeit kommt über das Datenprojekt der API. Unter PowerShell legst du die Verbindung zur **eigenen lokalen Testinstanz** fest:

```powershell
$env:ADDRESSBOOK_TEST_SQLSERVER = 'Server=localhost\SQLEXPRESS;Database=master;Integrated Security=true;TrustServerCertificate=true'
dotnet test AddressBook.SqlServer.Tests/AddressBook.SqlServer.Tests.csproj --configuration Release
```

Die Factory ersetzt `master` durch den erzeugten Testdatenbanknamen, bevor sie den Context erstellt. Die Tests laufen erst, wenn du die Factory und Testmethoden implementiert hast. Verwende nicht die Connection String einer bestehenden Adressbuch- oder Produktionsdatenbank. Das lokale Vertrauen in das Entwicklungszertifikat ersetzt keine Zertifikatsprüfung für veröffentlichte Verbindungen.

## Welche Fälle bringen zusätzlichen Nutzen?

| Prüfung | Durchführung | Erwartung |
| --- | --- | --- |
| Migrationen | frische Datenbank migrieren, erneut migrieren | Schema entsteht; zweiter Lauf ohne neue Änderungen |
| Schema-Regeln | Alter `-1` direkt mit EF speichern | `DbUpdateException` durch Check Constraint |
| Persistenz | speichern, Context entsorgen, neuen Context öffnen | gleicher Kontakt mit derselben ID |
| ID-Vergabe | erstellen, löschen, erneut erstellen | IDs kollidieren nicht |
| SQL-Abfrage | LINQ-Suche, Sortierung und Begrenzung aus Stufe 5 ausführen | erwartete Ergebnismenge auf SQL Server |
| Textvergleich | Suche nach `Alice` und `alice` | Verhalten dokumentiert und mit gewünschter Kollation verglichen |

SQLite und SQL Server können bei Datentypen, Migrationen und Textvergleichen verschieden reagieren. Notiere daher die tatsächliche Kollation deiner Testdatenbank. Behaupte nicht, jeder SQL Server ignoriere automatisch Groß-/Kleinschreibung.

Nach einer erwarteten Speicher-Exception verwende für weitere Prüfungen einen neuen Context oder entferne den fehlgeschlagenen Eintrag aus dem Change Tracker. Sonst kann ein späterer `SaveChanges` denselben ungültigen Eintrag erneut schreiben.

## Gestufte Hinweise

Versuche zuerst eine eigene Lösung. Öffne bei Bedarf zunächst Hinweis 1 und erst danach Hinweis 2; die vorhandenen Beispiele bzw. Referenzen dienen anschließend zum Vergleichen.

<details>
<summary>Hinweis 1: Denkanstoß</summary>

Welche Regel wird von der Datenbank selbst erzwungen und welcher Test umgeht dafür die API-Validierung?

</details>

<details>
<summary>Hinweis 2: Vorgehensweise</summary>

Migriere eine frische Datenbank und speichere ein ungültiges Alter direkt über den Context; erwarte eine DbUpdateException.

</details>

## Selbst prüfen

Alle beschriebenen Fälle laufen auf SQL Server, einzeln und gemeinsam. Datenbanken bleiben auch nach einem absichtlich fehlgeschlagenen Test nicht zurück. Ein fehlender Server ergibt eine verständliche Einrichtungsfehlermeldung. Die SQLite-Tests funktionieren weiterhin ohne SQL Server. Deine Auswertung benennt, welcher zusätzliche Fehler durch die neue Prüfung erkennbar ist.

Abgabe: Testfixture, gezielte SQL-Server-Tests, dokumentierter Startbefehl und Vergleich der Aussagen beider Testarten. Du brauchst nicht alle HTTP-Testfälle zu duplizieren.

## Bonus innerhalb der Vertiefung: Testdatenbank im Container

**Intention:** Mache den zusätzlichen Testlauf unabhängig von einer manuell installierten Instanz. **Lernziel:** Du kannst eine separate SQL-Server-Testinstanz starten, auf Bereitschaft warten, ihre Verbindung an den Testhost geben und sie nach dem Lauf beenden.

Nach A05 kannst du einen eigenen SQL-Server-Testcontainer verwenden. Stelle einen nur lokal gebundenen Testport bereit oder führe Tests im selben Containernetz aus. Das bestehende Compose-Beispiel veröffentlicht den Datenbankport nicht und ist deshalb nicht unverändert aus dem Host-Testprozess erreichbar. Verwende für die Tests kein dauerhaftes Adressbuch-Volume. Automatisiere den Containerlauf in CI erst, nachdem der lokale Testlauf funktioniert.

## Passende Lernquellen

[Leseempfehlung für diesen Lernschritt](../Referenzen/Lernquellen.md#bonus-zugänglichkeit-und-datenbanktests). Wähle den dort genannten Abschnitt zur aktuellen Aufgabe und probiere ihn in deinem eigenen Programm aus.
