# Aufgabe A05: Deployment & Abschlussprojekt

## Einführung in Stufe 6: API & Webentwicklung

Nachdem die **REST-API entwickelt, getestet und mit einer Webanwendung verbunden wurde**, ist der letzte Schritt das **Deployment**.  
Das bedeutet, dass die Anwendung nicht mehr nur lokal läuft, sondern **auf einem Server oder in der Cloud** verfügbar ist.  

Ziel ist es, die **API und das Web-Frontend zu hosten**, sodass es von überall erreichbar ist.  
Zum Abschluss reflektieren wir das gesamte Projekt und überlegen, welche **Erweiterungen oder Verbesserungen** noch möglich sind.

---

## Ziel

In dieser Aufgabe lernen Sie:
- **Wie eine Webanwendung und API online bereitgestellt werden**.
- **Die Grundlagen von Deployment-Strategien**, z. B. Hosting über **Docker, Azure oder Netlify**.
- **Wie man eine finale Reflexion über das Projekt durchführt**.

---

## Anforderungen

1. **API und Webanwendung deployen**
   - **Option 1: Lokales Hosting mit Docker**:
     - Container für die API und das Frontend erstellen.
   - **Option 2: Deployment auf einem Cloud-Dienst (Azure, Netlify, Vercel)**.
   - **Option 3: Deployment auf eigenem Webserver** (z. B. über ein günstiges Hosting-Paket).

2. **Finale Tests nach dem Deployment**
   - Überprüfen, ob die API erreichbar ist (`https://meinprojekt.com/api/customers`).
   - Sicherstellen, dass das Frontend korrekt auf die API zugreift.

3. **Abschlussreflexion: Rückblick auf das Projekt**
   - Welche Konzepte wurden gelernt?
   - Welche Herausforderungen gab es?
   - Was könnte in Zukunft verbessert oder erweitert werden?

---

## Hinweise

- **Docker-Container ermöglichen ein flexibles Deployment**, indem sie API und Frontend in getrennte, portable Umgebungen packen.
- **Azure App Services oder Netlify sind einfache Cloud-Lösungen**, falls kein eigener Server vorhanden ist.
- **Nach dem Deployment ist eine gründliche Fehleranalyse wichtig**, um sicherzustellen, dass alle Komponenten korrekt funktionieren.

---

## Erweiterungsmöglichkeiten

- **Datenbank-Backup-Strategie entwickeln**, um Datenverluste zu vermeiden.
- **Sicherheit verbessern**, indem API-Zugriffe mit **JWT-Authentifizierung oder API-Keys** gesichert werden.
- **Automatische Updates und CI/CD einführen**, um Änderungen nahtlos online zu bringen.

---

<details>
<summary><strong>Lösungsvorschlag anzeigen</strong></summary>

### **1. Deployment mit Docker**
1. **Dockerfile für die API erstellen**:
```dockerfile
FROM mcr.microsoft.com/dotnet/aspnet:6.0
WORKDIR /app
COPY ./publish .
ENTRYPOINT ["dotnet", "MyRestApi.dll"]
```

2. Dockerfile für das Frontend erstellen:
```dockerfile
FROM nginx
COPY ./webapp /usr/share/nginx/html
```

3. Docker-Container bauen und starten:

```shell
docker build -t myapi .
docker run -d -p 5000:80 myapi
```

### **2. Deployment auf Azure (alternativ)**
1. API in Azure App Service hochladen.
2. Web-App mit Netlify oder Vercel hosten.
3. API-URL in der Webanwendung anpassen.

### **3. Abschlussreflexion**
Fragen zur Reflexion:

- Was waren die größten Herausforderungen in diesem Projekt?
- Welche Konzepte sind jetzt klarer geworden?
- Wie könnte das Projekt in Zukunft weiterentwickelt werden?
</details>

## Abschließende Worte
Herzlichen Glückwunsch! 🎉
Mit dieser letzten Aufgabe ist das komplette Full-Stack-Projekt abgeschlossen.

Du hast gelernt, wie man:
✅ Eine API mit C# und ASP.NET Core entwickelt.
✅ Eine Webanwendung mit HTML, CSS und JavaScript erstellt.
✅ Automatisierte Tests schreibt, um Fehler frühzeitig zu erkennen.
✅ Die Anwendung auf einen Server deployt, sodass sie online erreichbar ist.

Das sind wertvolle Fähigkeiten, die direkt in der Praxis anwendbar sind.
Dieses Projekt kann jetzt als Portfolio-Projekt auf GitHub genutzt werden – und als Grundlage für viele weitere Webentwicklungsprojekte dienen. 🚀
