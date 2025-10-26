# Machine Learning mit Scikit-Learn

Uns liegt ein Datensatz zu Häusern in Kalifornien vor. Wir wollen untersuchen, welche Zusammenhänge zwischen bestimmten Hausmerkmalen (Features) und den Hauspreisen bestehen.
Die Analyse soll in *Jupyter Notebook* durchgeführt werden.

---

### 1. Datensatz laden

Lade den Datensatz mit:

```python
from sklearn.datasets import fetch_california_housing
housing = fetch_california_housing()
```

---

### 2. Überblick verschaffen

Untersuche, welche Felder (`feature_names`) es gibt und welche Bedeutung sie haben. Analysiere die Spalten in `data`: Welche Wertebereiche und Ausprägungen haben sie?

---

### 3. DataFrame erstellen

Erstelle aus `housing.data` und den Hauspreisen in `housing.target` ein `pandas DataFrame`.
Füge die Spaltennamen hinzu.

---

### 4. Fehlende Werte prüfen

Überprüfe, ob im DataFrame Nullwerte (`NaN`) enthalten sind.

---

### 5. Preisverteilung visualisieren

Untersuche die Verteilung der Hauspreise mit einem Histogramm oder einem geeigneten Diagramm (`matplotlib` oder `seaborn`).

---

### 6. Korrelation analysieren

Erstelle eine Korrelationsmatrix und visualisiere sie (z. B. mit `sns.heatmap`).
Welche Variablen zeigen die stärkste Korrelation mit dem Hauspreis?

---

### 7. Stärkste Korrelate identifizieren

Welche Variablen (Features) korrelieren mit einem Betrag größer als 0.5 mit dem Preis (`target`)?
Gib diese aus und benenne die am stärksten korrelierende Variable.

---

### 8. Aufteilung in Features und Zielvariable

Teile das DataFrame auf in:

* **X**: die unabhängigen Variablen (Hausmerkmale)
* **y**: die abhängige Variable (Hauspreis)

---

### 9. Train-/Test-Split

Teile den Datensatz in Trainings- und Testdaten, z. B.:

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

Warum ist dieser Schritt wichtig?

---

### 10. Modelle anwenden

Trainiere drei verschiedene Regressionsmodelle auf den Trainingsdaten:

* `LinearRegression`
* `KNeighborsRegressor`
* `DecisionTreeRegressor`

Führe anschließend Vorhersagen (`predict`) auf den **Testdaten** durch.

---

### 11. Modelle bewerten

Vergleiche die echten Preise (`y_test`) mit den vorhergesagten Preisen der Modelle:

* Verwende Scatterplots (`plt.scatter(y_test, y_pred)`), um die Übereinstimmung zu visualisieren.
* Berechne zusätzlich den **R²-Score** und den **Mean Squared Error (MSE)** zur quantitativen Bewertung.

---

### 12. Einfluss einzelner Variablen (optional)

Entferne einige Variablen mit mittlerer Korrelation und beobachte, wie sich die Modellgüte verändert.

---

### 13. Diskussion (optional)

Warum scheint die Variable *Location* (geografische Lage) im Datensatz keinen starken Einfluss zu haben, obwohl man annehmen würde, dass Häuser an der Küste teurer sind?

---

### Weiterführende Informationen

* [Nächste-Nachbarn-Klassifikation (Wikipedia)](https://de.wikipedia.org/wiki/N%C3%A4chste-Nachbarn-Klassifikation)
* [DecisionTreeRegressor: Warum er für Zukunftsprognosen problematisch ist](https://towardsdatascience.com/decisiontreeregressor-stop-using-for-future-projections-e27104537f6a)
* [Streudiagramm (Wikipedia)](https://de.wikipedia.org/wiki/Streudiagramm)

---

Möchtest du, dass ich das als vollständige Notebook-Vorlage mit Codezellen formatiere (also sofort ausführbar in `.ipynb`)?
