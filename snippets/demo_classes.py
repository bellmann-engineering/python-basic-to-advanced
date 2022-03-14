class Person():
    def __init__(self, vorname, nachname):
        self.vorname = vorname
        self.nachname = nachname

    def __str__(self):
        return f'Vorname: {self.vorname}, Nachname: {self.nachname}'

    @classmethod
    def from_string(cls, wort):
        vorname, nachname = wort.split(' ')
        return cls(vorname, nachname)

    @staticmethod
    def is_full_name(name):
        return (len(name.strip().split(' ')) > 1)


class Mitarbeiter(Person):
    def __init__(self, vorname, nachname, nummer):
        super().__init__(vorname, nachname)
        self.mitarbeiternummer = nummer

class Student(Person):
    def __init__(self, vorname, nachname, nummer):
        super().__init__(vorname, nachname)
        self.matrikelnummer = nummer

p1 = Person("Peter", "Müller") # Konstruktor wird aufgerufen

p2 = Person.from_string("Peter Müller")
print(p2)

m1 = Mitarbeiter("Hans", "Meier", 123)

print(Person.is_full_name("Kai Bellmann"))
