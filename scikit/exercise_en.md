# Machine Learning with Scikit-Learn

We have a dataset of houses in California. We want to investigate which relationships exist between certain house characteristics (features) and house prices.
The analysis should be carried out in *Jupyter Notebook*.

---

### 1. Load the dataset

Load the dataset with:

```python
from sklearn.datasets import fetch_california_housing
housing = fetch_california_housing()
```

---

### 2. Get an overview

Investigate which fields (`feature_names`) exist and what they mean. Analyze the columns in `data`: What value ranges and characteristics do they have?

---

### 3. Create a DataFrame

Create a `pandas DataFrame` from `housing.data` and the house prices in `housing.target`.
Add the column names.

---

### 4. Check for missing values

Check whether the DataFrame contains null values (`NaN`).

---

### 5. Visualize the price distribution

Investigate the distribution of house prices using a histogram or another suitable chart (`matplotlib` or `seaborn`).

---

### 6. Analyze correlations

Create a correlation matrix and visualize it (e.g. with `sns.heatmap`).
Which variables show the strongest correlation with the house price?

---

### 7. Identify the strongest correlates

Which variables (features) correlate with the price (`target`) with an absolute value greater than 0.5?
Output them and name the most strongly correlated variable.

---

### 8. Split into features and target variable

Split the DataFrame into:

* **X**: the independent variables (house characteristics)
* **y**: the dependent variable (house price)

---

### 9. Train/test split

Split the dataset into training and test data, e.g.:

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

Why is this step important?

---

### 10. Apply models

Train three different regression models on the training data:

* `LinearRegression`
* `KNeighborsRegressor`
* `DecisionTreeRegressor`

Then make predictions (`predict`) on the **test data**.

---

### 11. Evaluate models

Compare the actual prices (`y_test`) with the predicted prices of the models:

* Use scatter plots (`plt.scatter(y_test, y_pred)`) to visualize the agreement.
* Additionally, calculate the **R² score** and the **Mean Squared Error (MSE)** for quantitative evaluation.

---

### 12. Influence of individual variables (optional)

Remove some variables with medium correlation and observe how the model quality changes.

---

### 13. Discussion (optional)

Why does the variable *Location* (geographic location) seem to have no strong influence in the dataset, even though one would assume that houses on the coast are more expensive?

---

### Further information

* [Nearest-neighbor classification (Wikipedia)](https://de.wikipedia.org/wiki/N%C3%A4chste-Nachbarn-Klassifikation)
* [DecisionTreeRegressor: Why it is problematic for future projections](https://towardsdatascience.com/decisiontreeregressor-stop-using-for-future-projections-e27104537f6a)
* [Scatter plot (Wikipedia)](https://de.wikipedia.org/wiki/Streudiagramm)
