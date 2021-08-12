class Ampel(object):
    def __init__(self, pListeZustaende):
        self.listeZustaende = pListeZustaende
        self.indexAktuellerZustand = 0

    def schalten(self):
        if self.indexAktuellerZustand < len(self.listeZustaende)-1:
            self.indexAktuellerZustand = self.indexAktuellerZustand + 1
        else:
            self.indexAktuellerZustand = 0

    def getZustand(self):
        return self.listeZustaende[self.indexAktuellerZustand]

    def setZustand(self, z):
        self.indexAktuellerZustand = self.listeZustaende.index(z)

class AmpelAuto(Ampel):
    def __init__(self, anfangszustand):
        self.listeZustaende = ['rot', 'rotgelb', 'gruen', 'gelb']
        self.indexAktuellerZustand = self.listeZustaende.index(anfangszustand)

    def getLampen(self):
        zustand = self.listeZustaende[self.indexAktuellerZustand]
        if zustand == 'rot':
            lampen = (True, False, False)
        elif zustand == 'rotgelb':
            lampen = (True, True, False)
        elif zustand == 'gruen':
            lampen = (False, False, True)
        elif zustand == 'gelb':
            lampen = (False, True, False)
        return lampen
