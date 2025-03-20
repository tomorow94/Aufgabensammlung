# Aufgabe A02: Datenbank-Anbindung mit Microsoft SQL Server Express

## Ziel

In dieser Aufgabe lernen Sie die Grundlagen relationaler Datenbanken und erstellen eine **C#-Konsolenanwendung**, die mit **Microsoft SQL Server Express** kommuniziert.  
Dabei lernen Sie:
- **Das Konzept relationaler Datenbanken** und wie Tabellen miteinander verknüpft sind.
- **SQL-Abfragen** für CRUD-Operationen (**Create, Read, Update, Delete**).
- **Wie eine C#-Anwendung mit einer Datenbank interagiert**.

---

## Einführung: Was ist eine relationale Datenbank?

Eine **relationale Datenbank** speichert Daten in **Tabellen**, die aus **Zeilen** (Datensätze) und **Spalten** (Attribute) bestehen.  
Jede Zeile ist ein Datensatz, und Spalten definieren die Eigenschaften dieses Datensatzes.

### **Entity-Relationship-Modell (ERM)**

Bevor man eine Datenbank erstellt, wird oft ein **ERM-Diagramm** genutzt, um die Beziehungen zwischen den Tabellen zu planen.  
Ein Beispiel für eine einfache Datenbankstruktur:

**Tabelle: `Customers`**  
| CustomerID | Name        | Email              |
|-----------|------------|--------------------|
| 1         | Alice Smith | alice@mail.com    |
| 2         | Bob Johnson | bob@mail.com      |

**Tabelle: `Orders`**  
| OrderID | CustomerID | Product  | Amount |
|--------|-----------|----------|--------|
| 101    | 1         | Laptop   | 1200€  |
| 102    | 2         | Smartphone | 800€  |

💡 **`CustomerID` ist der "Primärschlüssel" in `Customers` und "Fremdschlüssel" in `Orders`, was die Beziehung zwischen den Tabellen herstellt.**

---

## Anforderungen

1. **SQL Server Express installieren & Datenbank anlegen**
   - Installieren Sie **Microsoft SQL Server Express** (falls nicht vorhanden).
   - Erstellen Sie eine **Datenbank** mit einer Tabelle `Customers`:
     - `CustomerID` (Primärschlüssel, Auto-Increment)
     - `Name` (VARCHAR)
     - `Email` (VARCHAR)

2. **C#-Anwendung für CRUD-Operationen**
   - **Create**: Einen neuen Kunden hinzufügen.
   - **Read**: Alle Kunden aus der Datenbank abrufen.
   - **Update**: E-Mail eines Kunden aktualisieren.
   - **Delete**: Einen Kunden löschen.

3. **SQL-Verbindung in C# herstellen**
   - Nutzen Sie `SqlConnection` aus `System.Data.SqlClient`, um mit der Datenbank zu kommunizieren.
   - Verwenden Sie `SqlCommand`, um SQL-Abfragen auszuführen.

---

## Hinweise

- **SQL Server Management Studio (SSMS)** kann genutzt werden, um die Datenbank zu verwalten.
- **SQL-Abfragen testen**: Bevor Sie die Abfragen in C# einbauen, testen Sie sie direkt in SSMS.
- Nutzen Sie **Prepared Statements (`SqlParameter`)**, um **SQL-Injection** zu vermeiden.

<details>
<summary><strong>Anleitung: Erste Schritte mit SQL Server Management Studio (SSMS) und C#</strong></summary>

## **1. Installation von Microsoft SQL Server Express und SSMS**
Falls Sie Microsoft SQL Server Express und SSMS noch nicht installiert haben, können Sie diese hier herunterladen:
- **SQL Server Express**: [Download-Link](https://www.microsoft.com/de-de/sql-server/sql-server-downloads)
- **SQL Server Management Studio (SSMS)**: [Download-Link](https://aka.ms/ssmsfullsetup)

Nach der Installation starten Sie **SQL Server Management Studio (SSMS)** und verbinden sich mit Ihrem lokalen SQL Server.

---

## **2. Verbindung mit dem SQL Server in SSMS**
1. Öffnen Sie **SSMS**.
2. Wählen Sie im Verbindungsdialog:
   - **Servertyp**: `Datenbank-Engine`
   - **Servername**: `localhost\SQLEXPRESS` (Standard für SQL Server Express)
   - **Authentifizierung**: `Windows-Authentifizierung`
3. Klicken Sie auf **Verbinden**.

Falls die Verbindung fehlschlägt, prüfen Sie:
- Ob der **SQL Server-Dienst** läuft (`SQL Server Configuration Manager`).
- Ob `SQLEXPRESS` tatsächlich installiert ist (ggf. mit `.\SQLEXPRESS` oder nur `localhost` testen).

---

## **3. Neue Datenbank in SSMS anlegen**
1. Klicken Sie mit der rechten Maustaste auf **Datenbanken** → **Neue Datenbank…**
2. Geben Sie den Namen **CustomerDB** ein.
3. Klicken Sie auf **OK**.

---

## **4. Tabelle in SSMS erstellen**
Nachdem die Datenbank erstellt wurde:
1. Erweitern Sie die Datenbank **CustomerDB** → **Tabellen**.
2. Rechtsklick auf **Tabellen** → **Neue Tabelle**.
3. Fügen Sie folgende Spalten hinzu:
   - `CustomerID` (Typ: `INT`, **Primärschlüssel**, Auto-Increment: `IDENTITY(1,1)`)
   - `Name` (Typ: `NVARCHAR(100)`, **nicht null**)
   - `Email` (Typ: `NVARCHAR(100)`, **nicht null**)
4. Speichern Sie die Tabelle unter dem Namen **Customers**.

Oder alternativ per **SQL-Skript:**
```sql
CREATE TABLE Customers (
    CustomerID INT IDENTITY(1,1) PRIMARY KEY,
    Name NVARCHAR(100) NOT NULL,
    Email NVARCHAR(100) NOT NULL
);
```

Führen Sie dieses SQL-Skript in SSMS aus, um die Tabelle zu erstellen.

## **5. Verbindung zur SQL-Datenbank in einer C#-Anwendung**
Um mit der Datenbank aus einer C#-Anwendung zu kommunizieren, benötigen Sie die Connection String-Informationen.

Ein typischer Connection String für SQL Server Express:

```csharp
string connectionString = "Server=localhost\\SQLEXPRESS;Database=CustomerDB;Trusted_Connection=True;";
```

Falls Sie SQL-Authentifizierung verwenden, müssen Sie Benutzername und Passwort hinzufügen:

```csharp
string connectionString = "Server=localhost\\SQLEXPRESS;Database=CustomerDB;User Id=meinBenutzer;Password=meinPasswort;";
```

Beispiel für eine Verbindung und eine einfache SQL-Abfrage in C#:
```csharp
using System;
using System.Data.SqlClient;

class Program
{
    static void Main()
    {
        string connectionString = "Server=localhost\\SQLEXPRESS;Database=CustomerDB;Trusted_Connection=True;";

        using (SqlConnection conn = new SqlConnection(connectionString))
        {
            conn.Open();
            Console.WriteLine("Verbindung erfolgreich!");

            string query = "SELECT COUNT(*) FROM Customers";
            using (SqlCommand cmd = new SqlCommand(query, conn))
            {
                int count = (int)cmd.ExecuteScalar();
                Console.WriteLine($"Anzahl der Kunden: {count}");
            }
        }
    }
}
```

## **6. Testen der Verbindung**
1. Starten Sie das C#-Programm.
2. Falls die Verbindung fehlschlägt, überprüfen Sie:
    - Ob der SQL Server-Dienst läuft.
    - Ob die Datenbank- und Tabellen-Namen korrekt sind.
    - Ob `SQLEXPRESS` korrekt als Servername eingetragen wurde.
Diese Anleitung gibt Ihnen eine Schritt-für-Schritt-Erklärung, wie Sie eine SQL-Datenbank erstellen, in SSMS verwalten und mit C# darauf zugreifen können! 🚀

</details>

---

## Erweiterungsmöglichkeiten

- **Weitere Tabellen hinzufügen**: Eine `Orders`-Tabelle mit Kundenverknüpfung erstellen.
- **GUI-Integration**: Eine **Windows Forms- oder WPF-Oberfläche** zur Verwaltung der Datenbank.
- **Logging**: Änderungen in einer Log-Tabelle speichern.

---

<details>
<summary><strong>Lösungsvorschlag anzeigen</strong></summary>

### **1. SQL-Datenbank & Tabelle anlegen**
```sql
CREATE DATABASE CustomerDB;
USE CustomerDB;

CREATE TABLE Customers (
    CustomerID INT IDENTITY(1,1) PRIMARY KEY,
    Name NVARCHAR(100),
    Email NVARCHAR(100)
);
```
2. C#-Code für die Datenbankverbindung & CRUD-Operationen

```csharp
using System;
using System.Data.SqlClient;

class Program
{
    static string connectionString = "Server=localhost\\SQLEXPRESS;Database=CustomerDB;Trusted_Connection=True;";

    static void Main()
    {
        bool running = true;
        while (running)
        {
            Console.WriteLine("\n===== Customer Management =====");
            Console.WriteLine("1. Add Customer");
            Console.WriteLine("2. View Customers");
            Console.WriteLine("3. Update Email");
            Console.WriteLine("4. Delete Customer");
            Console.WriteLine("5. Exit");
            Console.Write("Choose an option: ");

            switch (Console.ReadLine())
            {
                case "1":
                    AddCustomer();
                    break;
                case "2":
                    ViewCustomers();
                    break;
                case "3":
                    UpdateEmail();
                    break;
                case "4":
                    DeleteCustomer();
                    break;
                case "5":
                    running = false;
                    break;
                default:
                    Console.WriteLine("Invalid selection.");
                    break;
            }
        }
    }

    static void AddCustomer()
    {
        Console.Write("Enter name: ");
        string name = Console.ReadLine();
        Console.Write("Enter email: ");
        string email = Console.ReadLine();

        using (SqlConnection conn = new SqlConnection(connectionString))
        {
            conn.Open();
            string query = "INSERT INTO Customers (Name, Email) VALUES (@name, @email)";
            using (SqlCommand cmd = new SqlCommand(query, conn))
            {
                cmd.Parameters.AddWithValue("@name", name);
                cmd.Parameters.AddWithValue("@email", email);
                cmd.ExecuteNonQuery();
            }
        }
        Console.WriteLine("Customer added.");
    }

    static void ViewCustomers()
    {
        using (SqlConnection conn = new SqlConnection(connectionString))
        {
            conn.Open();
            string query = "SELECT * FROM Customers";
            using (SqlCommand cmd = new SqlCommand(query, conn))
            using (SqlDataReader reader = cmd.ExecuteReader())
            {
                Console.WriteLine("\nCustomers:");
                while (reader.Read())
                {
                    Console.WriteLine($"{reader["CustomerID"]}: {reader["Name"]} - {reader["Email"]}");
                }
            }
        }
    }

    static void UpdateEmail()
    {
        Console.Write("Enter customer ID: ");
        if (int.TryParse(Console.ReadLine(), out int id))
        {
            Console.Write("Enter new email: ");
            string newEmail = Console.ReadLine();

            using (SqlConnection conn = new SqlConnection(connectionString))
            {
                conn.Open();
                string query = "UPDATE Customers SET Email = @email WHERE CustomerID = @id";
                using (SqlCommand cmd = new SqlCommand(query, conn))
                {
                    cmd.Parameters.AddWithValue("@id", id);
                    cmd.Parameters.AddWithValue("@email", newEmail);
                    int rowsAffected = cmd.ExecuteNonQuery();
                    Console.WriteLine(rowsAffected > 0 ? "Email updated." : "Customer not found.");
                }
            }
        }
    }

    static void DeleteCustomer()
    {
        Console.Write("Enter customer ID to delete: ");
        if (int.TryParse(Console.ReadLine(), out int id))
        {
            using (SqlConnection conn = new SqlConnection(connectionString))
            {
                conn.Open();
                string query = "DELETE FROM Customers WHERE CustomerID = @id";
                using (SqlCommand cmd = new SqlCommand(query, conn))
                {
                    cmd.Parameters.AddWithValue("@id", id);
                    int rowsAffected = cmd.ExecuteNonQuery();
                    Console.WriteLine(rowsAffected > 0 ? "Customer deleted." : "Customer not found.");
                }
            }
        }
    }
}
```
</details> 
