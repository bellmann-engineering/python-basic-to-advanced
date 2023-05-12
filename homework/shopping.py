## Aufgabe 1

# 1. Erstelle eine Liste namens fruits mit den Elementen "Apfel", "Banane", "Orange", "Mango".
fruits = ["Apfel", "Banane", "Orange", "Mango"]

# 2. Füge der Liste fruits das Element "Erdbeere" hinzu.
fruits.append("Erdbeere")

# 3. Entferne das Element "Banane" aus der Liste fruits.
fruits.remove("Banane")

# 4. Erstelle ein Tuple namens numbers mit den Elementen 1, 2, 3, 4.
numbers = (1, 2, 3, 4)

# 5. Füge dem Tuple numbers das Element 5 hinzu.
numbers = numbers + (5,)

# 6. Gib das Element an der dritten Stelle der Liste fruits aus.
print(fruits[2])

# 7. Gib das erste Element des Tuples numbers aus.
print(numbers[0])


## Aufgabe 2

# 1. Erstelle eine Liste namens shopping_list mit den Elementen "Milch", "Eier", "Brot", "Butter".
shopping_list = ["Milch", "Eier", "Brot", "Butter"]

# 2. Gib die Länge der Liste shopping_list aus.
print(len(shopping_list))

# 3. Füge der Liste shopping_list das Element "Käse" hinzu.
shopping_list.append("Käse")

# 4. Gib das erste und das letzte Element der Liste shopping_list aus.
print(shopping_list[0])
print(shopping_list[-1])

# 5. Erstelle ein Tuple namens coordinates mit den Elementen 12.345, 67.890.
coordinates = (12.345, 67.890)

# 6. Füge dem Tuple coordinates das Element 100 hinzu.
coordinates = coordinates + (100,)

# 7. Gib das zweite Element des Tuples coordinates aus.
print(coordinates[1])

# 8. Entferne das Element "Eier" aus der Liste shopping_list.
shopping_list.remove("Eier")



## Aufgabe 3

# 1. Erstelle eine Liste numbers mit den Elementen 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 2. Schreibe eine Schleife, die jedes Element der Liste numbers quadriert und das Ergebnis in squared_numbers speichert.
squared_numbers = []
for number in numbers:
    squared_numbers.append(number ** 2)

# 3. Schreibe eine Schleife, die jedes zweite Element der Liste squared_numbers ausgibt.
for i in range(1, len(squared_numbers), 2):
    print(squared_numbers[i])

# 4. Erstelle eine Liste colors mit den Elementen "Rot", "Grün", "Blau", "Gelb", "Lila".
colors = ["Rot", "Grün", "Blau", "Gelb", "Lila"]

# 5. Schreibe eine Schleife, die jedes Element der Liste colors zusammen mit seinem Index ausgibt.
for i, color in enumerate(colors):
    print(f"Die Farbe an Index {i} ist {color}.")

# 6. Schreibe eine Schleife, die jedes Element der Liste numbers durchläuft und prüft, ob das Element gerade oder ungerade ist. Gib für jedes Element eine entsprechende Meldung aus.
for number in numbers:
    if number % 2 == 0:
        print(f"{number} ist gerade.")
    else:
        print(f"{number} ist ungerade.")
