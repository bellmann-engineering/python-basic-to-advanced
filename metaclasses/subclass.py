# Eine Nicht-Ableitbare Klasse
class Final(type):
    def __new__(cls, name, bases, attr):
        # Ueberprueft, ob Final bereits in einer Subklasse genutzt wurde. Falls
        # ja, wird eine Exception geworfen
        type_arr = [type(x) for x in bases]
        for i in type_arr:
            if i is Final:
                raise RuntimeError("You cannot subclass a Final class")
        return super(Final, cls).__new__(cls, name, bases, attr)

# Test: Nutzt die Metaklasse um eine nicht weiter vererbare Klasse zu erzeugen

class Cop(metaclass=Final):
    def exit():
        print("Exiting...")
        quit()

# Der Versuch eine weitere Vererbung vorzunehmen sollte mit einer Fehlermeldung
# quittiert werden
class FakeCop(Cop):
    def scam():
        print("This is a hold up!")

cop1 = Cop()
fakecop1 = FakeCop()
