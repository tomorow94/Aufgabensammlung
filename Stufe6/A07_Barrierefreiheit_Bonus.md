# 🔴 Bonus A07: Das Adressbuch zugänglich bedienen

## Einordnung und Lernziele

**Status:** Bonus (optional; keine Voraussetzung für spätere Pflichtaufgaben).

**Voraussetzungen:** [Webseite für dasselbe Adressbuch](A03_Webentwicklung.md)

**Intention:** Die bestehende Webseite für zusätzliche Bedienweisen untersuchen und verbessern.

**Lernziele:**

- Du kannst Feldfehler, dynamische Meldungen und Löschaktionen zugänglich zuordnen.
- Du kannst einen vollständigen Ablauf mit Tastatur und weiteren Prüfmethoden dokumentieren.

**Weiter im Pflichtpfad:** [Bestehendes GitHub-Projekt und CI weiterentwickeln](A04_GitHub.md)

## Aufgabe und Voraussetzungen

Die grundlegenden Beschriftungen, nativen Buttons und der sichtbare Tastaturfokus gehören bereits zu [A03](./A03_Webentwicklung.md). Diese Vertiefung untersucht zusätzlich, wie Fehler, Ladezustände und dynamische Kontaktlisten für unterschiedliche Bedienweisen verständlich werden. Arbeite an derselben Webseite und derselben API.

## Anforderungen

1. Dokumentiere einen vollständigen Ablauf mit Tastatur: Formular ausfüllen, Kontakt speichern, Liste neu laden und Kontakt löschen. Verwende Tab, Shift+Tab und die üblichen Tasten für Buttons und Auswahlfelder.
2. Prüfe mit einem verfügbaren Screenreader, ob jedes Eingabefeld einen verständlichen Namen und der Geschlechts-Selektor erkennbare Optionen hat. Nutze zusätzlich den Accessibility-Baum der Browserwerkzeuge. Falls kein Screenreader verfügbar ist, dokumentiere diese noch offene Prüfung ausdrücklich.
3. Ordne erklärende Texte und eigene Validierungsfehler mit `aria-describedby` dem jeweiligen Feld zu. Setze `aria-invalid="true"` nur bei einem tatsächlich erkannten Fehler und entferne den Zustand nach der Korrektur. Browser- und Servervalidierung müssen weiterhin funktionieren.
4. Melde dynamische Erfolgs- und Ladezustände über einen passenden Statusbereich. Die Referenz hat bereits `role="status"`; prüfe seine tatsächlichen Ansagen. Vermeide mehrere gleichzeitige Live-Regionen mit derselben Meldung.
5. Gestalte wiederholte Löschbuttons unterscheidbar, etwa mit dem zugänglichen Namen „Alice löschen“. Erzeuge Namen aus Kontaktdaten weiterhin als Text, nicht als HTML.
6. Lege fest, wo der Fokus nach dem Löschen des gerade fokussierten Kontakts landet. Wähle etwa den nächsten Kontakt oder den Button „Liste neu laden“. Ein Listenabruf ohne Löschung darf den Fokus nicht unnötig versetzen.
7. Teste die Seite mit 200 % Zoom und einem schmalen Fenster. Beschriftungen, Fehler und Buttons bleiben lesbar und erreichbar. Information wird nicht allein durch Farbe vermittelt.

Native HTML-Elemente sind der Ausgangspunkt. Zusätzliche ARIA-Attribute haben einen konkreten Zweck und müssen zum sichtbaren Verhalten passen. Verändere keine Kontaktfelder und keine API-Endpunkte für diese Übung.

## Vorgehen

Beginne mit einer Liste beobachteter Probleme. Ändere pro Schritt ein Problem und wiederhole denselben Ablauf. Vergleiche vor und nach der Änderung die sichtbare Darstellung, den Accessibility-Baum und die Bedienung. Browserseitige Pflichtfeldprüfung und eine HTTP-400-Antwort sind zwei verschiedene Fehlerwege; untersuche beide.

## Gestufte Hinweise

Versuche zuerst eine eigene Lösung. Öffne bei Bedarf zunächst Hinweis 1 und erst danach Hinweis 2; die vorhandenen Beispiele bzw. Referenzen dienen anschließend zum Vergleichen.

<details>
<summary>Hinweis 1: Denkanstoß</summary>

Wie erkennt eine Person ohne Maus das betroffene Feld und die nächste Aktion?

</details>

<details>
<summary>Hinweis 2: Vorgehensweise</summary>

Prüfe Namen und Fokus zuerst mit nativen Elementen; ergänze ARIA nur für konkrete Beziehungen und Statusänderungen.

</details>

## Selbst prüfen

| Fall | Erwartung |
| --- | --- |
| reine Tastaturbedienung | alle Aktionen erreichbar, Fokus sichtbar, keine Tastaturfalle |
| leeres Pflichtfeld / ungültige E-Mail | betroffener Eingabe und Erklärung zuordenbar |
| API nicht erreichbar | verständliche Meldung, eingegebene Daten erhalten |
| Kontakt erfolgreich gespeichert | verständliche Statusmeldung ohne unnötigen Fokuswechsel |
| fokussierten Kontakt löschen | Fokus erreicht ein sinnvolles verbleibendes Element |
| zwei Kontakte mit verschiedenen Namen | Löschaktionen sind unterscheidbar |
| Zoom und schmales Fenster | Inhalt bleibt bedienbar |

Abgabe: eine kurze Liste der Befunde mit Vorher/Nachher und den verwendeten Prüfmethoden. Wenn ein automatischer Check keine Probleme meldet, ist die manuelle Tastatur- und Screenreader-Prüfung trotzdem nötig. Die Übung belegt einzelne verbesserte Abläufe, keine vollständige Zertifizierung der Webseite.

## Passende Lernquellen

[Leseempfehlung für diesen Lernschritt](../Referenzen/Lernquellen.md#bonus-zugänglichkeit-und-datenbanktests). Wähle den dort genannten Abschnitt zur aktuellen Aufgabe und probiere ihn in deinem eigenen Programm aus.
