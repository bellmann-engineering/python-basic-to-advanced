class Bar:

    #Die Klasse Bar mit 42 initalisieren
    def __init__(self):
        self.a = 42

    #Überprüfen, ob der übergebene Parameter 0 ist
    def wunschwert(self, par):
        if par == 0:
            #Falls der angegebene Paramenter 0 ist, kommt eine Fehlermeldung
            raise ValueError('Wert ist 0.')
        return self.a

b = Bar()
b.wunschwert(2)
print(b.a)