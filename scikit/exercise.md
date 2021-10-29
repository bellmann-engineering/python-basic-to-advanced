# Machine Learning mit Scikit-Learn

Uns liegt ein Datensatz zu Häusern in Califonien vor. Wir wollen etwas über den Zusammenhang von Häuservariablen (Features) und Hauspreisen lernen.
Die Ausführung der Analyse soll in *jupyter notebook* stattfinden.

Orientiere dich bei der nachfolgenden Aufgabe an der Durchführung ähnlicher Aufgaben am _Boston_ Datensatz: [Link](https://github.com/bellmann-engineering/python-basic-to-advanced/blob/main/scikit/boston3.ipynb)

1. Lade den Datensatz mittels
`from sklearn.datasets import fetch_california_housing

housing = fetch_california_housing() `

2. Sieh dir an welche Felder es gibt und analysiere die Spalten in `data`. Welche Ausprägung haben diese?
3. Erstelle aus `data` und Hauspreisen in `target` ein `pandas dataframe`.
4. Gibt es Nullwerte in diesem?
5. Sieh dir die Verteilung der Häuser bezogen auf dem Preis innerhalb des Datensatzes an. Erstelle dazu mit `matplotlib` ein Diagramm.
6. Erstelle eine Korrelationsmatrix und treffe eine Aussage welche Variablen mit dem Hauspreis korrelieren.
7. Welche Variablen (Features) korrelieren mehr als 0.5? Gebe diese aus. Welche korreliert am Stärksten?
8. Teile das Dataframe in X und y Anteil auf. 
 - X enthält die Daten über die Häuser
 - y enthält die Preise (`target`)
9. Wende LinearRegression und KNeighborsRegressor und DecisionTreeRegressor als Modelle an (`fit` + `predict`).
10. Vergleiche die Daten aus y mit den vom Modell geschätzten Daten mittels eines Scatterplot.
11. Wie verhält es sich wenn du Variablen aus dem Datensatz entfernst die eine mittelstarke Korrelation aufweisen.
12. Warum hat die Variable Location scheinbar keinen Einfluss obwohl Häuser an der Küste doch sicherer teuer sind.

Aufgabe 11 + 12 sind optional.

Weiterführende Informationen:

https://de.wikipedia.org/wiki/N%C3%A4chste-Nachbarn-Klassifikation

https://towardsdatascience.com/decisiontreeregressor-stop-using-for-future-projections-e27104537f6a

https://de.wikipedia.org/wiki/Streudiagramm
