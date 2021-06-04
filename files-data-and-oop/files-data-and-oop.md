# Camp2Code

## Übung zu Dateihandling, Datenkapselung und Objektorientierter Programmierung (OOP)

**Motivation:**
Bisher haben wir in den vorhergehenden Übungen Fahrzeuge (PKWs, LKWs und Motorräder) programmatorisch, also händisch, mit einer Zeile Code angelegt. Das die Erstellung in REPL oder Sourcecode war denkbar einfach:
``audi = Pkw(parameter...)``

Nun möchten wir den Fuhrpark direkt aus einer Datei einlesen und daraus Objekte erstellen, welche in einer Liste gespeichert werden sollen. Des Weiteren sollen zu den Fahrzeugen Fahrtenbücher eingelesen und beim Fahrzeug verwaltet werden.

**Aufgaben:**

1. Lese die Datei ``fahrzeuge.csv`` (...) ein und verarbeite sie. Über das csv Modul und den notwendigen Import kannst du hier nachlesen: https://docs.python.org/3/library/csv.html
- Die Spalten stellen Attribute der Klasse (Membervariablen) dar. Die erste Spalte zeigt an um welche Art von Fahrzeug es sich handelt. 
- Entsprechend der Spalte 1 soll der richtige Fahrzeugtyp (Objekt) angelegt werden.
2. Speichere alle eingelesen Fahrzeuge in einer Liste ab.
3. Mache aus der Liste ein Dictionary (https://docs.python.org/3/library/stdtypes.html#typesmapping). 
- Entscheide selbst welches Attribut des Fahrzeugs sich am besten als ``Key`` eignet. Value ist ``Objekt`` selbst.
4. Lade dir das zip Archiv mit den Fahrtenbüchern herunter und analysiere die darin befindlichen csv Dateien. Die Dateinamen können mit den vorhandenen Fahrzeugen über das Kennzeichen gematched werden.
5. Erstelle eine Klasse ``Journey`` die für das Einlesen von Fahrtenbucheinträgen passend ist. 
6. Speichere eine Liste genannt ``logbook`` von ``Drive``-Objekten (*List of Drives*) beim jeweiligen Fahrzeug.
7. Teste (manuell) ob du auf ein eingelesen Fahrzeug und sein Fahrtenbuch zugreifen kannst. Verwende ggf. den Debugger.
8. Stelle im Fahrzeug eine Methode  ``getLastDrive`` die aus dem Fahrzeugfahrtenbuch den letzten Eintrag holt und ihn ansprechend darstellt. 
9. Falls bisher noch nicht implementiert überlade in der ``Drive`` Klasse die Methode ```__str__`` 

Optionale Zusatzaufgabe:
10. Nutze das Factory Method Pattern (https://realpython.com/factory-method-python/) um Fahrzeuge und Fahrtenbücher in der jeweiligen Klasse einzulesen. 
