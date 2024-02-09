import sqlite3

db = sqlite3.connect('fahrzeugverwaltung.db')

db.execute("""CREATE TABLE IF NOT EXISTS fahrzeuge 
           (
           id INTEGER, marke TEXT, kennzeichen TEXT, 
           PRIMARY KEY(id)
           )""")

marke = "Porsche"
kennzeichen = "S-GO-911"
sqlStatement = "INSERT INTO fahrzeuge (marke, kennzeichen) VALUES (?, ?)"
db.execute(sqlStatement, 
           (marke, kennzeichen) )
db.commit()

rows = db.execute("SELECT * FROM fahrzeuge")

for row in rows:
    print(f"Der {row[1]} hat das Kennzeichen {row[2]}")
