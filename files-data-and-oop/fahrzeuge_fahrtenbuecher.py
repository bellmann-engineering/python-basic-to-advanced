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
		return self.fahrtenbuch[-1]

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
		self.startkm = int(startkm)
		self.endkm = int(endkm)
		self.zweck = zweck
		self.privat = (privat == 'ja')

	@property
	def distance(self):
		return self.endkm - self.startkm
	
	@classmethod
	def from_csv_line(cls, line):
		datum, startort, zielort, startkm, endkm, zweck, privat = line.rstrip().split(',')
		return cls(datum, startort, zielort, startkm, endkm, zweck, privat)

	
# init arrays
pkws = []
lkws = dict() # alternativ: {}
bikes = []

def read_cars(file):
	with open(file) as csvfile:
		reader = csv.DictReader(csvfile, delimiter=',')
		for row in reader:
			if row["TYP"] == "PKW":
				pkws.append(
					Pkw(row["MARKE"], 
						row["KENNZEICHEN"],
						row["ID"],
						row["BJ"],
						row["EZ"])
						)
			elif row["TYP"] == "LKW":
				lkws[row["KENNZEICHEN"]] = Lkw(row["MARKE"], 
										row["KENNZEICHEN"],
										row["ID"],
										row["BJ"],
										row["EZ"])
				

if __name__ == '__main__':
	fahrzeuge_file = 'fahrzeuge.csv'
	fahrtenbuch_folder = 'fahrtenbuecher/'
	if os.path.isfile(fahrzeuge_file):
		read_cars(fahrzeuge_file)

		#print(lkws[0].marke)

	if os.path.isdir(fahrtenbuch_folder):
		fahrtenbuecher_files = os.listdir(fahrtenbuch_folder)
		for fname in fahrtenbuecher_files:
			filepath = os.path.join(fahrtenbuch_folder, fname)
			with open(filepath) as f:
				kennzeichen = os.path.splitext(fname)[0] # remove ext from filename
				for line in f:
					lkws[kennzeichen].fahrtenbuch.append(Journey.from_csv_line(line))

	# Test:		
	lkw = lkws["H-EL-99"]
	last_journey = lkw.get_last_journey()
	print("Der LKW der Marke {} ist zuletzt von {} nach {} {} km gefahren.\n"
		.format(lkw.marke, last_journey.startort, last_journey.zielort, last_journey.distance))



