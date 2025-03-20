# Aufgabe A01: Erstellen einer REST-API in C# mit ASP.NET Core

## Einführung in Stufe 6: API & Webentwicklung

In dieser finalen Stufe des Projekts wird eine **vollständige Webanwendung** erstellt.  
Der erste Schritt besteht darin, eine **REST-API** mit ASP.NET Core zu entwickeln, die **alle bisher erstellten Funktionen** als Endpunkte bereitstellt.  
Später wird diese API von einer Webanwendung genutzt, um Benutzereingaben zu ermöglichen und Daten anzuzeigen.

Die API bildet die **Grundlage für die gesamte Webanwendung**, indem sie folgende Anforderungen erfüllt:
- **Bereitstellung von CRUD-Funktionen** für Datenbanken und bisherige Programmfunktionen.
- **RESTful-Architektur** mit standardisierten HTTP-Methoden.
- **Automatische API-Dokumentation** mit Swagger.

Diese Aufgabe konzentriert sich auf die **Erstellung der API und das Bereitstellen von Endpunkten**.

---

## Ziel

In dieser Aufgabe entwickeln Sie eine **REST-API** in **ASP.NET Core**.  
Dabei lernen Sie:
- **Grundlagen der REST-Architektur** und wie APIs funktionieren.
- **HTTP-Methoden** (`GET`, `POST`, `PUT`, `DELETE`).
- **Erstellen und Dokumentieren von API-Endpunkten** mit Swagger.

---

## Anforderungen

1. **Neues ASP.NET Core-Projekt erstellen**
   - Erstellen Sie eine **ASP.NET Core Web API**-Anwendung in Visual Studio.
   - Nutzen Sie das **Minimal API- oder Controller-Modell**.

2. **API-Endpunkte für bestehende Funktionen bereitstellen**
   - Nutzen Sie die bisher entwickelten Funktionen als **Datenquellen**.
   - Implementieren Sie CRUD-Operationen für ein Beispielmodell (z. B. `Customer`).

3. **REST-Architektur umsetzen**
   - **GET**: Daten abrufen (`api/customers`).
   - **POST**: Neue Daten hinzufügen (`api/customers`).
   - **PUT**: Bestehende Daten aktualisieren (`api/customers/{id}`).
   - **DELETE**: Daten löschen (`api/customers/{id}`).

4. **Swagger für API-Dokumentation integrieren**
   - Installieren Sie `Swashbuckle.AspNetCore` über NuGet.
   - Fügen Sie Swagger zur API hinzu, um Endpunkte zu dokumentieren.

---

## Hinweise

- **Verwenden Sie Dependency Injection**, um Datenbankzugriffe und Services sauber zu trennen.
- **Nutzen Sie JSON als Datenformat**, da es der Standard für REST-APIs ist.
- **Testen Sie Endpunkte mit Postman oder Swagger**, bevor Sie die API in die Webanwendung integrieren.

---

## Erweiterungsmöglichkeiten

- **Authentifizierung hinzufügen**: Absichern der API mit JWT-Token.
- **Logging und Fehlerbehandlung**: Zentrale Verwaltung von Fehlern und Logs.
- **Rate Limiting & Caching**: API-Leistung optimieren durch Zwischenspeicherung von Antworten.

---

<details>
<summary><strong>Lösungsvorschlag anzeigen</strong></summary>

### **1. Neues ASP.NET Core API-Projekt erstellen**
1. **Visual Studio öffnen** → Neues Projekt erstellen → **ASP.NET Core Web API** auswählen.
2. Projektname: **"MyRestApi"**.
3. Framework: **.NET 6+** auswählen.
4. Swagger aktivieren (`Enable OpenAPI support` ankreuzen).

---

### **2. Beispielmodell für die API**
```csharp
public class Customer
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string Email { get; set; }
}
```

### **3. API-Controller mit CRUD-Methoden**

```csharp
using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using System.Linq;

[Route("api/customers")]
[ApiController]
public class CustomersController : ControllerBase
{
    private static List<Customer> customers = new List<Customer>
    {
        new Customer { Id = 1, Name = "Alice", Email = "alice@mail.com" },
        new Customer { Id = 2, Name = "Bob", Email = "bob@mail.com" }
    };

    [HttpGet]
    public ActionResult<IEnumerable<Customer>> GetCustomers()
    {
        return Ok(customers);
    }

    [HttpGet("{id}")]
    public ActionResult<Customer> GetCustomer(int id)
    {
        var customer = customers.FirstOrDefault(c => c.Id == id);
        if (customer == null) return NotFound();
        return Ok(customer);
    }

    [HttpPost]
    public ActionResult AddCustomer([FromBody] Customer newCustomer)
    {
        newCustomer.Id = customers.Count + 1;
        customers.Add(newCustomer);
        return CreatedAtAction(nameof(GetCustomer), new { id = newCustomer.Id }, newCustomer);
    }

    [HttpPut("{id}")]
    public ActionResult UpdateCustomer(int id, [FromBody] Customer updatedCustomer)
    {
        var customer = customers.FirstOrDefault(c => c.Id == id);
        if (customer == null) return NotFound();
        
        customer.Name = updatedCustomer.Name;
        customer.Email = updatedCustomer.Email;
        return NoContent();
    }

    [HttpDelete("{id}")]
    public ActionResult DeleteCustomer(int id)
    {
        var customer = customers.FirstOrDefault(c => c.Id == id);
        if (customer == null) return NotFound();

        customers.Remove(customer);
        return NoContent();
    }
}
```

### **4. Swagger aktivieren**

Öffnen Sie Program.cs und fügen Sie Swagger hinzu:

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();
var app = builder.Build();

if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseAuthorization();
app.MapControllers();
app.Run();
```

Starten Sie die API, öffnen Sie den Browser und rufen Sie Swagger auf:
```bash
http://localhost:5000/swagger
```

Testen Sie die API-Endpunkte direkt in der Swagger-Oberfläche.

</details>
