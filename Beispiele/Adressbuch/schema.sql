-- In SSMS zuerst eine leere Datenbank AddressBook anlegen und auswählen.
CREATE TABLE Contacts (
    Id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
    Name NVARCHAR(100) NOT NULL,
    Age INT NOT NULL CHECK (Age BETWEEN 0 AND 130),
    Gender INT NOT NULL CHECK (Gender BETWEEN 0 AND 3),
    PhoneNumber NVARCHAR(50) NOT NULL,
    Email NVARCHAR(200) NOT NULL
);
