## Aufgabe 1

# 1. Erstelle eine Klasse Person mit den Eigenschaften name, alter und wohnort.
class Person:
    def __init__(self, name, alter, wohnort):
        self.name = name
        self.alter = alter
        self.wohnort = wohnort

    # 2. Definiere eine Methode say_hello, die eine Begrüßung mit dem Namen der Person ausgibt.
    def say_hello(self):
        print(f"Hallo, mein Name ist {self.name}.")

# 3. Erstelle ein Objekt person1 der Klasse Person.
person1 = Person("Max Mustermann", 30, "Berlin")

# 4. Rufe die Methode say_hello des Objekts person1 auf.
person1.say_hello()

# 5. Erstelle eine Unterklasse Student der Klasse Person mit der zusätzlichen Eigenschaft matrikelnummer.
class Student(Person):
    def __init__(self, name, alter, wohnort, matrikelnummer):
        super().__init__(name, alter, wohnort)
        self.matrikelnummer = matrikelnummer

# 7. Erstelle ein Objekt student1 der Klasse Student.
student1 = Student("Anna Müller", 20, "Hamburg", 123456)

# 8. Rufe die Methode say_hello des Objekts student1 auf.
student1.say_hello()

## Aufgabe 2

# 1. Erstelle eine Klasse Shape mit der Methode area(), die die Fläche der Form berechnet und zurückgibt.
class Shape:
    def area(self):
        pass

# 2. Definiere eine Unterklasse Rectangle der Klasse Shape mit den Eigenschaften width und height.
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # 3. Implementiere die Methode area() für die Klasse Rectangle, um die Fläche des Rechtecks zu berechnen.
    def area(self):
        return self.width * self.height

# 4. Definiere eine Unterklasse Square der Klasse Rectangle mit der Eigenschaft side_length.
class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    # 5. Implementiere die Methode area() für die Klasse Square, um die Fläche des Quadrats zu berechnen.
    def area(self):
        return self.width ** 2

# 6. Erstelle ein Rechteck-Objekt rect1 mit einer Breite von 4 und einer Höhe von 3.
rect1 = Rectangle(4, 3)

# 7. Rufe die Methode area() des Rechteck-Objekts rect1 auf und gib das Ergebnis aus.
print("Rechteckfläche:", rect1.area())

# 8. Erstelle ein Quadrat-Objekt square1 mit einer Seitenlänge von 5.
square1 = Square(5)

# 9. Rufe die Methode area() des Quadrat-Objekts square1 auf und gib das Ergebnis aus.
print("Quadratfläche:", square1.area())
