# Arbeiten mit Daten in Datasets

Mit pandas Dataframes Pandas wird die Bearbeitung von Daten einfach(er). Wir können Spalten auswählen oder ersetzen und die Daten darin umgestalten.

1. Wiederhole und erweitere dein Wissen im Bezug auf Dataframes mithilfe des nachfolgenden interaktiven Tutorials: https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python

2. Sieh dir die CheatSheets zu Pandas Basics, Dataframes und Data Wrangling an.
 
3. Arbeite mit dem employees Datensatz ([employees.csv](https://raw.githubusercontent.com/bellmann-engineering/python-basic-to-advanced/main/pandas_iii/employees.csv)) und verwende die nachfolgenden Funktionen aus dem pandas Paket:
  
  - isnull()
   - notnull()
   - dropna()
   - fillna()
   - replace()

Folgende Aufgaben sind zu lösen:
 1. Ist das Feld "Gender" immer gefüllt? Gebe alle Datensätze aus bei denen es nicht gefüllt ist.
 2. Fülle die leeren "Gender" Felder mit dem Wert "No Gender" auf.
 3. Ersetze alle weiteren Leerwerte (NaN) mit dem Wert -99.
 4. Lösche alle Zeilen aus dem Dataset die einen Leerwert enthalten. Speichere das Ergebnis in einem neuen Dataset.
 5. Ermittle die Anzahl der in 4. gelöschen Zeilen.
 6. Lösche Spalten die mind. 1 Leerwert enthalten.

Zusatzaufgaben (optional):
 1. Ersetze alle Salery Werte über 100.000 mit dem Median der Spalte.
 2. Entferne die Zeilen (Employees) mit Salery über 100.000 aus dem Datensatz.

> Hinweis: Beachte, dass es nicht immer sinnvoll ist die Werte _inplace_ zu ersetzen/zu löschen sofern mit Daten weitergearbeitet werden soll.

Daten sind in der realen Welt unvermeidlich nicht perfekt. Pandas kann uns helfen, wenn es um das Bereinigen, Umwandeln, Manipulieren und Analysieren von Daten geht.
Einfach ausgedrückt: Pandas hilft, das Chaos zu beseitigen.

Wichtig ist es vorallem die Arbeit mit unvollständigen Daten nicht nur technisch zu betrachten, um zum Ergebnis zu kommen sondern auch inhaltliche Fragen zu stellen.

Folgende Beispiele verdeutlichen das Vorgehen mit _Missing Values_: 
 - Werte fehlen und Berechnung ist daher nicht: Auffüllen n/a -> z.B. Median
 - Peakwerte wurden gekappt: Korrektur durch Schätzung
 - Werte mit Ausprägung 0/1 fehlen: Schätzung oder weglassen
 - Wert innerhalb einer Skala fehlt (z.B. Befragung): weglassen
