# 🟠 Aufgabe A04: Gemeinsame Schnittstelle und Menü

## Ziel und Voraussetzungen

Du hast Klassen und Objekte kennengelernt. Jetzt beschreibst du mit einer **Schnittstelle** einen gemeinsamen Vertrag: Jedes eingebundene Programm hat einen Namen und eine `Start()`-Methode. Das Menü braucht die konkrete Klasse dahinter nicht zu kennen. Dies ist eine erste Anwendung von Polymorphie.

## Anforderungen

1. Definiere `IMenuProgram` mit `Name` und `Start()`.
2. Registriere Programme ausdrücklich in einer `List<IMenuProgram>`.
3. Zeige die Liste als Menü und prüfe die Auswahl mit `TryParse`.
4. `0` beendet das Menü. Ungültiger Text beendet es nicht.
5. Ein Unterprogramm kehrt durch das Ende seiner `Start()`-Methode oder `return` ins aufrufende Menü zurück.

Eine Liste entdeckt Klassen **nicht automatisch**. Die explizite Registrierung ist in dieser Aufgabe Absicht. Reflection ist eine spätere Vertiefung. Tastenkürzel und Exceptions zur Navigation sind für diesen Lernschritt unnötig.

<details>
<summary>Vollständiges Beispiel für Program.cs (.NET 10)</summary>

```csharp
using System;
using System.Collections.Generic;
public interface IMenuProgram
{
    string Name { get; }
    void Start();
}
public class HelloWorld : IMenuProgram
{
    public string Name => "Hallo Welt";
    public void Start() => Console.WriteLine("Hallo Welt!");
}
public class Menu
{
    private readonly List<IMenuProgram> programs;
    public Menu(List<IMenuProgram> programs) => this.programs = programs;
    public void Start()
    {
        while (true)
        {
            for (int i = 0; i < programs.Count; i++) Console.WriteLine($"{i + 1}. {programs[i].Name}");
            Console.Write("0. Beenden\nAuswahl: ");
            string? text = Console.ReadLine();
            if (text is null) return;
            if (!int.TryParse(text, out int choice))
            {
                Console.WriteLine("Bitte eine ganze Zahl eingeben.");
                continue;
            }
            if (choice == 0) return;
            if (choice < 1 || choice > programs.Count)
            {
                Console.WriteLine("Auswahl außerhalb des Menüs.");
                continue;
            }
            programs[choice - 1].Start();
        }
    }
}
class Program
{
    static void Main() => new Menu(new List<IMenuProgram> { new HelloWorld() }).Start();
}
```

</details>

## Selbst prüfen

`abc`, leere Eingabe, `-1` und `99` zeigen Meldungen und lassen das Menü geöffnet. `1` führt das Unterprogramm aus und zeigt danach wieder das Menü. Nur `0` oder das Ende des Eingabestroms beendet es. Füge dein Adressbuch als weitere Implementierung hinzu und teste zwei Aufrufe: Der Zustand darf nicht versehentlich zurückgesetzt werden.

## Vertiefung

Vergleiche eine Schnittstelle mit einer abstrakten Basisklasse: Gemeinsame Implementierung kann in einer Basisklasse liegen, der Vertrag allein in einer Schnittstelle. Untermenüs können ein `NavigationResult`-Enum zurückgeben, etwa `Back` und `MainMenu`; der Aufrufer entscheidet über den weiteren Ablauf. Verwende hierfür keine Exception-Nachricht als Steuersignal.

Optional: Reflection zur Entdeckung von Implementierungen, nachdem du Registrierung und Polymorphie verstanden hast. Definiere dann ausdrücklich, welche Klassen instanziiert werden dürfen und wie sie ihre Abhängigkeiten erhalten.
