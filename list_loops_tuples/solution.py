from prettytable import PrettyTable # pip install prettytable


print("Fahrzeugerfassung:\n")

list_of_good_values = ['Volkswagen', 'Audi', 'Skoda', 'Porsche']

keepInserting = True

def getManufacturer():
    good_input = None
    while not good_input:
        manufacturer = input("Hersteller: ")
        if manufacturer in list_of_good_values: 
            good_input = manufacturer
        else:
            print("Kein gültiger Hersteller.")
    return manufacturer

def toInt(string) -> int:
    number = 0
    try: 
        number = int(string)
    except ValueError:
        print("Kein Zahlenwert")
    return number

def getNumber(name: str, range_from: int, range_to: int):
    no = 0
    # while no < range_from or pnos > range_to:
    while no not in range(range_from, range_to):
        caption = name + ": "
        no = toInt(input(caption))
    return no
    
fahrzeuge = []

# main loop
while keepInserting:
    manu  = getManufacturer()
    name  = input("Bezeichnung: ")
    psNo  = getNumber("PS", 30, 300)
    seats = getNumber("Sitze", 2, 6)
    maxKm = getNumber("Höchstgeschwindigkeit", 1, 300)
    fahrzeuge.append( (manu, name, psNo, seats, maxKm ) )

    answer = input("Weiteres Fahrzeug eingeben? (y/n): ")
    if(answer.lower() == 'n'):
        keepInserting = False

# print table

t = PrettyTable(
    [
        'Hersteller', 
        'Fahrzeugbezeichnung', 
        'PS', 
        'Anzahl Sitze', 
        'Höchstgeschwindkeit'
    ])
for f in fahrzeuge:
    t.add_row(list(f))

print(t)

# or iterate over raw data
# for index, tuple in enumerate(fahrzeuge):
#	element_one = tuple[0]
#	element_two = tuple[1]
#	print(element_one, element_two)
