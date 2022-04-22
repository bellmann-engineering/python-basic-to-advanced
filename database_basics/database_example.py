import sqlite3

# Datenbank erstellen / verbinden
db = sqlite3.connect('fahrzeugverwaltung.db')

db.execute("""CREATE TABLE IF NOT EXISTS fahrzeuge (
    id INTEGER, 
    marke varchar(50), 
    kennzeichen varchar(10), 
    PRIMARY KEY(id)
    )""")

# sql injection vermeiden durch parametrisiertes Statement
sqlInsert = "INSERT INTO fahrzeuge (marke, kennzeichen) VALUES (?, ?)"
#in datenbanktabelle einfügen
db.execute(sqlInsert, ('audi', 'M-KB-123'))

# Änderungen an die Datenbank senden
db.commit()

# auslesen der Tabelle fahrzeuge
rows = db.execute("SELECT * FROM fahrzeuge")

# zeilen durchlaufen
for r in rows:
    print("Der {} hat das Kennzeichen {}".format(r[1],r[2]))
