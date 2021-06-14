import sqlite3

class Fahrzeug():
	def __init__(self, marke, kennzeichen, fahrgestellnummer, baujahr, erstzulassung):
		self.marke = marke
		self.kennzeichen = kennzeichen
		self.fahrgestellnummer = fahrgestellnummer
		self.baujahr = baujahr
		self.erstzulassung = erstzulassung
		self.fahrtenbuch = []

	def __str__(self):
		return "Marke: {}, Kennzeichen: {}".format(self.marke, self.kennzeichen)

class Pkw(Fahrzeug): 
	def __init__(self, marke, kennzeichen, fahrgestellnummer =None, baujahr = None, erstzulassung = None, hubraum = 0):
		super().__init__(marke, kennzeichen, fahrgestellnummer, baujahr, erstzulassung)
		self.hubraum = hubraum
	

# Verbindung zur Datenbank aufbauen
db = sqlite3.connect('fahrzeugverwaltung.db')

# fahrzeuge aus der tabelle 'fahrzeuge' mittels sql-select holen
def read_cars(file):
	fahrzeuge = []

	rows = db.execute("""
        SELECT
            marke
            , kennzeichen
        FROM
            fahrzeuge""")
	for row in rows:
		fahrzeuge.append(Pkw(row[0], row[1])) # pkw objekte in fahrzeuge liste hinzufügen
	
	return fahrzeuge

if __name__ == "__main__":

    for f in read_cars("fahrzeuge.csv"):
        print(f)

