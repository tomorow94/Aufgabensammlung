# Aufgabe A03: ORM für vereinfachten Datenbankzugriff – Einführung in ORM und LINQ

## Ziel

In dieser Aufgabe lernen Sie, wie **Object-Relational Mapping (ORM)** den Zugriff auf relationale Datenbanken in C# vereinfacht.  
Zusätzlich wird **LINQ (Language Integrated Query)** genutzt, um Datenbankabfragen auf **objektorientierte Weise** auszuführen.

Dabei lernen Sie:
- **Grundlagen von ORM**: Wie ORM den Zugriff auf Datenbanktabellen erleichtert.
- **LINQ-Abfragen**, um CRUD-Operationen (Create, Read, Update, Delete) effizient auszuführen.
- **DbContext und DbSet** zur Verwaltung der Datenbank in einer C#-Anwendung.

---

## Einführung: Was ist Object-Relational Mapping (ORM)?

**ORM** ermöglicht es, Datenbanktabellen als **C#-Klassen** zu modellieren.  
Anstatt SQL-Abfragen zu schreiben, wird direkt mit Objekten gearbeitet.

**Beispiel für eine einfache SQL-Abfrage vs. LINQ:**
| **SQL** | **LINQ mit Entity Framework** |
|------------------------------|-----------------|
| `SELECT * FROM Customers WHERE Name = 'Alice';` | `context.Customers.Where(c => c.Name == "Alice").ToList();` |
| `INSERT INTO Customers (Name, PhoneNumber) VALUES ('Bob', '123456');` | `context.Customers.Add(new Customer { Name = "Bob", PhoneNumber = "123456" }); context.SaveChanges();` |
| `UPDATE Customers SET Name = 'Charlie' WHERE ID = 1;` | `customer.Name = "Charlie"; context.SaveChanges();` |

---

## Anforderungen

1. **ORM-Framework in das Projekt integrieren**
   - Nutzen Sie **Entity Framework Core** als ORM.
   - Installieren Sie über NuGet:
     ```shell
     Install-Package Microsoft.EntityFrameworkCore.SqlServer
     ```
   - Erstellen Sie eine **Datenbankverbindung** mit einer **DbContext-Klasse**.

2. **ORM-Klasse für Kunden anlegen**
   - Erstellen Sie eine ORM-Klasse `Customer`, die der SQL-Tabelle entspricht:
     - `CustomerID` (Primärschlüssel)
     - `Name` (String)
     - `PhoneNumber` (String)

3. **CRUD-Operationen mit LINQ**
   - **Create**: Kunden hinzufügen.
   - **Read**: Alle Kunden anzeigen, nach Namen suchen.
   - **Update**: Kundendaten ändern.
   - **Delete**: Kunde entfernen.

4. **Komplexere LINQ-Abfragen nutzen**
   - Kunden alphabetisch sortieren.
   - Kunden anzeigen, deren Name mit einem bestimmten Buchstaben beginnt.

5. **Anwendungslogik in einer Konsolen-App**
   - Der Benutzer kann Kunden verwalten, ohne SQL schreiben zu müssen.

---

## Hinweise

- ORM-Frameworks erstellen **automatisch Tabellen** basierend auf den definierten Klassen.
- **LINQ-Abfragen** vereinfachen das Arbeiten mit der Datenbank.
- **DbContext** verwaltet die Verbindung zur Datenbank und wird für Abfragen genutzt.

---

## Erweiterungsmöglichkeiten

- **Mehr Tabellen hinzufügen**: Beziehungen zwischen `Customers` und `Orders` definieren.
- **GUI-Anbindung**: Windows Forms oder WPF für eine visuelle Benutzeroberfläche.
- **Erweiterte Abfragen**: Kunden nach Telefonnummer filtern, Paginierung einbauen.

---

<details>
<summary><strong>Lösungsvorschlag anzeigen</strong></summary>

### **1. ORM-Datenbankverbindung einrichten**
```csharp
using Microsoft.EntityFrameworkCore;

public class CustomerContext : DbContext
{
    public DbSet<Customer> Customers { get; set; }

    protected override void OnConfiguring(DbContextOptionsBuilder options)
    {
        options.UseSqlServer("Server=localhost\\SQLEXPRESS;Database=OrmDatabase;Trusted_Connection=True;");
    }
}
```

### **2. ORM-Klasse für Customer**
```csharp
public class Customer
{
    public int CustomerID { get; set; }
    public string Name { get; set; }
    public string PhoneNumber { get; set; }
}
```

### **3. CRUD-Operationen mit LINQ**
```csharp
using System;
using System.Linq;

class Program
{
    static void Main()
    {
        using (var context = new CustomerContext())
        {
            context.Database.EnsureCreated(); // Erstellt die Datenbank, falls nicht vorhanden.

            bool running = true;
            while (running)
            {
                Console.WriteLine("\n===== Customer Management =====");
                Console.WriteLine("1. Add Customer");
                Console.WriteLine("2. View Customers");
                Console.WriteLine("3. Search Customers by Name");
                Console.WriteLine("4. Update Customer");
                Console.WriteLine("5. Delete Customer");
                Console.WriteLine("6. Exit");
                Console.Write("Choose an option: ");

                switch (Console.ReadLine())
                {
                    case "1":
                        AddCustomer(context);
                        break;
                    case "2":
                        ViewCustomers(context);
                        break;
                    case "3":
                        SearchCustomers(context);
                        break;
                    case "4":
                        UpdateCustomer(context);
                        break;
                    case "5":
                        DeleteCustomer(context);
                        break;
                    case "6":
                        running = false;
                        break;
                    default:
                        Console.WriteLine("Invalid selection.");
                        break;
                }
            }
        }
    }

    static void AddCustomer(CustomerContext context)
    {
        Console.Write("Enter name: ");
        string name = Console.ReadLine();
        Console.Write("Enter phone number: ");
        string phone = Console.ReadLine();

        var customer = new Customer { Name = name, PhoneNumber = phone };
        context.Customers.Add(customer);
        context.SaveChanges();
        Console.WriteLine("Customer added.");
    }

    static void ViewCustomers(CustomerContext context)
    {
        var customers = context.Customers.OrderBy(c => c.Name).ToList();
        Console.WriteLine("\nCustomers:");
        foreach (var customer in customers)
        {
            Console.WriteLine($"{customer.CustomerID}: {customer.Name} - {customer.PhoneNumber}");
        }
    }

    static void SearchCustomers(CustomerContext context)
    {
        Console.Write("Enter name to search: ");
        string name = Console.ReadLine();

        var results = context.Customers.Where(c => c.Name.Contains(name)).ToList();
        if (results.Any())
        {
            Console.WriteLine("\nSearch Results:");
            foreach (var customer in results)
            {
                Console.WriteLine($"{customer.CustomerID}: {customer.Name} - {customer.PhoneNumber}");
            }
        }
        else
        {
            Console.WriteLine("No customers found.");
        }
    }

    static void UpdateCustomer(CustomerContext context)
    {
        Console.Write("Enter customer ID to update: ");
        if (int.TryParse(Console.ReadLine(), out int id))
        {
            var customer = context.Customers.Find(id);
            if (customer != null)
            {
                Console.Write("Enter new name: ");
                customer.Name = Console.ReadLine();
                Console.Write("Enter new phone number: ");
                customer.PhoneNumber = Console.ReadLine();
                context.SaveChanges();
                Console.WriteLine("Customer updated.");
            }
            else
            {
                Console.WriteLine("Customer not found.");
            }
        }
    }

    static void DeleteCustomer(CustomerContext context)
    {
        Console.Write("Enter customer ID to delete: ");
        if (int.TryParse(Console.ReadLine(), out int id))
        {
            var customer = context.Customers.Find(id);
            if (customer != null)
            {
                context.Customers.Remove(customer);
                context.SaveChanges();
                Console.WriteLine("Customer deleted.");
            }
            else
            {
                Console.WriteLine("Customer not found.");
            }
        }
    }
}
```

</details>
