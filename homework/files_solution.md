### Übung: Zugriff auf das Dateisystem mit Python

#### Ziel:
Umgang mit dem Dateisystem.

### Schritt 1: Erstellen eines neuen Verzeichnisses

**Aufgabe:**
Erstelle ein neues Verzeichnis namens `mein_verzeichnis` im aktuellen Arbeitsverzeichnis.

**Hinweis:**
Verwende die `os`-Bibliothek, um Verzeichnisse zu erstellen.

```python
import os

# Verzeichnis erstellen
os.mkdir('mein_verzeichnis')
```

#### Test:
Überprüfe, ob das Verzeichnis tatsächlich erstellt wurde. Du kannst dies auch manuell im Dateisystem überprüfen.

### Schritt 2: Erstellen einer Datei im neuen Verzeichnis

**Aufgabe:**
Erstelle eine Datei mit dem Namen `meine_datei.txt` im Verzeichnis `mein_verzeichnis` und schreibe einige Textdaten in diese Datei.

**Hinweis:**
Verwende die `open()`-Funktion mit dem Modus `'w'`, um die Datei zu erstellen und zu beschreiben.

```python
# Datei im Verzeichnis erstellen und Daten schreiben
with open('mein_verzeichnis/meine_datei.txt', 'w') as file:
    file.write("Dies ist ein Test. Hallo Welt!")
```

#### Test:
Überprüfe, ob die Datei `meine_datei.txt` im Verzeichnis `mein_verzeichnis` vorhanden ist und ob die Daten korrekt geschrieben wurden.

### Schritt 3: Lesen der Datei

**Aufgabe:**
Lese den Inhalt der Datei `meine_datei.txt` und gebe den Inhalt auf der Konsole aus.

**Hinweis:**
Verwende `open()` mit dem Modus `'r'` zum Lesen der Datei.

```python
# Datei lesen und Inhalt ausgeben
with open('mein_verzeichnis/meine_datei.txt', 'r') as file:
    inhalt = file.read()
    print(inhalt)
```

#### Test:
Die Ausgabe sollte der Text sein, den du in Schritt 2 in die Datei geschrieben hast.

### Schritt 4: Anhängen von Daten an die Datei

**Aufgabe:**
Füge der Datei `meine_datei.txt` eine neue Zeile mit dem Text "Dies ist eine hinzugefügte Zeile." hinzu.

**Hinweis:**
Verwende den Modus `'a'` (Anhängen) zum Öffnen der Datei.

```python
# Daten an die Datei anhängen
with open('mein_verzeichnis/meine_datei.txt', 'a') as file:
    file.write("\nDies ist eine hinzugefügte Zeile.")
```

#### Test:
Überprüfe den Inhalt der Datei, um sicherzustellen, dass die neue Zeile erfolgreich hinzugefügt wurde.

### Schritt 5: Auflisten der Dateien in einem Verzeichnis

**Aufgabe:**
Liste alle Dateien im Verzeichnis `mein_verzeichnis` auf.

**Hinweis:**
Verwende `os.listdir()` oder `os.walk()` zum Auflisten der Dateien im Verzeichnis.

```python
# Alle Dateien im Verzeichnis auflisten
dateien = os.listdir('mein_verzeichnis')
print(dateien)
```

#### Test:
Überprüfe, ob die Datei `meine_datei.txt` in der Liste der Dateien erscheint.

### Schritt 6: Löschen der Datei

**Aufgabe:**
Lösche die Datei `meine_datei.txt` aus dem Verzeichnis `mein_verzeichnis`.

**Hinweis:**
Verwende `os.remove()`, um eine Datei zu löschen.

```python
# Datei löschen
os.remove('mein_verzeichnis/meine_datei.txt')
```

#### Test:
Überprüfe, ob die Datei `meine_datei.txt` aus dem Verzeichnis gelöscht wurde.

### Schritt 7: Löschen des Verzeichnisses

**Aufgabe:**
Lösche das Verzeichnis `mein_verzeichnis`. Achte darauf, dass das Verzeichnis leer ist, bevor du es löschst.

**Hinweis:**
Verwende `os.rmdir()`, um das Verzeichnis zu löschen.

```python
# Verzeichnis löschen
os.rmdir('mein_verzeichnis')
```

#### Test:
Überprüfe, ob das Verzeichnis `mein_verzeichnis` gelöscht wurde.

### Schritt 8: Fehlerbehandlung

**Aufgabe:**
Füge eine Fehlerbehandlung hinzu, um sicherzustellen, dass der Code robust ist. Zum Beispiel: Wenn das Verzeichnis oder die Datei bereits existiert, sollte eine entsprechende Nachricht angezeigt werden. Wenn beim Löschen der Datei oder des Verzeichnisses ein Fehler auftritt, soll eine Fehlermeldung ausgegeben werden.

**Hinweis:**
Verwende `try-except`, um Fehler abzufangen.

```python
try:
    os.mkdir('mein_verzeichnis')
except FileExistsError:
    print("Das Verzeichnis 'mein_verzeichnis' existiert bereits.")

try:
    os.remove('mein_verzeichnis/meine_datei.txt')
except FileNotFoundError:
    print("Die Datei 'meine_datei.txt' wurde nicht gefunden.")
```

#### Test:
Teste verschiedene Szenarien, wie das Erstellen eines Verzeichnisses, das bereits existiert, oder das Löschen einer nicht existierenden Datei.

---
