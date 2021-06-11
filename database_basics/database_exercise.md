# Camp 2 Code

## Basiswissen Datenbank SQLite mit Python

Unser Fuhrpark bestehend aus PKWs, LKWs und Motorrädern wächst stetig an. Eine Speicherung in Dateien ist daher nicht zukunftsweisend und wir wollen die Datenhaltung in einer SQL Datenbank realisieren.
SQL Lite ist einfach mit Python zu verbinden, erfordert keine aufwändige Installation eines Datenbankservers und verwendet die Sprache *SQL*.

In folgendem Codebeispiel siehst du wie eine Datenbanktabelle angelegt, Daten eingefügt und wieder ausgelesen werden können:
https://github.com/bellmann-engineering/python-basic-to-advanced/blob/21edcafdc181695e835cd25586976177535b4b03/database_basics/database_example.py

Schritt für Schritte Hilfe zur SQL Syntax findest du hier: https://www.sqlitetutorial.net/


1. Erstelle mittels SQL und dem ``sqlite3`` Modul Tabellen für Fahrzeuge und Fahrtenbücher über ein Python Script. Beispielname: ``create_tables.py``
Name der Datenbank: ``fuhrpark.db``

Jede Tabelle soll eine ID als Primärschlüssel haben. Für Textfelder verwende ``TEXT`` oder ``varchar(50)`` (Wert in Klammern ist die Größe). Für Zahlenfelder verwende ``INT``. 
Für Baujahr und Erstzulassung kann wahlweise ``INTEGER`` oder ``TEXT`` verwendet werden. Eine Date-Datentyp sieht SqLite nicht vor. Mehr zu Datentypen findest du hier:
https://www.sqlite.org/datatype3.html

3. Entwickle ein Python Script das zur Migration der Daten von csv in die SQL-Datenbank dient. Beispielname: ``migrate.py``
4. Entwickle auf Basis des Programms der Vorwoche eine Version die ohne CSV dafür mit SQL arbeitet.
 Beginne mit dem Einlesen der Fahrzeuge:
 - Ersetze die Datei-Einleseroutinen durch passende SQL Aufrufe
 - Füge Testweise neue Daten in die SQL Datenbank ein und prüfe das Ergebnis
 
 Nun soll aus der Tabelle für Fahrtenbücher die Eintäge gelesen werden. Da wir keine Dateien mit Kennzeichen als Dateinamen mehr führen benötigt die Tabelle Fahrtenbuch eine Spalte ``kennzeichen`` zur Zuordnung. Achte darauf, dass die Spalte den exakt gleichen Datentyp wie in der Fahrzeugtabelle hat.
 Erstelle ein Python Script ``alter_tables``, um die Spalte der Tabelle hinzufügen.
 
5. Hole mittels SELECT und WHERE-Bedindung für das jeweilige Fahrzeug die Fahrtenbucheintäge aus der Datenbanktabelle und speichere sie als ``Journey``-Objekte beim Fahrzeug.
 WHERE: https://www.sqlitetutorial.net/sqlite-where/
 
 
