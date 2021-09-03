import csv  # build in module
import functools

# Alle Daten aus der CSV Datei im Arbeitsspeicher ablegen
csv_data = []

# Achtung: Zeichensatz der csv Datei ist utf8
with open("athletes.csv", encoding="utf8") as file:
    csv_data = [row for row in csv.DictReader(file)]

# 1.
# sum
total = sum([int(row["gold"]) for row in csv_data])
print("[sum] Anzahl Gold Medallien (overall): ", total)

# sum + map
total = sum(map(lambda item: int(item["gold"]), csv_data))
print("[map + sum] Anzahl Gold Medallien (overall): ", total)

# reducer
total = functools.reduce(lambda val, row: val + int(row["gold"]), csv_data, 0)
print("[reduce] Anzahl Gold Medallien (overall): ", total)

# 2.
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

print("Alle Länder mit Anzahl Gold Medallien dahinter", countries)

# 3.
print("GER: ", countries["GER"])

print("Land mit den meisten Goldmedallien", max(countries, key=countries.get))

# 4.

print("Alle Gold Medallien", sum([int(row["gold"]) for row in csv_data]))
print("Alle Silber Medallien", sum([int(row["silver"]) for row in csv_data]))
print("Alle Bronze Medallien", sum([int(row["bronze"]) for row in csv_data]))

# 5.
total = sum(int(row["gold"]) for row in csv_data)
print("Anz. Gold: ", total)

# 6.
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

# 7.
print(
    "Anzahl der Länder die eine Gold Medallie bekommen haben:",
    len(countriesWithGoldMedals),
    sorted(countriesWithGoldMedals),
)
