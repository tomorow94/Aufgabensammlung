# 🔴 Aufgabe A03: Webseite für dasselbe Adressbuch

## Einordnung und Lernziele

**Status:** Pflicht im Lernfaden.

**Voraussetzungen:** [Unit- und Integrationstests für das Adressbuch](A02_Testing.md)

**Intention:** Dieselbe API mit einer verständlichen Browseroberfläche verbinden.

**Lernziele:**

- Du kannst semantisches HTML, CSS und Ereignisse schrittweise mit fetch verbinden.
- Du kannst Fehler sichtbar behandeln, Eingaben erhalten und grundlegende Tastaturbedienung prüfen.

**Weiter im Pflichtpfad:** [Bestehendes GitHub-Projekt und CI weiterentwickeln](A04_GitHub.md)

## Ziel und Voraussetzungen

Die getestete API verwaltet Kontakte. Erstelle jetzt eine Oberfläche mit HTML, CSS und JavaScript. Teile die Arbeit auf: erst statisches Formular, dann Beispielkontakte ohne Netzwerk, zuletzt echte API-Requests.

**HTML** beschreibt Struktur und Bedeutung, **CSS** das Aussehen, **JavaScript** verarbeitet Aktionen. Das **DOM** ist die vom Browser verwaltete Dokumentstruktur. `fetch` sendet HTTP-Requests; `await` wartet auf die Antwort.

## Anforderungen

1. Erstelle `index.html`, `styles.css`, `script.js`.
2. Verwende sichtbare `label`-Elemente und passende Eingabetypen (`email`, `tel`, `number`).
3. Das Formular enthält dieselben Felder wie `ContactInput`: Name, Alter, Geschlecht, Telefonnummer und E-Mail.
4. GET lädt Kontakte, POST fügt einen hinzu, DELETE entfernt ihn. Eine Bearbeitungsfunktion mit PUT steht unter „Bonus“.
5. Prüfe `response.ok` vor der Verarbeitung. `fetch` wirft bei HTTP 400/404/500 nicht allein wegen des Status einen Fehler.
6. Zeige Ladezustand und Fehlermeldungen sichtbar an. Leere ein Formular erst nach einem erfolgreichen POST; bei einem Fehler bleiben die Daten erhalten.
7. Verwende für Kontaktdaten `textContent`, nicht aus Eingaben zusammengesetztes HTML.

## Zwei Startmöglichkeiten

**Gemeinsame Herkunft (empfohlener Einstieg):** Lege die Dateien in `Api/wwwroot` ab. ASP.NET Core liefert API und Webseite aus; relative Requests an `/api/contacts` verwenden automatisch denselben Host und Port. Vom Repository-Wurzelordner:

```shell
dotnet run --project Beispiele/Adressbuch/Api -- --urls http://localhost:5000
```

Öffne `http://localhost:5000`. Die Datenbankvorbereitung steht in A01; die Webseite wird nicht direkt als `file://` geöffnet.

**Separate Herkunft als Untersuchung:** Starte im Ordner `Api/wwwroot` einen lokalen statischen Server, z. B. mit Python:

```shell
python -m http.server 5500 --bind localhost
```

Ändere `apiUrl` in `script.js` hierfür zu `http://localhost:5000/api/contacts` und öffne `http://localhost:5500`. Port 5500 und Port 5000 sind verschiedene Origins. Die Referenz-API erlaubt für diesen Versuch ausdrücklich `http://localhost:5500` über CORS. Eine andere Adresse, etwa `127.0.0.1`, ist eine andere Herkunft und muss entsprechend konfiguriert werden. JSON-POSTs können einen OPTIONS-Preflight auslösen. Postman prüft keine Browser-CORS-Regeln.

Für den gemeinsamen Start stelle anschließend wieder die relative URL ein. Beim Veröffentlichen keine `localhost`-Adresse im Frontend belassen.

## Gestufte Hinweise

Versuche zuerst eine eigene Lösung. Öffne bei Bedarf zunächst Hinweis 1 und erst danach Hinweis 2; die vorhandenen Beispiele bzw. Referenzen dienen anschließend zum Vergleichen.

<details>
<summary>Hinweis 1: Denkanstoß</summary>

Welche Teile funktionieren bereits ohne Netzwerk und welcher Schritt braucht die API?

</details>

<details>
<summary>Hinweis 2: Vorgehensweise</summary>

Erstelle erst Formular und Beispielkontakte; prüfe bei fetch response.ok und leere Felder ausschließlich nach erfolgreichem Speichern.

</details>

<details>
<summary>Vollständige Lösung</summary>

- [index.html](../Beispiele/Adressbuch/Api/wwwroot/index.html): Formular mit allen Eingabefeldern und Beschriftungen.
- [styles.css](../Beispiele/Adressbuch/Api/wwwroot/styles.css): einfache Gestaltung und sichtbarer Tastaturfokus.
- [script.js](../Beispiele/Adressbuch/Api/wwwroot/script.js): Request-Helfer, Fehlerbehandlung, Ladezustand und CRUD-Aktionen.

Das Script wird mit `defer` geladen, sodass die DOM-Elemente bereits verfügbar sind. Die Request-Funktion behandelt 204 ohne JSON-Body und liest bei Fehlern nach Möglichkeit die Validierungsinformationen der API. Konsolenausgaben allein wären für Benutzer keine ausreichende Fehlerrückmeldung.

</details>

## Selbst prüfen

| Aktion | Erwartung |
|---|---|
| gültigen vollständigen Kontakt absenden | Kontakt erscheint, Formular wird geleert |
| ungültige E-Mail oder leere Pflichtfelder | kein Kontakt gespeichert, verständliche Meldung |
| API stoppen und Formular absenden | sichtbarer Fehler, Eingaben bleiben erhalten |
| Kontakt löschen | aus Liste und Datenbank entfernt |
| POST erfolgreich, danach Listenabruf fehlgeschlagen | Meldung unterscheidet gespeicherten Kontakt und fehlende Aktualisierung |
| Name enthält `<b>Alice</b>` | Text erscheint als Text, nicht als HTML |
| Bedienung nur mit Tastatur | Formular und Buttons erreichbar, Fokus sichtbar |
| separater Server auf 5500 | Preflight und Request funktionieren |

Öffne im Browser die Netzwerkansicht: Prüfe JSON-Felder, Statuscode, OPTIONS und Antwortinhalt. Node.js, npm und ein Frontendframework sind für diese einfache Webseite nicht erforderlich.

Grundlegende Beschriftungen, native Buttons und sichtbarer Fokus sind Teil dieser Pflichtaufgabe. Die zusätzliche Prüfung dynamischer Meldungen, Feldfehler und Screenreader-Bedienung folgt in [Bonus A07](./A07_Barrierefreiheit_Bonus.md).

Referenzen: [Fetch und Fehlerstatus](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch), [CORS in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/security/cors?view=aspnetcore-10.0).

## Drei kleine Einstiegsschritte

**HTML:** Schreibe zuerst eine Überschrift, ein Formular und eine Liste. Ein `<label for="name">` gehört zu einem Feld mit `id="name"`; `required` aktiviert die Browserprüfung. Die Serverprüfung bleibt trotzdem notwendig.

```html
<label for="name">Name</label>
<input id="name" name="name" required>
<ul id="contacts"></ul>
```

**CSS:** Binde die Datei im `head` mit `<link rel="stylesheet" href="styles.css">` ein. Ein Selektor wie `form` wählt die entsprechenden Elemente; Deklarationen legen deren Darstellung fest.

```css
form { display: grid; gap: 0.5rem; }
```

**JavaScript:** Ein Event-Listener reagiert auf eine Aktion. `preventDefault()` verhindert hier, dass das Formular eine neue Seite lädt. Die Skizze setzt ein vorhandenes Formular voraus und gehört in die mit `defer` geladene Scriptdatei.

```js
const form = document.getElementById("contactForm");
form.addEventListener("submit", event => {
    event.preventDefault();
    console.log("Formular wurde abgeschickt.");
});
```

Teste jeden Schritt einzeln. Erst danach ersetzt du die Konsolenausgabe durch einen API-Request. Die vollständige Referenzlösung oben enthält bereits die notwendigen Pflichtfelder und Fehlerbehandlung.

## Bonus: Bearbeiten und Suchen

**Intention:** Erweitere die bestehenden Kontaktaktionen bei unverändertem Datenmodell. **Lernziel:** Du kannst ein vorhandenes Formular mit Kontaktdaten befüllen, per PUT speichern und eine Suchfunktion mit passender Fehlerbehandlung ergänzen. Ladezustand und Eingabeerhalt gehören bereits zur Pflichtaufgabe.

Verwende die vorhandenen PUT-Endpunkte und überprüfe erfolgreiche Speicherung, HTTP 400 und eine inzwischen gelöschte ID mit HTTP 404. Die zusätzliche Barrierefreiheitsprüfung steht in Bonus A07.

## Passende Lernquellen

[Leseempfehlung für diesen Lernschritt](../Referenzen/Lernquellen.md#stufe-6-http-tests-und-webseite). Wähle den dort genannten Abschnitt zur aktuellen Aufgabe und probiere ihn in deinem eigenen Programm aus.
