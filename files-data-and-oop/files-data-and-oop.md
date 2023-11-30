# Camp2Code

## Übung zu Dateihandling, Datenkapselung und Objektorientierter Programmierung (OOP)

**Motivation:**
Bisher haben wir in den vorhergehenden Übungen Fahrzeuge (PKWs, LKWs und Motorräder) programmatorisch, also händisch, mit einer Zeile Code angelegt. Das die Erstellung in Python REPL oder im Sourcecode war denkbar einfach:
``audi = Pkw(parameter...)``

Nun möchten wir den Fuhrpark direkt aus einer Datei einlesen und daraus Objekte erstellen, welche in einer Liste gespeichert werden sollen. Des Weiteren sollen zu den Fahrzeugen Fahrtenbücher eingelesen und beim Fahrzeug verwaltet werden.

**Aufgaben:**

1. Lese die Datei ``fahrzeuge.csv`` ([Dateidownload](https://raw.githubusercontent.com/bellmann-engineering/python-basic-to-advanced/main/files-data-and-oop/fahrzeuge.csv)) ein und verarbeite sie. Über das build-in csv Module und den notwendigen Import kannst du hier nachlesen: https://docs.python.org/3/library/csv.html
 - Die Spalten stellen Attribute der Klasse (Membervariablen) dar. Die erste Spalte zeigt an um welche Art von Fahrzeug es sich handelt. 
 - Entsprechend der ersten Spalte soll der richtige Fahrzeugtyp (Objekt) angelegt werden.

>TYP,MARKE,KENNZEICHEN,ID,BJ,EZ<br>
>PKW,Volkswagen,WOB-A-123,W0L000051T2123456,1.7.2012,1.12.2013<br>
>PKW,Volkswagen,WOB-XX-444,WKZ000051T2123777,5.5.2012,8.1.2013<br>
>PKW,Audi,WOB-XX-444,W101ZZZ51T2654321,1.1.2019,12.4.2021<br>
>LKW,Scania,H-EL-99,WKZAAAAA766544123,1.4.2020,1.5.2021<br>

2. Speichere alle eingelesen Fahrzeuge in einer Liste ab.
3. Mache aus der Liste ein Dictionary (https://docs.python.org/3/library/stdtypes.html#typesmapping). 
- Entscheide selbst welches Attribut des Fahrzeugs sich am besten als ``Key`` eignet. Value ist ``Objekt`` selbst.
4. Erstelle Fahrtenbücher mit dem Kennzeichen des jeweiligen Fahrzeuges als Dateinamen. Die Fahrtenbücher sollen folgendes Format haben:
> 1.5.2021,Wolfsburg,Hannover,40100,40185,Warenlieferung,nein<br>
> 4.5.2021,Hannover,Wolfsburg,40185,40270,Rückfahrt zum Standort,nein

Das Beispiel für ein Fahrzeug kann so verwendet werden. 
[[Hier zum Download]](https://raw.githubusercontent.com/bellmann-engineering/python-basic-to-advanced/f0d9cf24ba06eb580315f8a4437d5c43fa3cf95e/files-data-and-oop/fahrtenbuecher/H-EL-99.csv)

Es werden weitere solche Dateien benötigt, die du selbst anlegst.

5. Erstelle eine Klasse ``Journey``, die für das Einlesen von Fahrtenbucheinträgen passend ist. Eine Fahrt im Fahrtenbuch besteht aus:
 - Datum
 - Startort
 - Zielort
 - Startkilometerstand (lt. Tacho)
 - Endkilometerstand
 - Privatfahrt (bool: ja/nein)
 - Zweck
6. Speichere eine Liste genannt ``fahrtenbuch`` von ``Journey``-Objekten (sprich: *List of Journeys*) beim jeweiligen Fahrzeug.
7. Teste (manuell) ob du auf ein eingelesen Fahrzeug und sein Fahrtenbuch zugreifen kannst. Verwende ggf. den Debugger dazu.
8. Erweitere den Fahrtenbucheintrag um ein ``@Property`` welches die Distanz der Fahrt zurückgibt.
9. Erstelle in der Klasse ``Fahrzeug`` eine Methode  ``get_last_journey(self)`` die aus dem Fahrzeugfahrtenbuch den letzten Eintrag holt und ihn ansprechend darstellt. 


Optionale Zusatzaufgabe:

10. Filtere die Fahrtenbucheinträge entsprechend, sodass Privatfahrten mittels des Parameters ``doNotShowPrivate`` ausgeblendet werden können.
11. Entwickle eine Methode die Lücken im Fartenbuch aufdeckt.

![uml](https://github.com/bellmann-engineering/python-basic-to-advanced/blob/7157099aa44e7f41dc6aa1f8bc43fc25e8a29897/files-data-and-oop/classdiagramm.png)

