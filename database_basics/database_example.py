import sqlite3


def tableExists(db: sqlite3.Connection, tablename: str) -> bool:
    # Pro Tipp: SQL Abfragen formattieren. Mehr Übersicht, schneller Probleme
    # erkennen.
    query = """
            SELECT
                COUNT(name)
            FROM
                sqlite_master
            WHERE
                type = 'table'
            AND
                name = ?"""

    # Wenn nur ein Parameter angegeben wird muss ein Komma folgen sonst erhält
    # man einen Compiler-Error der ungefähr so aussieht:
    # 'sqlite3.ProgrammingError: Incorrect number of bindings supplied.
    # The current statement uses 1, and there are 9 supplied.'
    cursor = db.execute(query, (tablename,))

    return (cursor.fetchone()[0] == 1)


if __name__ == "__main__":

    # Verbindung zur Datenbank aufbauen
    db = sqlite3.connect('fahrzeugverwaltung.db')

    # Prüfen ob Tabelle 'fahrzeuge' existiert
    if not tableExists(db, 'fahrzeuge'):
        # Erstelle Tabelle 'fahrzeuge'
        db.execute("""
            CREATE TABLE fahrzeuge(
                id INTEGER
                , marke varchar(50),
                , kennzeichen varchar(10)
                PRIMARY KEY(id)
            )""")

        print("Tabelle erstellt.\n")

    # Abfrage für Fahrzeug einfügen
    query = """
        INSERT INTO fahrzeuge
            (marke, kennzeichen)
        VALUES
            (?, ?)"""

    # Abfrage nehmen und mit Werten befüllen
    db.execute(query, ('audi', 'H-BB-123'))

    # Abfrage an die Datenbank senden
    db.commit()

    print("Fahrzeug in Tabelle eingefügt.\n")

    # Fahrzeuge aus der Tabelle auslesen
    rows = db.execute("""
        SELECT
            marke
            , kennzeichen
        FROM
            fahrzeuge""")

    # Fahrzeuge zeilenweise auflisten
    for row in rows:
        print("{} hat das Kennzeichen {}".format(row[0], row[1]))

    print("Fahrzeug(e) aus Tabelle ausgelesen.\n")

    # Datenbankverbindung schließen
    db.close()
