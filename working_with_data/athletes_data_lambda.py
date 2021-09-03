import csv  # build in module
import functools

# Alle Daten aus der CSV Datei im Arbeitsspeicher ablegen
csv_data = []

# Achtung: Zeichensatz der csv Datei ist utf8
with open("athletes.csv", encoding="utf8") as file:
    csv_data = [row for row in csv.DictReader(file)]

# 1. Anzahl alle Goldmedallien zählen
# sum
total = sum([int(row["gold"]) for row in csv_data])
print("[sum] Anzahl Gold Medallien (overall): ", total)

# sum + map
total = sum(map(lambda item: int(item["gold"]), csv_data))
print("[map + sum] Anzahl Gold Medallien (overall): ", total)

# reducer
total = functools.reduce(lambda val, row: val + int(row["gold"]), csv_data, 0)
print("[reduce] Anzahl Gold Medallien (overall): ", total)

# 2. Es wird ein Dictionary verwendet und value beim Key (Land) hochgezählt
countries = {}


def reducer(value, row):
    country = row["nationality"]
    gold_medals = int(row["gold"])

    if country not in value:
        value[country] = gold_medals
    else:
        value[country] += gold_medals

    return value


countries = functools.reduce(reducer, csv_data, {})

# Alle Länder mit Gold-Medallienanzahl:
print("Alle Länder mit Anzahl Gold Medallien dahinter", countries)

# 3. Um die Anzahl deutscher Medallien auszugeben
print("GER: ", countries["GER"])

print("Land mit den meisten Goldmedallien", max(countries, key=countries.get))

# 4. weitere Möglichkeit: wir verwenden eine Liste, bilden Tuples und summieren

print("Alle Gold Medallien", sum([int(row["gold"]) for row in csv_data]))
print("Alle Silber Medallien", sum([int(row["silver"]) for row in csv_data]))
print("Alle Bronze Medallien", sum([int(row["bronze"]) for row in csv_data]))

# 5. Anzahl Gold Medallien direkt mit sum im CSV Reader ermitteln
total = sum(int(row["gold"]) for row in csv_data)
print("Anz. Gold: ", total)

# 6. Filtern nach Ländern die mindestens eine Gold Medallie haben / eine Gold Medallie haben
def countries_gold_reducter(data, row):
    country = row["nationality"]
    gold_count = int(row["gold"])

    if gold_count == 0:
        return data

    if country not in data:
        data[country] = gold_count
    else:
        data[country] += gold_count

    return data


countriesWithGoldMedals = functools.reduce(countries_gold_reducter, csv_data, {})
print("Ländern mit Gold:", countriesWithGoldMedals)

# 7. Anzahl der Einträge aus 5 verwenden, um Anzahl der Länder mit Gold zu ermitteln
print(
    "Anzahl der Länder die eine Gold Medallie bekommen haben:",
    len(countriesWithGoldMedals),
    sorted(countriesWithGoldMedals),
)
