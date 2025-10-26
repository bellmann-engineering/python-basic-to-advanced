### 1. Datensatz laden

```python
from sklearn.datasets import fetch_california_housing
import pandas as pd

housing = fetch_california_housing()
housing.keys()
```

---

### 2. Überblick verschaffen

```python
print("Feature-Namen:", housing.feature_names)
print("\nBeschreibung:\n", housing.DESCR)
```

---

### 3. DataFrame erstellen

```python
df = pd.DataFrame(housing.data, columns=housing.feature_names)
df["Price"] = housing.target
df.head()
```

---

### 4. Fehlende Werte prüfen

```python
df.isnull().sum()
```

---

### 5. Verteilung der Hauspreise visualisieren

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))
plt.hist(df["Price"], bins=30, color="steelblue", edgecolor="black")
plt.title("Verteilung der Hauspreise")
plt.xlabel("Preis in 100.000 USD")
plt.ylabel("Anzahl der Häuser")
plt.show()
```

---

### 6. Korrelation analysieren

```python
import seaborn as sns

corr = df.corr(numeric_only=True)
plt.figure(figsize=(10,8))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Korrelationsmatrix")
plt.show()
```

---

### 7. Stärkste Korrelate identifizieren

```python
corr_price = corr["Price"].abs().sort_values(ascending=False)
corr_price[corr_price > 0.5]
```

---

### 8. Aufteilung in Features (X) und Zielvariable (y)

```python
X = df.drop("Price", axis=1)
y = df["Price"]
```

---

### 9. Train-/Test-Split

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Trainingsdaten:", X_train.shape)
print("Testdaten:", X_test.shape)
```

---

### 10. Modelle anwenden

```python
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor

models = {
    "LinearRegression": LinearRegression(),
    "KNeighborsRegressor": KNeighborsRegressor(),
    "DecisionTreeRegressor": DecisionTreeRegressor(random_state=42)
}

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    plt.figure(figsize=(5,5))
    plt.scatter(y_test, y_pred, alpha=0.5)
    plt.xlabel("Echter Preis")
    plt.ylabel("Vorhergesagter Preis")
    plt.title(f"{name}: Vergleich Ist vs. Prognose")
    plt.plot([0,5], [0,5], 'r--')  # Referenzlinie
    plt.show()
```

---

### 11. Modellbewertung mit R² und MSE

```python
from sklearn.metrics import r2_score, mean_squared_error

for name, model in models.items():
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    print(f"{name}: R² = {r2:.3f}, MSE = {mse:.3f}")
```

---

### 12. Einfluss einzelner Variablen

```python
# Beispiel: Entferne weniger stark korrelierte Variablen und vergleiche das Ergebnis
selected_features = corr_price[corr_price > 0.3].index.drop("Price")
X_reduced = df[selected_features]

X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(X_reduced, y, test_size=0.2, random_state=42)

lr = LinearRegression()
lr.fit(X_train_r, y_train_r)
y_pred_r = lr.predict(X_test_r)

print("Reduziertes Modell: R² =", round(r2_score(y_test_r, y_pred_r), 3))
```

---

### 13. Diskussion um Location

Das Modell kann aus reinen Breiten- und Längengraden keinen sinnvollen räumlichen Zusammenhang „verstehen“, weil diese Zahlen keine lineare oder metrisch einfache Beziehung zu den Preisen ausdrücken.

Um den Standort sinnvoll nutzbar zu machen, müsste man die Koordinaten in Regionen oder Cluster umwandeln. Zum Beispiel nach Küstennähe („coastal“, „inland“, „mountain area“),
Technisch könnte man das über eine Zusatzspalte (z. B. Region = "Küste" / "Inland" / "Zentral-Kalifornien") abbilden.

Möchtest du, dass ich dir diese Notebook-Struktur als echte `.ipynb`-Datei generiere, damit du sie direkt herunterladen und in Jupyter öffnen kannst?
