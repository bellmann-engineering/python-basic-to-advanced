# Camp2Code
## Aufgabe zu Datenauswertung mit Pandas

Ziel ist ein Programm zur Analyse der Netzwerkbelegung von zu entwickeln. Ferner soll das Programm die Möglichkeit bieten eine Vorausschau zu ermöglichen um entstende Engpässe frühzeitig zu erkennen.

# Aufgabe

1. Es liegt eine Rohdaten Excel-Datei (raw.xlsm) aus der die Spalten A und H-S in eine `SQL`-Tabelle überführt werden soll. Nutze dazu auf der einen Seite `pandas` dazu die Exceldatei zu lesen, auf der anderen Seite soll die Tabelle in einer sqlite Datenbank entstehen.
Die SQL Datenbank dient als Persistenz für Auswertung.
2. Die SQL-Tabelle besteht aus Netzen, Erfassungspunkten und der NET-Auslasung (`USAGE`). Sie soll folgendermaßen aussehen:


| ID  |      NET      | USAGE | TIMESTAMP |
|-----|---------------|-------|-----------|
|   1 |  10.252.114.0 |  12.5 |  1.2.2021 |
|   2 |  10.252.114.0 |  12.5 |  1.3.2021 |
| ... |               |       |           |
|   7 |  194.114.40.0 |    80 |  1.2.2021 |
| ... |               |       |           |
|   11 | 194.114.108.0 |   3.7 |  1.2.2021 |



3. Lese die SQL Tabelle mit `pandas` ein. 
4. Entwickle eine Funktion zur Vorausschau, um die nächsten 3 Monate vorauszusagen. Nutze um einen Trend zu generieren lineare Regression. 
Sollten nicht ausreichend Datenpunkte für ein Netz aus der Vergangenheit vorliegen so kann kein Trend berechnet werden.
5. Zeige an welche Netze in den nächsten 3 Monaten nurnoch 5% und 10% freie Kapazität haben.
