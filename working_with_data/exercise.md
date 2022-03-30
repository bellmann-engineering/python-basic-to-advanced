# Camp2Code
## Arbeiten mit Daten

Uns liegt ein Datensatz in Form einer CSV Datei ([athletes.csv](athletes.csv)) vor, welcher Daten aller Athleten die 2016 in Rio an den Olympischen Spielen teilgenommen haben, enthält. Der Datensatz enthält 11.538 Athleten (6333 Männer und 5205 Frauen).

Die CSV Datei hat 12 Spalten, wobei vorallem für unsere Auswertung die Spalte `gold`, welche die Anzahl Goldmedaille die der Athlet gewonnen hat enthält, sowie die Spalte `nationality`, die eine 3-stelligen Ländercode enthält, für uns von Interesse sind.
Bei den Ländercodes handelt es sich um IOC Länderschlüssel (https://en.wikipedia.org/wiki/List_of_IOC_country_codes), wobei z.B. "GER" für Deutschland steht.


Aufgaben: 
1. Lese die CSV Datei mittels dem build in module `csv` ein. Hinweis: Die CSV Datei liegt im UTF-8 Zeichensatz vor.
- Ignoriere dabei die Kopfzeile mit den Spaltenbeschriftungen.
- Zähle die Anzahl an Goldmedaille die während der Austragung verliehen wurden.
2. Ermittle mittels eines Dictionaries wieviele Goldmedaille je Land gewonnen wurden.
3. Ermittele wieviele Goldmedaille Deutschland gewonnen hat.
4. Ermittele mithilfe eines Liste auf Tuples (Land, Goldmedailleanzahl) und der `sum`-Funktion das selbe Ergebnis wie in Aufgabe 2 und 3.
5. Kann die Summenfunktion auch direkt beim CSV lesen geschickt eingsetzt werden, sodass weniger Codezeilen notwendig sind um die Anzahl Goldmedaillen (Total) zu ermitteln?
6. Definiere einen Filter über das Dictionary aus Aufgabe 2, sodass ein neues Dictionary entsteht, welches nur die Länder mit mind. einer Goldmedaille enthält.
7. Wieviele Ländern haben mind. eine Goldmedaille gewinnen können?

--
Zusatzaufgabe:
