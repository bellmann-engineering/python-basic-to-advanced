Schritt 1: 1. Normalform (1NF)

| FahrtNr. | BusNr. | Busbezeichnung | Bustyp   | Vorname | Nachname   | Ziel          |
|----------|--------|----------------|----------|---------|------------|---------------|
| 1        | 455    | EG1            | Lang     | Hans    | Meier      | Heide         |
| 2        | 1212   | Regio4         | Kurz     | Peter   | Fahrer     | Moor          |
| 3        | 633    | Regio1         | Kurz     | Peter   | Fahrer     | World's End   |
| 4        | 303    | Schnellbus     | Lang     | Bill    | Gates      | Wonderland    |

Schritt 2: 2. Normalform (2NF)

In diesem Schritt stellen wir sicher, dass jedes Attribut von der vollständigen Primärschlüsselabhängig ist. Der Primärschlüssel besteht aus "FahrtNr." und "BusNr.". Wir sehen, dass die Attribute "Busbezeichnung" und "Bustyp" nur von "BusNr." abhängig sind, während "FahrerID" von "FahrtNr." abhängig ist. Um dies zu beheben, erstellen wir zusätzliche Tabellen:


Tabelle "Busse":

| BusNr. | Busbezeichnung |
|--------|----------------|
| 455    | EG1            |
| 1212   | Regio4         |
| 633    | Regio1         |
| 303    | Schnellbus     |


Tabelle "Fahrer":

| FahrerID | Vorname | Nachname |
|----------|---------|----------|
| 1        | Hans    | Meier    |
| 2        | Peter   | Fahrer   |
| 3        | Bill    | Gates    |


In der 3. Normalform sind alle Attribute von der Primärschlüsselabhängig und es gibt keine transitive Abhängigkeit zwischen den Attributen. Die Attribute "Busbezeichnung" und "Bustyp" hängen nur von "BusNr." ab und sind nicht von "FahrtNr." abhängig. Daher wurden sie in die separate Tabelle "Busse" verschoben. "Fahrer" und "Busse" werden den Fahrten über Fremdschlüssel zugeordnet. 

Tabelle "Fahrten":

| FahrtNr. | BusNr. | Bustyp   | Ziel          | FahrerID |
|----------|--------|----------|---------------|----------|
| 1        | 455    | Lang     | Heide         | 1        |
| 2        | 1212   | Kurz     | Moor          | 2        |
| 3        | 633    | Kurz     | World's End   | 2        |
| 4        | 303    | Lang     | Wonderland    | 3        |

Tabelle "Busse":

| BusNr. | Busbezeichnung |
|--------|----------------|
| 455    | EG1            |
| 1212   | Regio4         |
| 633    | Regio1         |
| 303    | Schnellbus     |


Tabelle "Fahrer":

| FahrerID | Vorname | Nachname |
|----------|---------|----------|
| 1        | Hans    | Meier    |
| 2        | Peter   | Fahrer   |
| 3        | Bill    | Gates    |

Es wäre denkbar die Zeile und sogar die Bustypen ebenfalls in Tabellen auszulagern und als Fremdschlüssel zu referenzieren.
