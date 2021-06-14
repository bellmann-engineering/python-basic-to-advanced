import csv
import sqlite3
import os

con = sqlite3.connect("fahrzeugverwaltung.db") 
cur = con.cursor()

# Fahrzeuge einlesen und inserten
with open('fahrzeuge.csv','r') as fin:
    dr = csv.DictReader(fin) # komma (,) ist default delimiter
    to_db = [(i['MARKE'], i['KENNZEICHEN']) for i in dr]

cur.executemany("INSERT INTO fahrzeuge (marke, kennzeichen) VALUES (?, ?);", to_db)
con.commit()

# Fahrtenbücher einlesen und inserten
fahrtenbuch_folder = 'fahrtenbuecher/'
if os.path.isdir(fahrtenbuch_folder): # prüfen ob es das verzeichnis gibt
    fahrtenbuecher_files = os.listdir(fahrtenbuch_folder) # ermitteln der dateien im verzeichnis
    for fname in fahrtenbuecher_files:
        filepath = os.path.join(fahrtenbuch_folder, fname) # pfad zusammensetzen
        with open(filepath) as f:
            kennzeichen = os.path.splitext(fname)[0] # dateiendung von dateinamen entfernen
            for line in f:
                date, src, dest, *rest = line.split(',') # hier könnte man auch wieder DictReader verwenden
                to_db = (kennzeichen, src, dest) # wir wollen erst einmal nur die 3 inserten
                cur.execute("""
                    INSERT INTO fahrtenbuch (kennzeichen, startort, zielort) 
                    VALUES (?, ?, ?);""", to_db)

con.commit()
con.close() # nicht vergessen wieder zu schließen
