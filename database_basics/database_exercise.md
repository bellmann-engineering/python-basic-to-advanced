## Basiswissen Datenbank mit SQLite in Python

### Motivation

<!--Unser Fuhrpark wächst stetig an. Weitere LKWs, PKWs oder Motorräder müssten immer wieder per Hand im Code hinzugefügt werden. Das wird mit der Zeit sehr aufwändig und das Programm wird sehr unübersichtlich.

Jetzt ist es an der Zeit in unserem Code die Logik und die Datenaufbewahrung voneinander zu trennen.-->

Wir möchten einen Fuhrpark bestehend aus LKWs, PKWs und Motorrädern aufbauen. Diese Datenmenge lässt sich nicht mehr gut in Dateien organisieren. Wir benötigen eine konsistente Datenhaltung.

Dies erreichen wir mit einer einfachen `SQLite` Datenbank. Diese spricht wie viele anderen Datenbanken die Sprache `SQL`. Dies ist eine standartisierte Sprache die SQL Datenbankserver wie postgresql, MS SQL Server, MySQL oder MariaDB sprich.

[Wikipedia Artikel zu SQL Sprache](https://de.wikipedia.org/wiki/SQL)

`SQLite` ist eine sehr kompakte Datenbank für die keine weiteren Programme oder Dienste installiert werden müssen. `sqlite3` ist ein Modul das bereits bei Python mitgeliefert wird und die Schnittstelle zur Kommunikation bereitstellt.

```pyhton
import sqlite3
```

Eine kompakte Einführung in SQL findest du hier in einer interaktiven Schritt-Für-Schritt-Anleitung bei der du auch eigene kleine Dinge ausprobieren kannst: [SQLite Tutorial](https://www.sqlitetutorial.net/)

Um SQL Syntax zu validieren hilft diese Seite: [sql-syntax-check-validator](https://www.eversql.com/sql-syntax-check-validator/)

Eine grundlegendes Datenbankschema für diese Übung haben wir dir vorbereitet: [create_tables.py](https://github.com/bellmann-engineering/python-basic-to-advanced/blob/main/database_basics/create_tables.py)

### Aufgaben

1. Erstelle mittels SQL und dem `sqlite3` Modul Tabellen für Fahrzeuge und Fahrtenbücher über ein Python Script. 
 - Tabellen erstellen: `create_tables.py` 
 - Datenbankname: `fuhrpark.db`
 - Tabellen: `fahrzeuge`, `fahrtenbuch`

2. Jede Tabelle soll eine Spalte `Id` als Primärschlüssel besitzen. Diese `Id` (Abkürzung aus dem englischen Identity) dient zur eindeutigen Identifizierung der gespeicherten Daten. Eine kompakte Erklärung zu diesem Thema findest du auf Website [Dateneule: Primär-  und Fremdschlüssel](https://www.dateneule.de/2019/05/27/primaer-und-fremdschluessel/)

3. Für Textfelder verwende `VARCHAR(50)` oder `TEXT` (Wert in den Klammern gibt die maximale Feldänge an. SQLite ignoriert auf Grund der einfachen Struktur die Länge an den Spaltentypen, erkennt diese als gültig an um kompatibel mit anderen SQL Datenbank zu sein). Für Zahlenfelder verwende `INTEGER`.  
Für Baujahr und Erstzulassung kann wahlweise `INTEGER`, `VARCHAR(4)` oder `TEXT` verwendet werden. Eine Date-Datentyp sieht SQLite nicht vor. Mehr zu Datentypen findest du hier:
https://www.sqlite.org/datatype3.html

4. Welche Datentypen passen für die Spalte `privat`, zur Kennzeichnung einer Privatfahrt, in der Tabelle `fahrtenbuch`?

5. Entwickle ein Python Script das zum Einlesen von Daten aus einer csv-Datei in die SQL-Datenbank dient. Beispielname: `seed.py` (Aus dem Englischen *säen*)
 - Erzeuge eine Schleife die zeilenweise Daten aus der CSV Datei einließt und diese in `INSERT`-Befehle übersetzt
 - Führe anschließend die erzeugten `INSERT` Befehle aus um die Daten in der Datenbank zu speichern

6. Entwickle auf Basis des Programms der Woche 3<sup>1</sup> eine Version, die **ohne CSV dafür mit SQL** arbeitet.
 Beginne mit dem Einlesen der Fahrzeuge:
 - Ersetze die Datei-Einleseroutinen durch passende SQL Aufrufe.
 - Füge testweise neue Daten in die SQL Datenbank ein und prüfe das Ergebnis.
 - Nun sollen die Fahrten aus der Fahrtenbuchtabelle gelesen werden: Da wir keine Dateien mit Kennzeichen als Dateinamen mehr führen benötigt die Tabelle Fahrtenbuch eine Spalte `kennzeichen` zur Zuordnung. Achte darauf die die Spalte `kennzeichen` in der Tabelle `fahrzeuge` und `fahrtenbuch` den exakt gleichen Typen haben.  
 Erstelle ein Python Script `alter_tables.py`, um die Spalte der Tabelle hinzufügen. Der SQL Befehl `ALTER TABLE` ermöglicht Anpassungen an bestehenden Datenbankstrukturen.

1: https://github.com/bellmann-engineering/python-basic-to-advanced/blob/main/files-data-and-oop/files-data-and-oop.md

Optional:

7. Hole mittels SELECT und WHERE-Bedindung für das jeweilige Fahrzeug die Fahrtenbucheintäge aus der Datenbanktabelle und speichere sie als ``Journey``-Objekte beim Fahrzeug. SQL Befehl `WHERE`: https://www.sqlitetutorial.net/sqlite-where/
 
![fahrzeuge_schema](https://github.com/bellmann-engineering/python-basic-to-advanced/blob/main/database_basics/fahrzeuge_table.PNG) 

![fahrtenbuch_schema](https://github.com/bellmann-engineering/python-basic-to-advanced/blob/main/database_basics/fahrenbuch_table.PNG)

 
