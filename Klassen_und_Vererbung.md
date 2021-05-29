# Camp2Code
## Aufgabe zu Klassen und Vererbung

[![uml](https://github.com/bellmann-engineering/python-basic-to-advanced/raw/main/fahrzeug_uml.png)](https://github.com/bellmann-engineering/python-basic-to-advanced/raw/main/fahrzeug_uml.png)

Ziel ist es in Python Klassen wie auf dem UML Diagramm abgebildet zu erstellen.
- ``Fahrzeug``: Basisklasse (Elternklasse) 
- ``Kfz``: Kind von Fahrzeug
- ``Motorrad``: Kind von Fahrzeug
- ``LKW``: Kind von Fahrzeug
- ``Person``: Bildet eine Person ab

Es soll ermöglich werden Personen mit Name und Geburtsdatum anzulegen und einen Instanz von ``PKW``, ``LKW`` oder ``Motorrad`` mittels der ``hasFahrerlaubnis``-Methode zu fragen, ob die übergebene ``Person`` das jeweilige ``Fahrzeug`` (Basis) fahren darf.

Die Grundlage zur Entscheidung, ob eine Person fahren darf bildet nachfolgende Matrix:



| Alter  | Motorrad | PKW | LKW |
| ------------- | ------------- | ------------ | ------------- |
| < 18  | - | - | - |
| >= 18 | x | x | - |
| >= 24  | x | x | x |


Aufgabenschritte: 
1. Erstelle die Klassen ``Fahrzeug``, ``LKW``, ``PKW``, ``Motorrad`` und ``Person``
wie im Klassendiagramm abgebildet.
2. Stelle eine entsprechende Vererbung her
3. Füge Membervariablen hinzu:
``baujahr``, ``erstzulassung``, ``identNr``, ``farbe``
4. Füge der ``Person`` Klasse: 
- Vorname
- Nachname 
- und Geburtstag hinzu.
5. Erstelle in ``Motorrad`` und ``PKW`` Membervariablen:
- Motorrad: ``automatik`` (bool)
- PKW: ``hubraum`` (int)
6. Überlade die Methoden ``__repl__`` und ``__str__`` in allen Klassen entsprechend
7. Definiere eine Methode ``hasFahrerlaubnis(Person)`` mit Rückgabewert ``bool``.
Es soll der Aufruf ``audi.hasFahrerlaubnis(peter)`` möglich werden. (*audi* ist ein konkretes Objekt von ``PKW`` und *peter* eines von ``Person``).
Nutze dazu die Datumsberechnung sowie die statische Methode aus dem Modul ``datetime``: ``datetime.date.today()``.
8. Füge den Fahrzeugen eine Methode ``setSize (hoehe, breite, laenge)`` hinzu.
Die übergebenen Werte sollen in Membervariablen gespeichert werden.
9. Definiere eine ``@property`` namens ``volumen``
die das aus ``hoehe``, ``breite`` und ``laenge`` errechnete Volumen zurückgibt.

Optional:

10. Mache es möglich, dass Objekte hinsichtlich ihres Volumens verglichen werden können.
11. Überlade die ``__eq__`` Methode aller Klassen.
12. Überlade die ``__ne__`` Methode aller Klassen.
13. Kann ``Fahrzeug`` abstrakt gemacht werden? Falls ja, sieh dir das Modul ``abc`` dazu an.

