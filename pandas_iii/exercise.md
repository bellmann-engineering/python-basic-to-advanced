# Arbeiten mit Daten in Datasets

Mit pandas Dataframes Pandas wird die Bearbeitung von Daten einfach(er). Wir können Spalten auswählen oder ersetzen und die Daten darin umgestalten.

1. Wiederhole und erweitere dein Wissen im Bezug auf Dataframes mithilfe des nachfolgenden Tutorial:
 -> https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python
 
2. Arbeite mit dem employees Datensatz (employees.csv) und verwende die nachfolgenden Funktionen:

    isnull()
    notnull()
    dropna()
    fillna()
    replace()
    interpolate()

2.1. Ist das Feld "Gender" immer gefüllt?
2.2.


Daten sind in der realen Welt unvermeidlich nicht perfekt. Pandas kann uns helfen, wenn es um das Bereinigen, Umwandeln, Manipulieren und Analysieren von Daten geht.
Einfach ausgedrückt: Pandas hilft, das Chaos zu beseitigen.

Wichtig ist es vorallem die Arbeit mit unvollständigen Daten nicht nur technisch zu betrachten, um zum Ergebnis zu kommen sondern auch inhaltliche Fragen zu stellen.

Folgende Beispiele verdeutlichen das Vorgehen mit _Missing Values_: 
 - Werte fehlen und Berechnung ist daher nicht: Auffüllen n/a -> z.B. Median
 - Peakwerte wurden gekappt: Korrektur durch Schätzung
 - Werte mit Ausprägung 0/1 fehlen: Schätzung oder weglassen
 - Wert innerhalb einer Skala fehlt (z.B. Befragung): weglassen
