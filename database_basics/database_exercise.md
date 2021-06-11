# Camp2Code

## Basiswissen Datenbank mit SQLite in Python

**Motivation:**
Unser Fuhrpark bestehend aus PKWs, LKWs und Motorrädern wächst stetig an. Eine Speicherung in Dateien ist daher nicht zukunftsweisend und wir wollen die Datenhaltung in einer SQL Datenbank realisieren.
SqLite ist einfach mit Python zu verbinden, erfordert keine aufwändige Installation eines Datenbankservers und verwendet die Sprache *SQL*.

In folgendem Codebeispiel siehst du wie eine Datenbanktabelle angelegt, Daten eingefügt und wieder ausgelesen werden können:
[Beispiel](https://github.com/bellmann-engineering/python-basic-to-advanced/blob/21edcafdc181695e835cd25586976177535b4b03/database_basics/database_example.py)


Schritt für Schritte Hilfe zur SQL Syntax findest du hier: [SQLLite Tutorial](https://www.sqlitetutorial.net/)

**Aufgaben:**

1. Erstelle mittels SQL und dem ``sqlite3`` Modul Tabellen für Fahrzeuge und Fahrtenbücher über ein Python Script. Beispielname: ``create_tables.py``
Name der Datenbank: ``fuhrpark.db``

Tabellennamen: ``fahrzeuge``, ``fahrtenbuch``

2. Jede Tabelle soll eine Spalte ID als Primärschlüssel besitzen. Der Primärschlüssel kommt in relationalen Datenbanken immer dann zum Einsatz wenn Datensätze eindeutig identifiziert werden sollen. Mehr dazu: [Primär-  und Fremdschlüssel](https://www.dateneule.de/2019/05/27/primaer-und-fremdschluessel/)
3. Für Textfelder verwende ``TEXT`` oder ``varchar(50)`` (Wert in Klammern ist die Größe). Für Zahlenfelder verwende ``INTEGER``. 
Für Baujahr und Erstzulassung kann wahlweise ``INTEGER`` oder ``TEXT`` verwendet werden. Eine Date-Datentyp sieht SqLite nicht vor. Mehr zu Datentypen findest du hier:
https://www.sqlite.org/datatype3.html

4. Welche Datentypen kommen für die Spalte ``privat`` (um eine Privatfahrt zu kennezeichnen) der Tabelle ``fahrtenbuch`` in Frage?

5. Entwickle ein Python Script das zur Migration der Daten von csv in die SQL-Datenbank dient. Beispielname: ``migrate.py``
 - Mache zu diesem Zwecke eine Schleife die zeilenweise aus der csv Datei leist und daraus INSERT Befehle erzeugt für die Datenbank.
7. Entwickle auf Basis des Programms der Vorwoche eine Version die ohne CSV dafür mit SQL arbeitet.
 Beginne mit dem Einlesen der Fahrzeuge:
 - Ersetze die Datei-Einleseroutinen durch passende SQL Aufrufe.
 - Füge testweise neue Daten in die SQL Datenbank ein und prüfe das Ergebnis.
 
 Nun sollen die Fahrten aus der Fahrtenbuchtabelle gelesen werden: Da wir keine Dateien mit Kennzeichen als Dateinamen mehr führen benötigt die Tabelle Fahrtenbuch eine Spalte ``kennzeichen`` zur Zuordnung. Achte darauf, dass die Spalte den exakt gleichen Datentyp wie in der Fahrzeugtabelle hat.
 Erstelle ein Python Script ``alter_tables``, um die Spalte der Tabelle hinzufügen. Sieh dir dazu den SQL Befehl ``ALTER TABLE`` an.
 
7. Hole mittels SELECT und WHERE-Bedindung für das jeweilige Fahrzeug die Fahrtenbucheintäge aus der Datenbanktabelle und speichere sie als ``Journey``-Objekte beim Fahrzeug.
 WHERE: https://www.sqlitetutorial.net/sqlite-where/
 
 
![fahrzeuge_schema](https://github.com/bellmann-engineering/python-basic-to-advanced/blob/96e5d90c5eadaf6dfb9a5f80458d6493c9a51659/database_basics/fahrzeuge_table.PNG) ![fahrtenbuch_schema](https://github.com/bellmann-engineering/python-basic-to-advanced/blob/96e5d90c5eadaf6dfb9a5f80458d6493c9a51659/database_basics/fahrenbuch_table.PNG)

 
