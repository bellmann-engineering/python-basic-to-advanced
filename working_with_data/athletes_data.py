import csv  # build in module

# Konstanten für Spalten die uns interessieren
COUNTRY_COL = 2
GOLD_COL = 8

# 1. Anzahl alle Goldmedallien zählen
# Achtung: Zeichensatz der csv Datei ist utf8
with open("athletes.csv", encoding="utf8") as fin:
    next(fin)  # kopfzeile
    total = 0
    for row in csv.reader(fin):
        total += int(row[GOLD_COL])
    print("Anzahl Gold Medallien (overall): ", total)

# 2. Es wird ein Dictionary verwendet und value beim Key (Land) hochgezählt
countries = {}

with open("athletes.csv", encoding="utf8") as fin:
    next(fin)  # kopfzeile überspringen
    total = 0
    for row in csv.reader(fin):
        country = row[COUNTRY_COL]
        if country not in countries:
            countries[country] = 0
        countries[country] += int(row[GOLD_COL])

# Alle Länder mit Gold-Medallienanzahl:
print("Alle Länder mit Anzahl Gold Medallien dahinter", countries)

# 3. Um die Anzahl deutscher Medallien auszugeben
print("GER: ", countries["GER"])

# 4. weitere Möglichkeit: wir verwenden eine Liste, bilden Tuples und summieren
countries_list = []

with open("athletes.csv", encoding="utf8") as fin:
    next(fin)  # kopfzeile überspringen
    total = 0
    for row in csv.reader(fin):
        countries_list.append((country, int(row[GOLD_COL])))

# sum funktion auf tuple index 1 => anzahl
total_gold_medals = sum([pair[1] for pair in countries_list])
print("Alle Gold Medallien", total_gold_medals)

# sum funktion mit bedingung verknüpft
total_german_gold = sum([pair[1] for pair in countries_list if pair[0] == "GER"])
print("German Gold:", total_german_gold)


# 5. Anzahl Gold Medallien direkt mit sum im CSV Reader ermitteln
with open("athletes.csv", encoding="utf8") as fin:
    next(fin)  # kopfzeile überspringen
    total = sum(int(r[GOLD_COL]) for r in csv.reader(fin))

    print("Anz. Gold: ", total)

# 6. Filtern nach Ländern die mindestens eine Gold Medallie haben / eine Gold Medallie haben
countriesWithGoldMedals = {key: value for (key, value) in countries.items() if value > 0}
print("Ländern mit Gold:", countriesWithGoldMedals)

# 7. Anzahl der Einträge aus 5 verwenden, um Anzahl der Länder mit Gold zu ermitteln
print("Anzahl der Länder die eine Gold Medallie bekommen haben:", len(countriesWithGoldMedals))
