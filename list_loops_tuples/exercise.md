### Camp2Code: Aufgabe zu Listen, Schleifen und Tuples

Ziel ist es ein Konsoleprogramm zu schreiben das Benutzereingaben entgegennimmt. Der Aufrufer des Programms soll Parameter eines Fahrzeuges abgefragt werden. 
Hierzu zählen:
 * Hersteller
 * Bezeichnung
 * PS
 * Anzahl Sitze
 * Höchstgeschwindigkeit

(https://github.com/bellmann-engineering/python-basic-to-advanced/blob/70cff86edc27491e159627c07167bb68d285405c/list_loops_tuples/input_screenshot.png)

Ist ein Fahrzeug vollständig eingegeben, so soll der Benutzer gefragt werden ob er ein weiteres Fahrzeug eingeben möchte. 

Die Werte (Hersteller, Bezeichnung, ...) sollen als passende Datentypen in einem Tuple gespeichert werden. Die Tuple wiederrum in einer Liste.
Die Kapselung davon ist Folgende: `liste = [('Volkswagen', 'ID3', 200, 4, 220), ('Audi, ... )]`

Entscheidet der Benutzer er hat ausreichend Fahrzeuge eingegeben werden alle Fahrzeuge tabellarisch ausgegeben.

Schritte:
1. Programmiere eine Schleife für die Fahrzeugeingabe.
2. Validiere die eingegeben Werte (Hersteller und Bezeichung sind Zeichenketten, PS, Sitzanzahl und Höchstgeschwindigkeit Zahlenwerte).
3. Erweitere die Validierung um eine Plausibilitätsprüfung (PS größer 30 und kleiner 300, Anzahl Sitze mind. 2, ...).
4. Nehme die Speicherung im Tuple vor.
5. Speichere die Tuples in einer Liste.
6. Gebe die Liste möglichst ansprechend aus.

Zusatzaufgabe:
Stelle sicher, dass nur Autos der Marken Volkswagen, Audi, Skoda und Porsche erfasst werden können.

Hinweis: Eine Datenhaltung in Datenbank oder Textdatei ist nicht notwendig. Die Daten werden nur zur Laufzeit des Programmes gespeichert.

Zusatzaufgabe: 
Lagere möglichst viele Operationen in Funktionen aus, um das Programm besser lesbar und wartbar zu gestalten.
