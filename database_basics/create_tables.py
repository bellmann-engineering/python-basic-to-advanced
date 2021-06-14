import sqlite3

db = sqlite3.connect('fahrzeugverwaltung.db')

db.execute("""
    CREATE TABLE fahrzeuge (
        id INTEGER
        , marke varchar(50)
        , kennzeichen varchar(10)
        , fahrgestellnr TEXT
        , baujahr INTEGER
        , erstzulassung INTEGER
        , PRIMARY KEY(id))""")


db.execute("""
    CREATE TABLE fahrtenbuch (
        id INTEGER
        , kennzeichen varchar(10)
        , datum INTEGER
        , startkm INTEGER
        , endkm INTEGER
        , startort TEXT
        , zielort TEXT
        , privat varchar(1)
        , PRIMARY KEY(id))""")
