# 🟠 Aufgabe A05: Bestehenden Code schrittweise verbessern

## Einordnung und Lernziele

**Status:** Pflicht im Lernfaden.

**Voraussetzungen:** [Gemeinsame Schnittstelle und Menü](A04_BesseresMenu.md)

**Intention:** Lesbarkeit und Verantwortlichkeiten verbessern, ohne Verhalten zu verändern.

**Lernziele:**

- Du kannst eine begründete Strukturänderung in kleinen Schritten durchführen.
- Du kannst mit festen Prüffällen und einem Diff nachweisen, was gleich geblieben ist.

**Weiter im Pflichtpfad:** [Tic Tac Toe – Einführung in Spielmechaniken, Arrays und Entscheidungslogik](../Stufe4/A01_TicTacToe.md)

## Aufgabe und Voraussetzungen

Du hast ein funktionierendes Menü und ein Adressbuch mit JSON-Speicherung. Nun verbesserst du die innere Struktur, während das beobachtbare Verhalten gleich bleibt. Dies nennt man **Refactoring**. Überarbeite dafür den vorhandenen Code in deinem bestehenden Repository.

## Anforderungen

1. Speichere den funktionierenden Stand in einem Commit. Lege einen Branch wie `refactor/addressbook-input` an.
2. Notiere mindestens fünf Prüffälle mit Eingabe und Erwartung: Hinzufügen, ungültiges Alter, Suche, Neustart mit gespeicherten Daten und fehlende bzw. beschädigte Datei.
3. Wähle in **deinem** Code eine konkrete Verbesserung: eine lange Methode aufteilen, doppelte Zahleneingabe zusammenführen oder unklare Namen verbessern. Begründe, was derzeit schwer zu lesen oder zu ändern ist.
4. Trenne Konsolenkommunikation von Kontaktverwaltung und Speicherung. Das Menü fragt nach und zeigt Meldungen; `AddressBook` verwaltet Kontakte und gibt Ergebnisse zurück. Übernimm die Trennung aus A03, wenn du sie bisher noch nicht vollständig umgesetzt hast.
5. Führe jeweils eine kleine Änderung durch. Baue danach und wiederhole die betroffenen Prüffälle. Neue Funktionen, geänderte Validierungsregeln und ein anderes JSON-Format gehören in spätere Änderungen.
6. Lies den Diff: Stimmen Kontaktfelder, ID-Vergabe, Dateipfad und Fehlermeldungen weiterhin? Dokumentiere die Verbesserung und die Ergebnisse in einem Pull Request oder deiner Änderungsnotiz.

Bereits gut strukturierter Code braucht keine künstliche zusätzliche Klasse. Wähle dann einen schlecht benannten Teil deines früheren Taschenrechners und übertrage die gleiche Arbeitsweise. Das Adressbuch bleibt die Grundlage für die nächsten Stufen.

## Beispiel für einen sinnvollen Zuschnitt

Eine Menüaktion liest alle Felder, prüft sie, fügt einen Kontakt hinzu und schreibt eine Datei. Markiere zuerst die Abschnitte „Eingabe“, „Prüfung“, „Kontaktverwaltung“ und „Speicherung“. Eine eigene Methode für wiederholte Alterseingabe kann sinnvoll sein; eine Methode für jede einzelne Codezeile ist es meist nicht.

Reine Prüfmethoden geben einen Wert oder ein Ergebnis zurück. Sie sollen nicht gleichzeitig die Konsole lesen. Bei der Wiederverwendung einer Zahleneingabemethode müssen unterschiedliche Wertebereiche erhalten bleiben: Ein gültiges Alter ist nicht automatisch eine gültige Menüauswahl.

Automatisierte Tests folgen ausführlich in Stufe 6. Hier reichen festgehaltene und wiederholbare manuelle Prüffälle. Wenn du bereits Tests geschrieben hast, lässt du sie zusätzlich nach jedem Schritt laufen.

## Gestufte Hinweise

Versuche zuerst eine eigene Lösung. Öffne bei Bedarf zunächst Hinweis 1 und erst danach Hinweis 2; die vorhandenen Beispiele bzw. Referenzen dienen anschließend zum Vergleichen.

<details>
<summary>Hinweis 1: Denkanstoß</summary>

Welche Stelle ist schwer zu verstehen und welche Beobachtungen müssen gleich bleiben?

</details>

<details>
<summary>Hinweis 2: Vorgehensweise</summary>

Notiere zuerst Erwartungen; extrahiere dann genau eine Methode und prüfe vor der nächsten Änderung erneut.

</details>

## Selbst prüfen

| Vorher und nachher ausführen | Erwartung |
| --- | --- |
| gültigen Kontakt hinzufügen und suchen | gleiche Kontaktfelder und Suchregeln |
| Alter `-1`, leere Telefonnummer, ungültige E-Mail | weiterhin abgewiesen |
| Kontakt speichern, neu starten und weiteren hinzufügen | Daten erhalten, IDs verschieden |
| fehlende Datei | leeres Adressbuch |
| beschädigte Datei | Meldung; vorhandene Datei bleibt erhalten |
| Menüaktion zweimal aufrufen | dieselbe Adressbuchinstanz, kein Datenverlust |

Du kannst am Diff zeigen, welche Verantwortung jetzt klarer liegt. Alle notierten Erwartungen bestehen weiterhin. Dein Commit beschreibt eine Strukturverbesserung und enthält keine neue Funktion.

## Bonus: Refactoring mit automatisierter Absicherung

**Intention:** Erlebe später den Unterschied zwischen manueller Wiederholung und automatisch ausgeführten Regressionstests. **Lernziel:** Nach [Stufe 6, A02](../Stufe6/A02_Testing.md) kannst du eine weitere Strukturänderung mit bestehenden Tests absichern. Die Testeinrichtung ist keine Voraussetzung für den Übergang zu Stufe 4.

## Passende Lernquellen

[Leseempfehlung für diesen Lernschritt](../Referenzen/Lernquellen.md#stufe-3-struktur-und-versionsgeschichte). Wähle den dort genannten Abschnitt zur aktuellen Aufgabe und probiere ihn in deinem eigenen Programm aus.
