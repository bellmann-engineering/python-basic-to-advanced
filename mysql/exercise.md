# Tabellendesign

Die Hauptmotivation des Tabellendesign ist es innerhalb des rationalen Schemas folgende Ziele zu verfolgen:

- Redundanz und Inkonsistenz vermeiden
- Anomalien vermeiden
- Verlustlose Zerlegungen finden
- Abhängigkeiten bewahren

## Normalformen
Unter Normalisierung eines relationalen Datenbankmodells versteht man die Aufteilung von Attributen in mehrere Relationen (Tabellen) mithilfe der Normalisierungsregeln und deren
Normalformen, sodass eine Form entsteht, die keine vermeidbaren Redundanzen mehr enthält.
Ziel der Normalisierung ist eine redundanzfreie Datenspeicherung zu erstellen. Redundanzfrei bedeutet, dass Duplikate entfernt werden können, ohne dass es zu Informationsverlusten kommt.
Weiterhin soll die Normalisierung Anomalien entfernen. Im Normalisierungsprozess gibt es fünf Normalformen, welche im Folgenden genauer erklärt werden.
In der Datenbankentwicklung ist die Dritte Normalform oft ausreichend, um die perfekte Balance aus Redundanz, Performance und Flexibilität für eine Datenbank zu gewährleisten. Natürlich gibt es auch Sonderfälle, z.B. im wissenschaftlichen Bereich, wo eine Datenbank bis zur 5. Normalform normalisiert werden kann bzw. muss.

## Erste Normalform
_Die Erste Normalform (1NF) ist dann gegeben, wenn alle Informationen in einer Tabelle atomar vorliegen._
Es bedeutet, dass jede Information innerhalb einer Tabelle eine eigene Tabellenspalte bekommt und zusammenhängende Informationen, wie zum Beispiel die Postleitzahl (PLZ) und der Ort, nicht in
einer Tabellenspalte vorliegen dürfen.

![table1.PNG](table1.PNG)

Sowohl die Werte in der Spalte "Name" als auch die "Adresse" sind nicht *atomar* gespeichert. 
Um die 1. Normalform zu erfüllen sollte das Tabellendesign so aussehen:

![table2.PNG](table2.PNG)

Die Spalten wurden entsprechend aufgeteilt.

_Hinweis:_
Ob die Spalte "Strasse" aufgeteilt werden sollte in "Straße" und "Hausnummer" wirft regelmäßig Diskussionen auf. 
Bei Straße und Hausnummer wird es in der Regel nicht notwendig sein sie zu teilen, da eine Suche oder Abfrage auf Hausnummern ohne Straßen in der Praxis eher unüblich ist. 

## Zweite Normalform

Eine Relation befindet sich in der zweiten Normalform, wenn 
1.	Sie in der ersten Normalform ist und 
2.	jedes Nicht-Schlüssel-Attribut vom Primärschlüssel voll funktional abhängig ist.

Zuerst müssen wir den Begriff Primärschlüssel aufklären: Er wird zur eindeutigen Identifizierung eines Datensatzes verwendet. In einer normalisierten Datenbank besitzen alle Tabellen einen Primärschlüssel.
In unserem Beispiel handelt es sich um die Spalte "Id", welche eine fortlaufende eindeutige Nummer für jeden Kundeneintrag in der Tabelle führt. Nun müssen wir also sicherstellen, dass jedes Feld der Tabelle sich inhaltlich auf die Schlüsselspalte bezieht:

![table3.PNG](table3.PNG)

In diesem Fall ist die Tabelle bereits in der 2. Normalform, da es keine partiale Abhängigkeit eines Nicht-Schlüsselattributs von einem Teilschlüssel gibt. Es müssen keine weiteren Änderungen vorgenommen werden.

Angenommen, die Spalte "id" ist der Primärschlüssel und "Strasse" ist von der Kombination aus "Ort" und "Id" abhängig, während die restlichen Attribute ("FName", "LName" und "E-mail") nur von "id" abhängen. In diesem Fall müssten wir die Tabelle umstrukturieren, um die 2. Normalform zu erreichen.

Eine mögliche Umstrukturierung könnte wie folgt aussehen:

Tabelle 1: Personen

    Id (Primärschlüssel)
    FName
    nachname
    email

Tabelle 2: Adresse

    Id (Primärschlüssel)
    Strasse
    Ort

## Dritte Normalform
Eine Relation befindet sich in der dritten Normalform, wenn 
1.	Sie in der zweiten Normalform ist und 
2.	jedes Nicht-Schlüssel-Attribut nicht transitiv vom Primärschlüssel abhängig ist, d.h. aus keinem Nicht-Schlüssel-Attribut folgt ein anderes Nicht-Schlüssel-Attribut. 

Diese Definition ist erst einmal schwer zu verstehen. Mit einer weiteren Grafik lässt sich jedoch aufzeigen, was mit Punkt 2 gemeint ist:

![table4.PNG](table4.PNG)


Die Spalte "Straße" hängt von "Ort" ab und das obwohl Ort kein Primärschlüssel-Attribut ist. Um den Verstoß aufzulösen wird eine zweite Tabelle "Cities" für die Orte gebildet und in der "Customers" Tabelle ein Verweis gespeichert. Den Verweis nennt man Fremdschlüssel, was oftmals mit „FK“ in der Spaltenbezeichnung abgekürzt wird. 

![table5.PNG](table5.PNG)

Wenn wir nun die neu erstellte Tabelle "Cities" mit den Spalten "Id" und "Ort" genau ansehen stellen wir fest, dass sie gegen die 2. Normalform verstößt. Dementsprechend sollen auch hier drei Spalten anstelle von zwei gebildet werden, sodass sich folgendes Bild ergibt:

![table6.PNG](table6.PNG)

## Übung 1 (Tabellendesign)

Die nachfolgenden Aufgaben können auf Papier, in Excel oder jedem anderen vergleichbaren Tool durchgeführt werden. 

1.	Die Daten eines Busreiseunternehmens sollen in einer relationalen Datenbank abgespeichert werden. Die folgende Abbildung zeigt den Datenbestand in einer nicht-Normalisierten Form.
Führe schrittweise die Normalformen 1–3 durch.

![table7.PNG](table7.PNG)

2.	Welche weiteren Spalten wären denkbar und welchen Typ sollten diese haben? Zur Auswahl stehen die folgenden Datentypen: Zahl, Datum, Text, Zahl (Währung). 

## Übung 2

Die nachfolgenden Aufgaben können in der MySQL Workbench (sofern installiert), dem MySQL Query Explorer, PhpMyAdmin oder auch einem Online Tool durchgeführt werden.
Als Online-Tool empfiehlt sich z.B.: https://onecompiler.com/mysql

Wir möchten vier Tabellen anlegen: Abteilungen, Angestellte, Kunden und Autos.
Wobei die Beziehungen zwischen den Tabellen folgendermaßen definiert sind:

- Jede Abteilung kann 0 oder mehr Mitarbeiter haben
- Jeder Kunde kann 0 oder mehr Autos haben 

Die Syntax für die erste Tabelle "Abteilung" ist folgende:

``CREATE TABLE Departments (
    Id INT NOT NULL AUTO_INCREMENT,
    Name VARCHAR(25) NOT NULL,
    PRIMARY KEY(Id)
);``

Die Tabelle "Departments" (englisch für "Abteilung") hat zwei Spalten: "Id" und "Name". Der Primärschlüssel ist "Id". Der Schlüssel entspricht hier eine natürlichen Zahl, die fortlaufend hochgezählt wird.

Für jede Spalte müssen wir einen Namen spezifizieren. Spaltennamen dürfen keine Leerzeichen enthalten (nutze stattdessen den Unterstrich). Ebenso darf keine Zahl am Anfang des Namens stehen. Ein Minus ist ebenfalls problematisch, dort lieber den Unterstrich verwenden.

``Autoincrement`` ist eine Hilfsfunktion die mittlerweile in die meisten Datenbanken Einzug gehalten hat. Es handelt sich um einen Mechanismus um eindeutige Zahlenwerte zu generieren indem der Zahlenwert bei jedem `INSERT` hochgezählt wird:

``CREATE TABLE Departments (
    Id INT NOT NULL AUTO_INCREMENT,
    Name VARCHAR(25) NOT NULL,
    PRIMARY KEY(Id),
);``

Wenn wir es nachträglich bei der bereits angelegten Tabelle ändern wollen:

``ALTER TABLE Departments CHANGE Id Id INT(10) AUTO_INCREMENT PRIMARY KEY;``


1.	Lege folgende vier Tabellen an:

![table8.PNG](table8.PNG)

Solltet ihr das Attribut `FOREIGN KEY` einsetzten so ist es wichtig auf die Reihenfolge bei der Erstellung zu achten, da die Tabellen damit aufeinander verweisen.

2. Identifiziere in jeder Tabelle den Primärschlüssel.
3. Stelle sicher, dass jedes Feld den passenden Datentypen hat.

Zur Übung:
- Füge der Tabelle Employees eine zusätzliche Spalte Plz hinzu. 
- Löschen die zuvor angelegte Spalte Plz wieder.

4. Nun wollen wir konsistente Daten in die Tabellen eintragen. Hierzu verwenden wir bereits bekannten ``INSERT``-Befehl.
5. Mit welcher Abfrage bekommen wir besonders einfach den Abteilungsnamen eines bestimmten Mitarbeiters zusammen mit seinen Nachnamen angezeigt?
