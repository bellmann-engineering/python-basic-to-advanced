import csv
from datetime import datetime
import os.path

class Fahrzeug():
	def __init__(self, marke, kennzeichen, fahrgestellnummer, baujahr, erstzulassung):
		self.marke = marke
		self.kennzeichen = kennzeichen
		self.fahrgestellnummer = fahrgestellnummer
		self.baujahr = baujahr
		self.erstzulassung = erstzulassung
		self.fahrtenbuch = []

	def __repr__(self):
		return '<{0}.{1} object at {2}>'.format(self.__module__, type(self).__name__, hex(id(self)))

	def __str__(self):
		return "EZ: {}, BJ: {}".format(self.erstzulassung, self.baujahr)

	def get_last_journey(self):
		return self.fahrtenbuch[-1] #letzten Eintrag aus der Liste holen

class Pkw(Fahrzeug): 
	def __init__(self, marke, kennzeichen, fahrgestellnummer, baujahr, erstzulassung, hubraum = 0):
		super().__init__(marke, kennzeichen, fahrgestellnummer, baujahr, erstzulassung)
		self.hubraum = hubraum

class Lkw(Fahrzeug): 
	def __init__(self, marke, kennzeichen, fahrgestellnummer, baujahr, erstzulassung, hubraum = 0):
		super().__init__(marke, kennzeichen, fahrgestellnummer, baujahr, erstzulassung)
	
class Journey():
	def __init__(self, datum_as_string, startort, zielort, startkm, endkm, zweck, privat):
		self.datum = datetime.strptime(datum_as_string, '%d.%m.%Y')
		self.startort = startort
		self.zielort = zielort
		self.startkm = int(startkm) # Kilometerstände zwingend als integer damit wir damit rechnen können
		self.endkm = int(endkm)
		self.zweck = zweck
		self.privat = (privat == 'ja') # soll bool-Variable sein

	@property
	def distance(self):
		return self.endkm - self.startkm
	
    # factory method
	@classmethod
	def from_csv_line(cls, line): 
		datum, startort, zielort, startkm, endkm, zweck, privat = line.rstrip().split(',')
		return cls(datum, startort, zielort, startkm, endkm, zweck, privat)

	
# init arrays
pkws = []
lkws = dict() # alternative Schreibweise: {}
bikes = [] # vorgesehen für die Motorräder

# Einelesen der fahrzeuge.csv mitteld DictReader 
# damit in [] Bezeichner verwendet werden können.
def read_cars(file):
	with open(file) as csvfile:
		reader = csv.DictReader(csvfile, delimiter=',')
		for row in reader:
			if row["TYP"] == "PKW":
				pkws.append(    # in pkw liste hinzufügen
					Pkw(row["MARKE"], 
						row["KENNZEICHEN"],
						row["ID"],
						row["BJ"],
						row["EZ"])
						)
			elif row["TYP"] == "LKW":
				lkws[row["KENNZEICHEN"]] = Lkw(row["MARKE"], # dem dict hinzufügen, Schlüssel ist das Kennzeichen
										row["KENNZEICHEN"],
										row["ID"],
										row["BJ"],
										row["EZ"])
				

if __name__ == '__main__':
	fahrzeuge_file = 'fahrzeuge.csv'
	fahrtenbuch_folder = 'fahrtenbuecher/'
    
	if os.path.isfile(fahrzeuge_file): # prüfen ob die Datei vorhannden ist
		read_cars(fahrzeuge_file)

	if os.path.isdir(fahrtenbuch_folder): # prüfen ob es das verzeichnis gibt
		fahrtenbuecher_files = os.listdir(fahrtenbuch_folder) # ermitteln der dateien im verzeichnis
		for fname in fahrtenbuecher_files:
			filepath = os.path.join(fahrtenbuch_folder, fname) # pfad zusammensetzen
			with open(filepath) as f:
				kennzeichen = os.path.splitext(fname)[0] # dateiendung von dateinamen entfernen
				for line in f:
					lkws[kennzeichen].fahrtenbuch.append(Journey.from_csv_line(line))   # an der richtigen stelle im dict
                                                                                        # an die fahrtenbuchliste anfügen

	# Test:		
	lkw = lkws["H-EL-99"]
	last_journey = lkw.get_last_journey()
	print("Der LKW der Marke {} ist zuletzt von {} nach {} {} km gefahren.\n"
		.format(lkw.marke, last_journey.startort, last_journey.zielort, last_journey.distance))



