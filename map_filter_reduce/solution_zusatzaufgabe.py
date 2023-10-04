from functools import reduce

# 1. Erstelle eine Liste von solchen Mitarbeiterdaten-Dictionaries mit deutschen Namen
employees = [
    {
        "name": "Max Mustermann",
        "id": "EMP123",
        "stundenlohn": 20.0,
        "stunden gearbeitet": [40, 35, 42, 38, 45]
    },
    {
        "name": "Maria Musterfrau",
        "id": "EMP456",
        "stundenlohn": 18.5,
        "stunden gearbeitet": [37, 40, 36, 40, 32]
    },
    {
        "name": "Franz Müller",
        "id": "EMP789",
        "stundenlohn": 22.0,
        "stunden gearbeitet": [45, 38, 40, 41, 39]
    },
    {
        "name": "Anna Schmidt",
        "id": "EMP101",
        "stundenlohn": 19.5,
        "stunden gearbeitet": [42, 37, 39, 38, 41]
    },
    {
        "name": "Sabine Schneider",
        "id": "EMP202",
        "stundenlohn": 21.5,
        "stunden gearbeitet": [36, 40, 44, 35, 42]
    }
]

# 2. Verwende `map`, um das Gesamtgehalt für jeden Mitarbeiter zu berechnen
total_salaries = list(map(lambda emp: emp["stundenlohn"] * sum(emp["stunden gearbeitet"]), employees))

# 3. Verwende `filter`, um Mitarbeiter mit einem Gesamtgehalt von mindestens 4000 Euro zu filtern
filtered_employees = list(filter(lambda emp: emp["stundenlohn"] * sum(emp["stunden gearbeitet"]) >= 4000, employees))

# 4. Erstelle eine Liste der Namen der Mitarbeiter, die die Filterung in Schritt 3 bestanden haben
filtered_employee_names = [emp["name"] for emp in filtered_employees]

# 5. Verwende die `reduce` Funktion, um die Gesamtsumme aller Gehälter zu berechnen
total_salary_sum = reduce(lambda x, y: x + y, total_salaries)

# 6. Sortiere die Liste der Mitarbeiterdaten nach den Mitarbeiter-IDs in aufsteigender Reihenfolge
sorted_employees = sorted(employees, key=lambda emp: emp["id"])

# Ausgabe der Ergebnisse
print("Gesamtgehälter:", total_salaries)
print("Mitarbeiter mit einem Gesamtgehalt von mindestens 1000 Euro:", filtered_employee_names)
print("Gesamtsumme aller Gehälter:", total_salary_sum)
print("Mitarbeiterdaten nach Mitarbeiter-IDs sortiert:")
for emp in sorted_employees:
    print(emp)
