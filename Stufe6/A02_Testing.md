# Aufgabe A02: Unit Testing & Integration Testing für die API

## Einführung in Stufe 6: API & Webentwicklung

Nachdem wir in der vorherigen Aufgabe eine **REST-API** mit ASP.NET Core entwickelt haben, ist es wichtig sicherzustellen, dass sie fehlerfrei funktioniert.  
Dafür nutzen wir **automatisierte Tests**, um die API kontinuierlich zu überprüfen.  

In dieser Aufgabe wird das **Testen der API** behandelt. Dabei unterscheiden wir zwischen:
- **Unit-Tests**: Testen **einzelne Methoden oder Klassen** unabhängig von der API.
- **Integration-Tests**: Testen die API **als Ganzes**, inklusive Datenbank- und HTTP-Kommunikation.

Diese Tests helfen, Fehler frühzeitig zu erkennen und ermöglichen eine **zuverlässige API-Entwicklung**.

---

## Ziel

In dieser Aufgabe lernen Sie:
- **Wie Unit-Tests mit xUnit oder NUnit in ASP.NET Core erstellt werden**.
- **Wie Integration-Tests mit ASP.NET TestServer oder Postman/Newman funktionieren**.
- **Die Grundlagen von Test Driven Development (TDD)** (optional).

---

## Anforderungen

1. **Testprojekt für Unit-Tests erstellen**
   - Legen Sie ein neues **xUnit- oder NUnit-Testprojekt** in Visual Studio an.
   - Installieren Sie das NuGet-Paket für xUnit:
     ```shell
     Install-Package xUnit
     ```
   - Testen Sie **die Logik der API unabhängig von HTTP**.

2. **Unit-Tests für API-Controller schreiben**
   - Testen Sie die Geschäftslogik, z. B.:
     - **Ob Kunden korrekt hinzugefügt werden**.
     - **Ob eine Fehlerbehandlung erfolgt, wenn Daten fehlen**.

3. **Integration-Tests mit ASP.NET TestServer durchführen**
   - Nutzen Sie `Microsoft.AspNetCore.Mvc.Testing` für Tests ohne echten Webserver.
   - Führen Sie API-Tests durch, die echte HTTP-Requests simulieren.

4. **Optional: Test Driven Development (TDD)**
   - Entwickeln Sie eine neue API-Funktion zuerst als **Testfall** und implementieren Sie sie dann.

---

## Hinweise

- **Unit-Tests sollten unabhängig von der Datenbank sein**. Nutzen Sie Mocking-Techniken mit **Moq** oder **Fake-Daten**.
- **Integration-Tests verwenden eine In-Memory-Datenbank**, um echte API-Aufrufe zu simulieren.
- **Tests automatisch ausführen**: Nutzen Sie GitHub Actions oder Azure DevOps, um die Tests nach jedem Code-Commit laufen zu lassen.

---

## Erweiterungsmöglichkeiten

- **Performance-Tests**: API-Reaktionszeiten mit Tools wie **JMeter** messen.
- **API-Testautomatisierung mit Postman/Newman**: API-Tests als Skript ausführen lassen.
- **Fehlermanagement testen**: Absichern, dass API-Anfragen sauber validiert werden.

---

<details>
<summary><strong>Lösungsvorschlag anzeigen</strong></summary>

### **1. Testprojekt erstellen**
1. In **Visual Studio** → Neues Projekt → **xUnit Test Project**.
2. Fügen Sie eine Referenz zum API-Projekt hinzu.
3. Installieren Sie xUnit und ASP.NET TestServer:
   ```shell
   Install-Package Microsoft.AspNetCore.Mvc.Testing
   Install-Package xUnit
    ```


### **2. Unit-Test für die API-Logik**
```csharp
using Xunit;
using MyRestApi.Controllers;
using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;

public class CustomersControllerTests
{
    [Fact]
    public void GetCustomers_ReturnsListOfCustomers()
    {
        var controller = new CustomersController();
        var result = controller.GetCustomers();
        var okResult = Assert.IsType<OkObjectResult>(result.Result);
        var customers = Assert.IsType<List<Customer>>(okResult.Value);
        Assert.NotEmpty(customers);
    }
}
```

### **3. Integration-Test für die API mit TestServer**
```csharp
using System.Net.Http;
using System.Threading.Tasks;
using Xunit;
using Microsoft.AspNetCore.Mvc.Testing;

public class CustomerApiTests : IClassFixture<WebApplicationFactory<Program>>
{
    private readonly HttpClient _client;

    public CustomerApiTests(WebApplicationFactory<Program> factory)
    {
        _client = factory.CreateClient();
    }

    [Fact]
    public async Task GetCustomers_ReturnsSuccess()
    {
        var response = await _client.GetAsync("/api/customers");
        response.EnsureSuccessStatusCode();
    }
}
```

### **4. Automatische API-Tests mit Postman/Newman (optional)**
1. Postman-Tests exportieren.
2. Newman CLI installieren:
```shell
npm install -g newman
```
3. Tests in der CI/CD-Pipeline ausführen:
```shell
newman run my_api_tests.json
```
</details>
