# Übung zu Programmiertechniken

## Advanced Flow Control

Ein Kollege aus einer anderen Abteilung hat unser Fahrtenbuch genutzt und eine 
kleine Anwendung entwickelt mit der Autos aus dem Fuhrpark an Mitarbeiter 
gegeben werden.

Die Anwendung ist relativ komplex geworden und der Kollege ist nun in einem 
anderen Projekt im Einsatz. Er steht maximal nur noch für Rückfragen zur 
Verfügung.

Er hat das Regelwerk mittels vieler `if`-`elsif`-`else` Verschachtelungen 
erstellt. Der Quellcode soll angepasst werden da weitere Anforderungen für die 
Fahrzeugvergabe hinzugefügt werden sollen.

Als erstes gilt es den Quellcode zu überarbeiten, so das neue Regeln schneller 
implementiert werden können.

Verbesserungsvorschläge dazu sind bereits von unserem Kollegen im Quellcode als 
Kommentar hinterlegt.

## Descriptors

Die Erstellung der Fahrzeuge in unserem Fahrtenbuch ermöglicht die Eingabe von 
unplausiblen Werten. Diese können beim Eintippen passieren. Hier soll unser 
Programm entsprechend gegensteuern und passende Fehlermeldungen erzeugen wenn 
Werte außerhalb eines vorgegebenen Bereiches liegen.

Unser neu erworbenes Wissen über Python Descriptors hilft uns die bestehenden 
Klassen entsprechend zu erweitern.

Ein Kollege mit Python-Grundkenntnissen hat an den Klassen bereits einige 
Kommentare für uns hinterlegt. Diese definieren die zu implementierenden 
Prüfwerte.
