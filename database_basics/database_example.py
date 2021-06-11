import sqlite3

def tableExists(db, tablename):
    c = db.execute("""SELECT COUNT(name) FROM sqlite_master WHERE type='table' AND name='{}'""".format(tablename))
    return (c.fetchone()[0] == 1)

if __name__ == "__main__":

    db = sqlite3.connect('fahrzeugverwaltung.db')

    if not tableExists(db, "fahrzeuge"):
        db.execute("""CREATE TABLE fahrzeuge(
                    id INTEGER,
                    marke varchar(50),
                    kennzeichen varchar(10),
                    PRIMARY KEY(id))""")

    print("Tabelle erstellt.\n")
                
    db.execute("INSERT INTO fahrzeuge (marke, kennzeichen) VALUES ('audi', 'H-BB-123')")
    db.commit()	
    print("Fahrzeug in Tabelle eingefügt.\n")

    rows = db.execute("SELECT marke, kennzeichen FROM fahrzeuge")
    for row in rows:
        print("{} hat das Kennzeichen {}".format(row[0], row[1]))

    print("Fahrzeug(e) aus Tabelle ausgelesen.\n")

    db.close()
