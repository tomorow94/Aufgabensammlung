# Aufgabe A04: GitHub Repository & Open Source Best Practices

## Einführung in Stufe 6: API & Webentwicklung

Nachdem wir eine **REST-API** und eine **Webanwendung** erstellt haben, geht es nun um die **Verwaltung und Bereitstellung des Projekts** mit **GitHub**.  
Versionskontrolle ist essenziell für die **Nachvollziehbarkeit von Änderungen** und die Zusammenarbeit mit anderen Entwicklern.  

Diese Aufgabe zeigt, wie man:
- **Das Projekt auf GitHub speichert und verwaltet**.
- **Eine professionelle README-Datei mit Dokumentation und Beispielen erstellt**.
- **Automatisierte Tests und Code-Qualitätsprüfungen integriert**.
- **Issues und Pull Requests für eine strukturierte Entwicklung nutzt**.

---

## Ziel

In dieser Aufgabe lernen Sie:
- **Wie GitHub für Versionskontrolle und Zusammenarbeit genutzt wird**.
- **Best Practices für Open Source-Projekte**, um professionelle Repositories zu erstellen.
- **Wie man Badges für Code-Qualität, Tests und Builds hinzufügt**.

---

## Anforderungen

1. **Projekt auf GitHub hochladen**
   - Erstellen Sie ein neues Repository auf GitHub.
   - **Fügen Sie eine `.gitignore`-Datei hinzu**, um unnötige Dateien auszuschließen.
   - Initialisieren Sie Git und laden Sie das Projekt hoch:
     ```shell
     git init
     git add .
     git commit -m "Initial commit"
     git branch -M main
     git remote add origin <Repository-URL>
     git push -u origin main
     ```

2. **README-Datei erstellen**
   - Eine ausführliche **README.md** mit folgenden Inhalten:
     - **Projektbeschreibung**: Worum geht es?
     - **Installation & Nutzung**: Wie wird das Projekt gestartet?
     - **API-Dokumentation**: Welche Endpunkte existieren?
     - **Beispiel-Requests und Screenshots**.

3. **Badges für Code-Qualität & Tests hinzufügen**
   - **SonarCloud für Code-Analyse**:
     - Erstellen Sie einen SonarCloud-Account und verbinden Sie das Repository.
     - Fügen Sie einen **Code-Qualitäts-Badge** in die README ein.
   - **GitHub Actions für automatische Tests**:
     - Workflow erstellen für `dotnet test` und `npm test` (falls JavaScript vorhanden).
     - Status-Badge für den Build in README einfügen.
   - **Bug-Tracking mit Issues**:
     - Einrichten von Labels (`Bug`, `Enhancement`, `Feature`).
     - Verlinkung in der README (`[Issues](https://github.com/user/repository/issues)`).

4. **Issues & Pull Requests für Entwicklungsstruktur nutzen**
   - Erstellen Sie mindestens ein **Issue**, um eine neue Funktion zu planen.
   - Erstellen Sie eine **Branch**, um Änderungen zu testen.
   - **Erstellen Sie einen Pull Request**, um Änderungen in `main` zu übernehmen.

---

## Hinweise

- **Ein sauberes Repository** zeigt Professionalität – vermeiden Sie unnötige Dateien (`bin/`, `.vs/`, `node_modules/`).
- **Eine gute README ist entscheidend** – Sie hilft neuen Entwicklern, sich schnell zurechtzufinden.
- **Pull Requests sollten überprüft werden**, bevor sie gemerged werden – nutzen Sie Reviews.

---

## Erweiterungsmöglichkeiten

- **GitHub Pages oder Netlify nutzen**, um die Webanwendung direkt zu hosten.
- **Automatische Deployments mit CI/CD**, um Änderungen direkt auf einen Server zu bringen.
- **Detaillierte CONTRIBUTING.md erstellen**, um externe Entwickler zur Zusammenarbeit einzuladen.

---

<details>
<summary><strong>Lösungsvorschlag anzeigen</strong></summary>

### **1. GitHub Repository initialisieren**
```shell
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/user/repository.git
git push -u origin main
```



### **2. Beispiel-README.md**
```markdown
# MyProject - Webanwendung mit API

## 🚀 Projektbeschreibung
Dieses Projekt ist eine Webanwendung mit einer REST-API in ASP.NET Core und einem Frontend mit HTML, CSS und JavaScript.

## 📌 Features
- REST-API mit CRUD-Funktionalität.
- Dynamische Benutzeroberfläche mit API-Anbindung.
- Deployment über GitHub Actions.

## 📥 Installation
\```shell
git clone https://github.com/user/repository.git
cd repository
dotnet run
\```

## 📡 API-Endpunkte
| **Methode** | **Endpunkt**             | **Beschreibung**                 |
|------------|-------------------------|---------------------------------|
| `GET`      | `/api/customers`        | Liste aller Kunden abrufen      |
| `POST`     | `/api/customers`        | Neuen Kunden erstellen          |
| `PUT`      | `/api/customers/{id}`   | Kunden aktualisieren            |
| `DELETE`   | `/api/customers/{id}`   | Kunden löschen                   |

## 🔗 Links
Live-Demo
Issues
SonarCloud Analyse
```

---

### **3. SonarCloud für Code-Analyse einrichten**
1. **SonarCloud-Account erstellen** → Repository hinzufügen.
2. **Token generieren & GitHub Actions Workflow anpassen**:
    ```yaml
   name: SonarCloud Analysis
   on:
     push:
       branches:
         - main
   jobs:
     sonar:
       runs-on: ubuntu-latest
       steps:
         - name: Checkout Repository
           uses: actions/checkout@v3
         - name: Setup .NET
           uses: actions/setup-dotnet@v1
           with:
             dotnet-version: 6.0
         - name: Run SonarCloud Scan
           run: dotnet sonarscanner begin /k:"user_project" /d:sonar.host.url="https://sonarcloud.io" /d:sonar.login="${{ secrets.SONAR_TOKEN }}"
    ```

### **4. Automatische Tests mit GitHub Actions**
```yaml
name: Build & Test

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v3

      - name: Setup .NET
        uses: actions/setup-dotnet@v1
        with:
          dotnet-version: 6.0

      - name: Run Tests
        run: dotnet test
```

### **5. Beispiel-Issue für neue Funktion**
```markdown
### Neue API-Funktion: Benutzergruppen erstellen
**Beschreibung**: Die API soll Benutzer in Gruppen verwalten können.
**Akzeptanzkriterien**:
- Ein Benutzer kann zu einer Gruppe hinzugefügt werden.
- Gruppen können per `GET /api/groups` abgerufen werden.
- Dokumentation in Swagger ergänzen.

**Labels**: `Enhancement`
**Priorität**: Mittel
```
</details>

