Schritt 1: 1. Normalform (1NF)

Tabelle "Fahrten":
+---------+--------+----------------+---------+---------+------------------+
| FahrtNr.| BusNr. | Busbezeichnung | Bustyp  | FahrerID| Ziel             |
+---------+--------+----------------+---------+---------+------------------+
| 1       | 455    | EG1            | Lang    | 1       | Heide            |
| 2       | 1212   | Regio4         | Kurz    | 2       | Moor             |
| 3       | 633    | Regio1         | Kurz    | 2       | World's End      |
| 4       | 303    | Schnellbus     | Lang    | 3       | Wonderland       |
+---------+--------+----------------+---------+---------+------------------+

Tabelle "Fahrer":
+---------+-----------------+
| FahrerID| Name            |
+---------+-----------------+
| 1       | Hans Meier      |
| 2       | Peter Fahrer    |
| 3       | Bill Gates      |
+---------+-----------------+

Jetzt sind die Werte atomar, und wir haben eine separate Tabelle für Fahrer erstellt.

Schritt 2: 2. Normalform (2NF)

In diesem Schritt stellen wir sicher, dass jedes Attribut von der vollständigen Primärschlüsselabhängig ist. Der Primärschlüssel besteht aus "FahrtNr." und "BusNr.". Wir sehen, dass die Attribute "Busbezeichnung" und "Bustyp" nur von "BusNr." abhängig sind, während "FahrerID" von "FahrtNr." abhängig ist. Um dies zu beheben, erstellen wir zusätzliche Tabellen:

Tabelle "Fahrten":
+---------+--------+--------+------------------+
| FahrtNr.| BusNr. | Ziel   | FahrerID         |
+---------+--------+--------+------------------+
| 1       | 455    | Heide  | 1                |
| 2       | 1212   | Moor   | 2                |
| 3       | 633    | World's End | 2          |
| 4       | 303    | Wonderland | 3          |
+---------+--------+--------+------------------+

Tabelle "Busse":
+--------+----------------+
| BusNr. | Busbezeichnung |
+--------+----------------+
| 455    | EG1            |
| 1212   | Regio4         |
| 633    | Regio1         |
| 303    | Schnellbus     |
+--------+----------------+

Tabelle "Fahrer":
+---------+-----------------+
| FahrerID| Name            |
+---------+-----------------+
| 1       | Hans Meier      |
| 2       | Peter Fahrer    |
| 3       | Bill Gates      |
+---------+-----------------+

In der 3. Normalform sind alle Attribute von der Primärschlüsselabhängig und es gibt keine transitive Abhängigkeit zwischen den Attributen. Die Attribute "Busbezeichnung" und "Bustyp" hängen nur von "BusNr." ab und sind nicht von "FahrtNr." abhängig. Daher wurden sie in die separate Tabelle "Busse" verschoben.

+---------+--------+---------+
| FahrtNr.| BusNr. | Ziel    |
+---------+--------+---------+
| 1       | 455    | Heide   |
| 2       | 1212   | Moor    |
| 3       | 633    | World's End |
| 4       | 303    | Wonderland|
+---------+--------+---------+

+--------+----------------+
| BusNr. | Busbezeichnung |
+--------+----------------+
| 455    | EG1            |
| 1212   | Regio4         |
| 633    | Regio1         |
| 303    | Schnellbus     |
+--------+----------------+

+---------+-----------------+
| FahrerID| Name            |
+---------+-----------------+
| 1       | Hans Meier      |
| 2       | Peter Fahrer    |
| 3       | Bill Gates      |
+---------+-----------------+

