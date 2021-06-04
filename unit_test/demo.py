class Person:  # basisklasse / elternklasse / base
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.age = 0
        self.geburtstag = self.geburtsdatum(5)

    def geburtsdatum(self, a):
        a = 5

    # methode: nicht python weg für rückgabe einzelner werte
    def getFullName(self):
        return "{} {}".format(self.first_name, self.last_name)

    @property  # getter
    def full_name(self):
        # f'{self.first_name} {self.last_name}'
        return "{} {}".format(self.first_name, self.last_name)

    @full_name.setter
    def full_name(self, value):
        vorname, nachname = value.split(" ")
        self.first_name = vorname
        self.last_name = nachname


class Employee(Person):  # kind / child / erbende
    def __init__(self, first_name, last_name, personalnummer):
        super().__init__(first_name, last_name)
        self.personalnummer = personalnummer

    @property
    def personalinfo(self):
        return "{} : {}".format(self.full_name, self.personalnummer)


hans = Person("Hans", "Meier")
print(hans.getFullName())
hans.full_name = "Hans Mueller"
print(hans.full_name)

thomas = Employee("Thomas", "Huber", 123)
print(thomas.personalinfo)

print(isinstance(thomas, Employee))
print(isinstance(thomas, Person))

print(isinstance(hans, Employee))
print(isinstance(hans, Person))
