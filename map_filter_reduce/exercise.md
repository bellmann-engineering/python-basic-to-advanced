Ziel der Aufgabenstellung ist *Funktionale Programmierung* besser kennenzulernen. Mit kleinen Aufgaben zur Verarbeitung von Daten wollen wir im Umgang mit `map/filter/reduce/zip` sicher werden. 

**Aufgaben:**

1. Erstelle eine Liste von Namen. Alle Namen in der Liste sind in Kleinbuchstaben. Nun soll der erste Buchstabe eines jeden Namens Großgeschrieben werden. 
 - a) Verwerden dazu zuerst die imperative/native Herangehensweise (Schleife)
 - b) danach die `map` Funktion
2. Eine Liste von Gleitkommazahlen  `[6.56773, 9.57668, 4.00914, 56.24241, 9.01344, 32.00013]` soll gerundet werden. 
 - a) Runde alle Einträge auf 2 Nachkommastellen
 - b) Runde den ersten Eintrag auf eine Stelle, den zweiten auf zwei Stellen, den dritten auf drei, usw.
3. Verwende die `zip` Funktion, um die Listen 
`my_chars = ['a', 'b', 'c', 'd', 'e']` und 
`my_nums = [1,2,3,4,5]`
zusammenzuführen: a zu 1, b zu 2, ...
4. Filter eine Liste von `scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65, 92, 85]` sodass nurnoch Einträge größer als 80 übrig bleiben.
5. Filter eine Liste von Wörtern, sodass nur die Wörter übrig bleiben die ein sog. Palindrom sind (Vor- und Rückwärts das gleiche Wort). Hierbei soll Groß- und Kleinschreibung keine Rolle spielen. `myStrings = ("Regallager", "Anna", "C++", "python", "Volkswagen", "PHP")`
6. Nutze die `reduce` Funktion um eine Liste von Zahlen `[3, 4, 6, 9, 34, 12]` zu summieren. Hierbei soll zuerst 3+4(=7), dann 7+6, ... gerechnet werden. Hinweis: Es wird `from functools import reduce` dazu benötigt.

---

(Optionale) ganzheitliche **Zusatzaufgabe:**

Angenommen, du hast eine Liste von Mitarbeiterdaten in Form von Dictionaries, wobei jedes Dictionary die folgenden Informationen enthält:
```python
employee = {
    "name": "Max Mustermann",
    "id": "EMP123",
    "stundenlohn": 20.0,
    "stunden gearbeitet": [40, 35, 42, 38, 45]
}

```

1. Erstelle eine Liste von solchen Mitarbeiterdaten-Dictionaries mit Informationen von mindestens 5 Mitarbeitern.

2. Verwende `map`, um das Gesamtgehalt (Stundenlohn * Stunden gearbeitet) für jeden Mitarbeiter zu berechnen und eine neue Liste mit diesen Gesamtgehältern zu erstellen.

3. Verwende `filter`, um eine Liste der Mitarbeiter zu erstellen, die ein Gesamtgehalt von mindestens 4000 Euro haben.

4. Erstelle eine Liste mit den Namen der Mitarbeiter, die die Filterung in Schritt 3 bestanden haben.

5. Verwende die `reduce` Funktion, um die Gesamtsumme aller Gesamtgehälter zu berechnen. Sprich, die Lohnkosten, die das Unternehmen hat.

6. Sortiere die Liste der Mitarbeiterdaten nach den Mitarbeiter-IDs in aufsteigender Reihenfolge.
