# 1. Erstelle ein leeres Dictionary telefonbuch.
telefonbuch = {}

# 2. Füge dem Telefonbuch vier Einträge hinzu.
telefonbuch["Max Mustermann"] = "123456789"
telefonbuch["Lisa Müller"] = "987654321"
telefonbuch["Peter Meier"] = "456123789"
telefonbuch["Susanne Schmidt"] = "789654123"

# 3. Gib die Telefonnummer von "Max Mustermann" aus.
print("Telefonnummer von Max Mustermann:", telefonbuch["Max Mustermann"])

# 4. Entferne den Eintrag von "Peter Meier" aus dem Telefonbuch.
del telefonbuch["Peter Meier"]

# 5. Ändere die Telefonnummer von "Lisa Müller" auf "555555555".
telefonbuch["Lisa Müller"] = "555555555"

# 6. Füge dem Telefonbuch einen weiteren Eintrag hinzu.
telefonbuch["Markus Fischer"] = "321456987"

# 7. Gib alle Einträge im Telefonbuch aus.
print("Telefonbuch:")
for name, telefonnummer in telefonbuch.items():
    print(name + ":", telefonnummer)
