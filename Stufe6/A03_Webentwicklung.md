# Aufgabe A03: Webseite mit HTML, CSS und JavaScript – Einführung in Webentwicklung

## Einführung in Stufe 6: API & Webentwicklung

Nachdem wir in den vorherigen Aufgaben eine **REST-API** mit ASP.NET Core entwickelt und mit Tests abgesichert haben, benötigen wir nun eine Benutzeroberfläche.  
In dieser Aufgabe erstellen wir eine **einfache Webseite mit HTML, CSS und JavaScript**, die mit unserer API kommuniziert.  

Das Ziel ist es, die Grundlagen der **Frontend-Webentwicklung** zu verstehen und eine **dynamische Webseite** zu erstellen, die Daten von der API abruft und darstellt.

Die wichtigsten Konzepte in dieser Aufgabe sind:
- **HTML & CSS**: Strukturierung und Gestaltung der Webseite.
- **JavaScript & DOM-Manipulation**: Interaktive Inhalte erstellen.
- **API-Kommunikation**: Daten von der API abrufen und anzeigen.


<details>
<summary><strong>Einführung in HTML, CSS und JavaScript</strong></summary>

## **1. Was ist HTML?**
**HTML (Hypertext Markup Language)** ist die **Struktur** einer Webseite.  
Es beschreibt, welche **Elemente** auf einer Seite vorhanden sind, z. B. Überschriften, Absätze, Links oder Bilder.

### **Beispiel für ein einfaches HTML-Dokument:**
```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>Meine erste Webseite</title>
</head>
<body>
    <h1>Hallo Welt!</h1>
    <p>Das ist meine erste Webseite mit HTML.</p>
</body>
</html>
```

Wichtige HTML-Elemente:
| **Tag**               | **Beschreibung**                          |
|-----------------------|------------------------------------------|
| `<h1>` - `<h6>`      | Überschriften (h1 = größte, h6 = kleinste) |
| `<p>`                | Absatz (Paragraph)                        |
| `<a href="url">`     | Link zu einer anderen Seite              |
| `<img src="bild.jpg">` | Bild einfügen                           |
| `<ul><li></li></ul>` | Unsortierte Liste mit Einträgen          |

## **2. Was ist CSS?**
CSS (Cascading Style Sheets) bestimmt das Aussehen einer Webseite.
Es ermöglicht das Ändern von Farben, Schriftarten, Abständen, Layouts und mehr.

### Beispiel für CSS:
```css
body {
    background-color: lightgray;
    font-family: Arial, sans-serif;
}

h1 {
    color: blue;
    text-align: center;
}

p {
    font-size: 18px;
}
```

### Wie wird CSS eingebunden?
- Intern (im `<style>`-Tag in HTML)
- Extern (eine separate `styles.css`-Datei)
- Inline (direkt im HTML-Tag, sollte aber vermieden werden)

#### Externes CSS einbinden:

```html
<head>
    <link rel="stylesheet" href="styles.css">
</head>
```

## **3. Was ist JavaScript?**
JavaScript (JS) macht Webseiten interaktiv.
Damit kann man Buttons anklicken, Inhalte dynamisch laden, Eingaben validieren und vieles mehr.

### Beispiel für JavaScript:
```js
document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("btn").addEventListener("click", () => {
        alert("Hallo, das ist eine Interaktion mit JavaScript!");
    });
});
```

### JavaScript-Grundlagen:
| **Begriff**                | **Beschreibung**                          |
|----------------------------|------------------------------------------|
| `let` / `const`           | Variablen in JavaScript                 |
| `document.getElementById()` | Greift auf HTML-Elemente zu             |
| `addEventListener()`       | Reagiert auf Benutzeraktionen           |
| `fetch()`                  | Ruft Daten von einer API ab             |
| `console.log()`            | Gibt Werte in der Entwicklerkonsole aus |

## **4. JavaScript mit HTML verbinden**
JavaScript kann in einer separaten Datei (`script.js`) gespeichert und in HTML eingebunden werden:

```html
<script src="script.js"></script>
```
Dadurch bleibt der Code übersichtlich und wiederverwendbar.

## **5. API-Requests mit der Fetch API**
Webseiten können Daten aus einer API abrufen und anzeigen.

### Beispiel: Eine API-Abfrage mit Fetch
```js
fetch("https://jsonplaceholder.typicode.com/users")
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error("Fehler:", error));
```

Erklärung:

- `fetch(URL)` sendet eine Anfrage an die API.
- `.then(response => response.json())` verarbeitet die Antwort als JSON.
- `.catch(error => ...)` fängt Fehler ab.

</details> 

---

## Ziel

In dieser Aufgabe lernen Sie:
- **Grundlagen von HTML, CSS und JavaScript** für Webentwicklung.
- **Wie man API-Requests mit der Fetch API oder Axios durchführt**.
- **Wie man Daten aus der API in der Webseite darstellt**.

---

## Anforderungen

1. **Projektstruktur erstellen**
   - Arbeiten Sie in **Visual Studio Code** und legen Sie folgende Dateien an:
     ```
     /webapp
       ├── index.html
       ├── styles.css
       ├── script.js
     ```
   - **HTML für die Webseite** erstellen (`index.html`).
   - **CSS für das Layout** (`styles.css`).
   - **JavaScript für API-Aufrufe und Interaktivität** (`script.js`).

2. **HTML-Struktur für eine Benutzerverwaltung**
   - Erstellen Sie eine einfache **Tabelle oder Liste**, um Benutzer aus der API anzuzeigen.
   - Ein **Eingabefeld und ein Button**, um neue Benutzer hinzuzufügen.

3. **CSS zur Gestaltung der Webseite**
   - Nutzen Sie CSS für ein ansprechendes Layout (keine Inline-Styles).
   - Optional: Eine einfache **Button- und Tabellen-Formatierung**.

4. **JavaScript für API-Requests (Fetch API)**
   - **GET**-Request: Benutzerliste aus der API abrufen und anzeigen.
   - **POST**-Request: Neuen Benutzer hinzufügen.
   - **DELETE**-Request: Benutzer aus der Liste entfernen.

5. **Daten von der API abrufen & darstellen**
   - Verwenden Sie die Fetch API oder Axios, um mit der API zu kommunizieren.
   - JSON-Daten der API in eine HTML-Tabelle oder Liste einfügen.

---

## Hinweise

- **JavaScript-Logik trennen**: Halten Sie die API-Logik in `script.js`, statt Inline-Skripte in HTML zu verwenden.
- **Vermeiden Sie Seiten-Neuladen**: Nutzen Sie **`event.preventDefault()`**, um Formulare abzufangen.
- **Testen Sie die API vorab mit Postman oder im Browser**, um sicherzustellen, dass die Requests korrekt sind.

---

## Erweiterungsmöglichkeiten

- **Suchfunktion hinzufügen**: Lassen Sie Benutzer nach Namen filtern.
- **Dynamisches CSS**: Ändern Sie das Design basierend auf der API-Antwort.
- **Animations- oder Ladeeffekte**: Zeigen Sie ein „Lädt…“ an, während Daten abgerufen werden.

---

<details>
<summary><strong>Lösungsvorschlag anzeigen</strong></summary>

### **1. HTML-Grundstruktur**
```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Benutzerverwaltung</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Benutzerverwaltung</h1>
    <form id="userForm">
        <input type="text" id="username" placeholder="Benutzername eingeben" required>
        <button type="submit">Benutzer hinzufügen</button>
    </form>
    <ul id="userList"></ul>
    <script src="script.js"></script>
</body>
</html>
```

### **2. CSS für Layout & Buttons**
```css
body {
    font-family: Arial, sans-serif;
    text-align: center;
}

button {
    background-color: #28a745;
    color: white;
    border: none;
    padding: 10px 15px;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}
```

### **3. JavaScript für API-Requests**
```js
document.addEventListener("DOMContentLoaded", () => {
    const apiUrl = "http://localhost:5000/api/customers"; // URL zur API
    const userList = document.getElementById("userList");
    const userForm = document.getElementById("userForm");
    const usernameInput = document.getElementById("username");

    async function fetchUsers() {
        try {
            const response = await fetch(apiUrl);
            const users = await response.json();
            userList.innerHTML = ""; 
            users.forEach(user => {
                const li = document.createElement("li");
                li.textContent = `${user.name} (${user.id})`;
                
                const deleteBtn = document.createElement("button");
                deleteBtn.textContent = "Löschen";
                deleteBtn.onclick = () => deleteUser(user.id);
                
                li.appendChild(deleteBtn);
                userList.appendChild(li);
            });
        } catch (error) {
            console.error("Fehler beim Abrufen der Benutzer:", error);
        }
    }

    async function addUser(event) {
        event.preventDefault();
        const username = usernameInput.value.trim();
        if (!username) return;

        try {
            await fetch(apiUrl, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ name: username })
            });
            usernameInput.value = "";
            fetchUsers(); 
        } catch (error) {
            console.error("Fehler beim Hinzufügen des Benutzers:", error);
        }
    }

    async function deleteUser(id) {
        try {
            await fetch(`${apiUrl}/${id}`, { method: "DELETE" });
            fetchUsers(); 
        } catch (error) {
            console.error("Fehler beim Löschen des Benutzers:", error);
        }
    }

    userForm.addEventListener("submit", addUser);
    fetchUsers(); 
});
```
</details>
