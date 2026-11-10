# Data Preprocessing & EDA – Theory Notes

## What is Data Preprocessing?

Data preprocessing is the process of cleaning, transforming, and organizing
raw data before using it for analysis or feeding it into a machine learning
model. Real-world data is often messy — it may have missing values, wrong
data types, inconsistent formats, or extreme outliers.

If we train a model on bad data, we get bad results. This is why
preprocessing is considered one of the most important steps in any AI or
data science pipeline.

---

## What is EDA?

Exploratory Data Analysis (EDA) is the process of analyzing and
visualizing a dataset to understand its structure, spot patterns, find
anomalies, and check assumptions before building any model.

EDA answers questions like:
- What does the data look like?
- Are there missing values?
- How are variables distributed?
- Are there any correlations between features?

---

## Steps in Data Preprocessing

### 1. Loading the Data
We use **Pandas** to load data from CSV files, Excel sheets, or create
it manually using dictionaries.

```python
import pandas as pd
df = pd.read_csv('data.csv')
```

### 2. Exploring the Data
Before doing anything, understand what you have:

```python
df.shape        # rows and columns
df.info()       # data types and non-null counts
df.describe()   # statistical summary
df.head()       # first 5 rows
```

### 3. Handling Missing Values
Missing values appear as `NaN`. We can:
- **Drop** rows/columns with missing values
- **Fill** them with mean, median, mode, or a fixed value

```python
df['Age'].fillna(df['Age'].mean(), inplace=True)
```

Filling with mean is common for numerical columns when data is missing
at random and not too much of it is missing.

### 4. Encoding Categorical Data
Machine learning models work with numbers, not text. So we convert
categories like 'Male'/'Female' into numbers.

```python
df['Gender'] = df['Gender'].map({'M': 0, 'F': 1})
```

This is called **Label Encoding**. For more than 2 categories,
we use **One-Hot Encoding**.

### 5. Normalization / Scaling
Features with very different ranges (e.g. Age: 20–60, Salary: 30000–90000)
can bias models. We scale them to a common range.

**Min-Max Normalization** scales values between 0 and 1:

```
x_norm = (x - x_min) / (x_max - x_min)
```

**Standardization (Z-score)** scales to mean=0 and std=1:

```
x_std = (x - mean) / std_deviation
```

---

## EDA Techniques

### Histograms
Show the distribution of a numerical variable — how values are spread.

### Boxplots
Show the median, quartiles, and outliers of a variable.

### Bar Charts
Compare values across categories (e.g. average salary by gender).

### Correlation Heatmap
Shows how strongly pairs of numerical variables are related to each other.
Values range from -1 (strong negative) to +1 (strong positive).

---

## Libraries Used

| Library | Purpose |
|---------|---------|
| NumPy | Numerical operations, arrays |
| Pandas | Data loading, cleaning, manipulation |
| Matplotlib | Plotting basic charts |
| Seaborn | Statistical visualizations |

---

## Why is This Important in AI?

- **Garbage in, garbage out** — a model is only as good as its data
- Preprocessing removes noise and inconsistencies
- EDA helps us choose the right features and algorithms
- Scaling ensures no single feature dominates the model
- Encoding allows algorithms to work with all types of data

---

## Real-World Applications

- Cleaning medical records before training a diagnosis model
- Processing customer data for recommendation systems
- Preparing financial data for fraud detection
- Cleaning sensor data in IoT and robotics