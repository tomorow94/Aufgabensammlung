# Debugging: Fehler nachvollziehen und beheben

Diese Arbeitsweise gehört ab [Stufe 2, A01](../Stufe2/A01_UmrechnungVonEinheiten.md) zum Pflichtpfad. Du brauchst Variablen, Bedingungen, Schleifen und deine erste Methode. Die folgenden Schritte beziehen sich auf Visual Studio; andere C#-Debugger bieten entsprechende Befehle.

**Intention:** Du sollst eine Fehlerursache anhand beobachteter Werte erklären können, bevor du Code änderst.

**Lernziele:** Du kannst einen Fehler reproduzieren, einen Haltepunkt setzen, in eine Methode springen, lokale Variablen und den Aufrufstapel untersuchen und die Korrektur mit mehreren Eingaben prüfen.

## Ein Ablauf für jede Fehlersuche

1. Notiere Eingabe, erwartetes Ergebnis und tatsächliches Ergebnis. Wähle den kleinsten Fall, der den Fehler zeigt.
2. Setze mit F9 einen Haltepunkt unmittelbar vor der verdächtigen Berechnung oder Bedingung. Starte mit F5.
3. Beobachte Parameter und lokale Variablen. Die markierte Anweisung wird **als Nächstes** ausgeführt; F10 führt sie aus. Mit F11 springst du in eine eigene aufgerufene Methode.
4. Vergleiche den Zustand vor und nach dem Schritt. Formuliere eine konkrete Vermutung, etwa: „Die Division liefert eine ganze Zahl.“
5. Bei einer Exception prüfe Typ, Meldung und den ersten eigenen Aufruf im Aufrufstapel. Der Stapel erklärt, welche Methode die fehlerhafte Stelle aufgerufen hat.
6. Ändere eine Sache, prüfe den Fehlerfall erneut und wiederhole die normalen und ungültigen Fälle unter „Selbst prüfen“.
7. Halte Ursache, Änderung und Prüffälle in wenigen Sätzen fest. Ab Stufe 3 kommt die Korrektur in einen eigenen Git-Commit.

## Übung in deinem Umrechnungsprogramm

Verwende eine Kopie deiner funktionierenden Temperaturmethode. Baue dort absichtlich `c * (9 / 5) + 32` ein. Diese Variante lässt sich kompilieren, berechnet aber nicht für alle Eingaben das richtige Ergebnis.

Teste `0`, `100` und `-40` Grad Celsius. Beobachte in der Methode den Parameter und ergänze bei Bedarf eine lokale Variable für `9 / 5`. Warum fällt der Fehler bei `0` nicht auf? Korrigiere die Methode erst, wenn du das erklären kannst. Prüfe danach alle drei Fälle erneut und übertrage nur die Korrektur in dein Arbeitsprojekt.

<details>
<summary>Hinweis 1: Den Fehler eingrenzen</summary>

Der erwartete Faktor ist 1,8. Untersuche die Division getrennt von Multiplikation und Addition. Der Rückgabetyp der gesamten Methode ändert die Typen der beiden Operanden dieser Division nicht.

</details>

<details>
<summary>Hinweis 2: Ursache und Korrektur</summary>

`9` und `5` sind `int`-Literale; ihre Division ergibt `1`. Mit `9.0 / 5.0` erhältst du den benötigten Faktor. Bei `0` verschwindet der fehlerhafte Faktor in der Multiplikation, deshalb ist dieser einzelne Test unzureichend.

</details>

## Weitere Fehlerarten im Lernfaden

| Zeitpunkt | Untersuchung | Beobachtung |
| --- | --- | --- |
| Stufe 2: Dateien | Datei im unerwarteten Ordner | Arbeitsverzeichnis und vollständiger Dateipfad |
| Stufe 3: Objekte | Kontaktliste nach Menüwechsel leer | Lebensdauer der `AddressBook`-Instanz |
| Stufe 4: Spiele | Ungültiger Zug wechselt den Spieler | Reihenfolge von Prüfung und Zustandsänderung |
| Stufe 6: HTTP | Formular zeigt nach Fehler leere Felder | Netzwerkstatus und Zeitpunkt des Zurücksetzens |

Für Browser-JavaScript nutzt du später die Entwicklerwerkzeuge des Browsers. Eine Exception, ein falsches Ergebnis und eine fehlgeschlagene HTTP-Antwort sind unterschiedliche Beobachtungen; alle brauchen einen reproduzierbaren Fall.

## Selbst prüfen

Du kannst erklären, warum der Temperaturfehler erst mit weiteren Eingaben sichtbar wird. Ein Haltepunkt in der Methode wird erreicht, du zeigst den Parameter und die Division und benennst den Aufrufer. Nach der Korrektur stimmen `0 → 32`, `100 → 212` und `-40 → -40`.

Quelle: [Microsoft: C# mit dem Debugger untersuchen](https://learn.microsoft.com/en-us/visualstudio/get-started/csharp/tutorial-debugger). Lies zunächst die Abschnitte zu Haltepunkten, Schritten, lokalen Variablen und Aufrufstapel; die Bildschirmbilder können von deiner IDE-Version abweichen.
