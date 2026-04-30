from datetime import date


class Person:
    def __init__(self, vorname, nachname, geburtstag):
        self.vorname = vorname
        self.nachname = nachname
        self.geburtstag = geburtstag

    @property
    def age(self):
        today = date.today()
        return today.year - self.geburtstag.year - ((today.month, today.day) < (self.geburtstag.month, self.geburtstag.day))


class Fahrzeug:
    def __init__(self, baujahr, erstzulassung):
        self.baujahr = baujahr
        self.erstzulassung = erstzulassung
        self.hoehe = 0
        self.breite = 0
        self.laenge = 0

    def __repr__(self):
        return f"<{self.__module__}.{type(self).__name__} object at {hex(id(self))}>"
    
    def __str__(self):
        return f"EZ: {self.erstzulassung}, BJ: {self.baujahr}"

    def setSize(self, hoehe, breite, laenge):
        self.hoehe = hoehe
        self.breite = breite
        self.laenge = laenge

    @property
    def volumen(self):
        return self.hoehe * self.breite * self.laenge

    def isBiggerThan(self, other):
        return self.volumen > other.volumen


class Pkw(Fahrzeug):
    def __init__(self, baujahr, erstzulassung, hubraum):
        super().__init__(baujahr, erstzulassung)
        self.hubraum = hubraum

    def hasFahrerlaubnis(self, person):
        return person.age >= 18


class Motorrad(Fahrzeug):
    def __init__(self, baujahr, erstzulassung, automatik):
        super().__init__(baujahr, erstzulassung)
        self.automatik = automatik

    def hasFahrerlaubnis(self, person):
        return person.age >= 18


class Lkw(Fahrzeug):
    def __init__(self, baujahr, erstzulassung):
        super().__init__(baujahr, erstzulassung)

    def hasFahrerlaubnis(self, person):
        return person.age >= 24


peter = Person("Peter", "Meier", date(1966, 1, 12))
audi = Pkw(2018, date(2019, 4, 13), 2_000)
if audi.hasFahrerlaubnis(peter):
    print("\nPeter darf den Audi fahren.")

paul = Person("Paul", "Panther", date(1998, 10, 1))
brummi = Lkw(2000, date(2002, 1, 1))
if brummi.hasFahrerlaubnis(paul) == False:
    print("\nPaul ist zu jung um Lkw zu fahren.")

brummi.setSize(2.50, 2.80, 12)
print(f"\nDer LKW mit {brummi} hat ein Volumen von {brummi.volumen} m³")

audi.setSize(1.20, 2, 3.8)
if brummi.isBiggerThan(audi):
    print("\nDer Brummi ist größer als der Audi")
