# Tabellendesign

Die Hauptmotivation des Tabellendesign ist es innerhalb des rationalen Schemas folgende Ziele zu verfolgen:

- Redundanz und Inkonsistenz vermeiden - Daten nicht mehrfach speichern, sonst können sich Kopien widersprechen.
- Anomalien vermeiden - Probleme beim Ändern (Update), Einfügen und Löschen von Daten verhindern.
- Verlustlose Zerlegungen finden - Aufgeteilte Tabellen müssen sich per JOIN wieder exakt zur Originaltabelle zusammensetzen lassen.
- Abhängigkeiten bewahren - Alle ursprünglichen Abhängigkeiten müssen auch nach der Aufteilung noch innerhalb der Tabellen prüfbar sein, ohne Join.

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

Hier ist `Id` der **einzige** Primärschlüssel (einspaltig). Damit ist 2NF automatisch erfüllt - es gibt keinen "Teil" des Schlüssels, von dem etwas nur partiell abhängen könnte.

## Negativbeispiel

Stellen wir uns vor, eine Person kann **mehrere Adressen** haben (z. B. Hauptwohnsitz und Nebenwohnsitz), und die Tabelle sieht deshalb so aus:

| Id | Ort | FName | LName | Strasse | Email |
|----|-----|-------|-------|---------|-------|
| 1 | Berlin | Hans | Müller | Musterstr. 1 | h@mueller.de |
| 1 | München | Hans | Müller | Nebenstr. 9 | h@mueller.de |
| 2 | Entenhausen | Peter | Meier | Hauptstr. 5 | peter@gmail.com |

Der einzige Unterschied: Weil `Id` allein jetzt **nicht mehr eindeutig** ist (Zeile 1 und 2 haben beide `Id = 1`), braucht man `Id + Ort` als **zusammengesetzten Primärschlüssel**, um jede Zeile eindeutig zu identifizieren.

### Warum das die 2NF verletzt

- `Strasse` hängt von `Id` **und** `Ort` ab (welche Straße, hängt davon ab, um welchen Wohnsitz es geht) -> das ist ok, volle Abhängigkeit vom ganzen Schlüssel.
- `FName`, `LName`, `Email` hängen aber **nur von `Id`** ab - eine Person heißt "Hans Müller", egal an welchem Ort. Das ist nur ein **Teil** des Schlüssels.

Das ist die klassische **partielle Abhängigkeit**: Ein Attribut hängt nicht am vollständigen zusammengesetzten Schlüssel (`Id + Ort`), sondern nur an einer seiner Komponenten (`Id`). Genau das verbietet die 2NF.

Man sieht das Problem auch praktisch: "Hans Müller" mit seiner Email steht doppelt in der Tabelle, weil er zwei Adressen hat.

## Was man tun muss: Aufteilen

**Tabelle 1: Personen**

| Id | FName | LName | Email |
|----|-------|-------|-------|
| 1 | Hans | Müller | h@mueller.de |
| 2 | Peter | Meier | peter@gmail.com |

**Tabelle 2: Adresse**

| Id | Ort | Strasse |
|----|-----|---------|
| 1 | Berlin | Musterstr. 1 |
| 1 | München | Nebenstr. 9 |
| 2 | Entenhausen | Hauptstr. 5 |

Jetzt hängt in `Adresse` die `Strasse` am vollständigen Schlüssel (`Id + Ort`), und `FName`/`LName`/`Email` stehen in `Personen` nur einmal pro Person - unabhängig davon, wie viele Adressen sie hat.

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
Als Online-Tool empfiehlt sich z.B.: https://onecompiler.com/mysql oder https://www.programiz.com/sql/online-compiler/

Wir möchten vier Tabellen anlegen: Abteilungen, Angestellte, Kunden und Autos.
Wobei die Beziehungen zwischen den Tabellen folgendermaßen definiert sind:

- Jede Abteilung kann 0 oder mehr Mitarbeiter haben
- Jeder Kunde kann 0 oder mehr Autos haben 

Die Syntax für die erste Tabelle "Abteilung" ist folgende:

``CREATE TABLE Departments 
( 
  Id INT NOT NULL, Name VARCHAR(25) NOT NULL, PRIMARY KEY(Id) 
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
