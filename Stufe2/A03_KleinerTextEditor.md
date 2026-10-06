# 🔵 Aufgabe A03: Kleiner Text-Editor

## Einordnung und Lernziele

**Status:** Pflicht im Lernfaden.

**Voraussetzungen:** [Primzahlenprüfung](A02_Primzahlen.md)

**Intention:** Den Übergang von flüchtigem Text zu dauerhafter Speicherung verstehen.

**Lernziele:**

- Du kannst Text speichern und nach einem Neustart wieder laden.
- Du kannst fehlende Datei, Arbeitsverzeichnis und Schreibfehler nachvollziehen.

**Weiter im Pflichtpfad:** [Stoppuhr](A04_Stoppuhr.md)

## Ziel der Aufgabe

Erstelle ein einfaches Konsolenprogramm, das Texte in eine Datei speichert und wieder laden kann. Du vertiefst dabei das Arbeiten mit **Dateien**, **Benutzereingaben** und **einfacher Menüführung**.

Diese Aufgabe verlangt, dass du den Code **selbst schreibst**, orientiere dich dabei an bekannten Mustern oder recherchiere bei Bedarf gezielt nach passenden C#-Befehlen.

- Das Programm sollte dem Benutzer ein Menü mit folgenden Optionen bieten:
  
1. Neuen Text schreiben und speichern.
2. Gespeicherten Text laden und anzeigen.
3. Programm beenden.

- Basierend auf der Auswahl des Benutzers sollte das Programm die entsprechende Funktion ausführen.

---

## Was du lernst

* Wie man Text **in Dateien schreibt** und **aus ihnen liest**
* Wie man ein einfaches **Menü mit Benutzerauswahl** umsetzt
* Wie man **Fehlerbehandlung** für Dateizugriffe einsetzt
* Wie man mit Schleifen einfache Programme strukturiert

---

## Vorgehen & Tipps

1. **Plane dein Programm zuerst in Stichpunkten.** Das hilft dir, den Überblick zu behalten.

   Beispiel:

   ```csharp
   // Menü anzeigen
   // Benutzereingabe auswerten
   // Option 1: Text schreiben → speichern
   // Option 2: Dateiinhalt anzeigen
   // Option 3: Programm beenden
   ```

2. **So speicherst du Text in eine Datei:**

   ```csharp
   File.WriteAllText("meineDatei.txt", "Das ist mein Text.");
   ```

    🔎 **Hinweis:** Sollte noch keine Datei mit dem gegebenen Namen existieren, wird diese automatisch erstellt und in diese geschrieben.

3. **So erstellst du eine Datei (falls sie nicht existiert):**

   ```csharp
   string pfad = "meinOrdner\\meineDatei.txt";
   Directory.CreateDirectory("meinOrdner"); // erstellt den Ordner, falls er nicht existiert
   File.WriteAllText(pfad, "Neuer Inhalt der Datei");
   ```

   🔎 **Hinweis:** Bei Angabe eines relativen Pfads (wie oben) bezieht sich der Pfad auf das **aktuelle Arbeitsverzeichnis**. Es muss nicht mit dem Ordner der `.csproj`-Datei übereinstimmen. Prüfe es mit `Directory.GetCurrentDirectory()` und zeige mit `Path.GetFullPath(pfad)` den tatsächlichen Speicherort an.
   Das ist nützlich, damit dein Code auf verschiedenen Rechnern ohne Anpassung des Pfads funktioniert.

4. **So liest du Text aus einer Datei:**

   ```csharp
   string inhalt = File.ReadAllText("meineDatei.txt");
   Console.WriteLine(inhalt);
   ```

5. **So prüfst du, ob eine Datei existiert:**

   ```csharp
   if (File.Exists("meineDatei.txt"))
   {
       // Datei lesen oder anzeigen
   }
   else
   {
       Console.WriteLine("Datei nicht gefunden.");
   }
   ```

6. **So verwendest du eine Schleife, um Eingaben zu wiederholen:**

   ```csharp
   while (true)
   {
       // Menü anzeigen und auf Benutzereingabe reagieren
   }
   ```

7. **Tipp:** Nutze Kommentare, um die Aufgaben schrittweise zu dokumentieren und später leichter zu erweitern.

---

## Gestufte Hinweise

Versuche zuerst eine eigene Lösung. Öffne bei Bedarf zunächst Hinweis 1 und erst danach Hinweis 2; die vorhandenen Beispiele bzw. Referenzen dienen anschließend zum Vergleichen.

<details>
<summary>Hinweis 1: Denkanstoß</summary>

Wohin zeigt ein relativer Dateipfad bei deinem Programmstart?

</details>

<details>
<summary>Hinweis 2: Vorgehensweise</summary>

Zeige den vollständigen Pfad an und trenne Speichern von Laden; bestehender Inhalt wird bei WriteAllText überschrieben.

</details>

<details>
<summary><strong>Möglicher Lösungsvorschlag anzeigen</strong></summary>

```csharp
using System;
using System.IO;

namespace KleinerTextEditor
{
    class Program
    {
        static void Main(string[] args)
        {
            string dateiPfad = "textdatei.txt";
            Console.WriteLine($"Dateipfad: {Path.GetFullPath(dateiPfad)}");
            while (true)
            {
                Console.WriteLine("Kleiner Text-Editor");
                Console.WriteLine("1. Neuen Text schreiben und speichern");
                Console.WriteLine("2. Gespeicherten Text laden und anzeigen");
                Console.WriteLine("3. Programm beenden");
                Console.Write("Wählen Sie eine Option (1-3): ");
                string? eingabe = Console.ReadLine();
                if (eingabe is null) return;

                switch (eingabe)
                {
                    case "1":
                        NeuenTextSchreibenUndSpeichern(dateiPfad);
                        break;
                    case "2":
                        GespeichertenTextLadenUndAnzeigen(dateiPfad);
                        break;
                    case "3":
                        Console.WriteLine("Programm wird beendet.");
                        return;
                    default:
                        Console.WriteLine("Ungültige Eingabe. Bitte wählen Sie eine Option zwischen 1 und 3.");
                        break;
                }
                Console.WriteLine();
            }
        }

        static void NeuenTextSchreibenUndSpeichern(string pfad)
        {
            Console.WriteLine("Geben Sie den Text ein (beenden mit einer leeren Zeile):");
            string text = "";
            string? zeile;
            while ((zeile = Console.ReadLine()) is not null && zeile != "")
            {
                text += zeile + Environment.NewLine;
            }

            try
            {
                // WriteAllText überschreibt eine bereits vorhandene Datei vollständig.
                if (File.Exists(pfad)) Console.WriteLine("Die vorhandene Datei wird überschrieben.");
                File.WriteAllText(pfad, text);
                Console.WriteLine($"Text wurde erfolgreich in '{pfad}' gespeichert.");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Fehler beim Speichern der Datei: {ex.Message}");
            }
        }

        static void GespeichertenTextLadenUndAnzeigen(string pfad)
        {
            try
            {
                if (File.Exists(pfad))
                {
                    string text = File.ReadAllText(pfad);
                    Console.WriteLine("Gespeicherter Text:");
                    Console.WriteLine("-------------------");
                    Console.WriteLine(text);
                }
                else
                {
                    Console.WriteLine($"Die Datei '{pfad}' wurde nicht gefunden.");
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Fehler beim Laden der Datei: {ex.Message}");
            }
        }
    }
}
```

</details>

## Selbst prüfen

Speichere zwei Zeilen, starte neu und lade sie wieder. Eine fehlende Datei ergibt eine Meldung. Zeige den vollständigen Pfad an und ändere das Arbeitsverzeichnis: Der relative Speicherort verändert sich. Erneutes Speichern überschreibt den bisherigen Inhalt; weise darauf hin oder frage vorher nach. Eine schreibgeschützte Datei ergibt eine verständliche Fehlermeldung.

## Bonus: Mehrere Dateien verwalten

**Intention:** Erweitere den einfachen Speicherablauf um zusätzliche Dateiaktionen.

**Lernziel:** Du kannst Dateinamen wählen, bestehende Texte bearbeiten und die Folgen von Überschreiben oder Löschen erklären.


* Gib dem Benutzer die Möglichkeit, **Dateinamen selbst einzugeben**.
* Ergänze die Option, einen vorhandenen Text zu **bearbeiten und erneut zu speichern**.
* Ermögliche das **Löschen** einer Datei.
* Unterstütze das Speichern mehrerer Texte in verschiedenen Dateien.
* **Zusätzliche Textgestaltung:** Verwende ein ausdrückliches Abschlusswort für die Eingabe, sodass auch leere Absätze gespeichert werden können. Mehrere Textzeilen gehören bereits zum normalen Speichern; im Beispiel beendet eine leere Zeile die Eingabe.
---

> 💡 **Diese Aufgabe bildet die Grundlage für spätere Projekte mit Dateiverwaltung, z. B. Adressbuch oder Notizsystem.**

---

## Passende Lernquellen

[Leseempfehlung für diesen Lernschritt](../Referenzen/Lernquellen.md#stufe-2-methoden-und-fehlersuche). Wähle den dort genannten Abschnitt zur aktuellen Aufgabe und probiere ihn in deinem eigenen Programm aus.
