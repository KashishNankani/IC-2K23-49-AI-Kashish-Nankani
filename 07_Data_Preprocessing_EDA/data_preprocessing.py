import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ── 1. Create a sample dataset ──────────────────────────────────────────────
data = {
    'Name':   ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi'],
    'Age':    [25, 30, None, 22, 28, 35, None, 27],
    'Salary': [50000, 60000, 55000, None, 70000, 80000, 65000, None],
    'Gender': ['F', 'M', 'M', 'M', 'F', 'M', 'F', 'F'],
    'Score':  [88, 92, 75, 95, None, 60, 85, 90]
}

df = pd.DataFrame(data)

print("=" * 50)
print("ORIGINAL DATASET")
print("=" * 50)
print(df)

# ── 2. Basic Info ────────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("BASIC INFO")
print("=" * 50)
print(df.info())
print("\nShape:", df.shape)
print("\nDescriptive Statistics:")
print(df.describe())

# ── 3. Missing Values ────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("MISSING VALUES")
print("=" * 50)
print(df.isnull().sum())

# Fill missing numerical values with mean
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)
df['Score'].fillna(df['Score'].mean(), inplace=True)

print("\nAfter filling missing values:")
print(df.isnull().sum())

# ── 4. Encoding Categorical Data ─────────────────────────────────────────────
print("\n" + "=" * 50)
print("ENCODING CATEGORICAL DATA")
print("=" * 50)
df['Gender_Encoded'] = df['Gender'].map({'M': 0, 'F': 1})
print(df[['Name', 'Gender', 'Gender_Encoded']])

# ── 5. Normalization (Min-Max Scaling) ───────────────────────────────────────
print("\n" + "=" * 50)
print("NORMALIZATION (Min-Max Scaling)")
print("=" * 50)
for col in ['Age', 'Salary', 'Score']:
    df[col + '_Norm'] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())

print(df[['Age', 'Age_Norm', 'Salary', 'Salary_Norm']].head())

# ── 6. EDA — Visualizations ──────────────────────────────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle('Exploratory Data Analysis', fontsize=14)

# Age distribution
axes[0, 0].hist(df['Age'], bins=5, color='steelblue', edgecolor='black')
axes[0, 0].set_title('Age Distribution')
axes[0, 0].set_xlabel('Age')

# Salary by Gender
axes[0, 1].bar(df['Gender'].unique(),
               df.groupby('Gender')['Salary'].mean(),
               color=['salmon', 'steelblue'])
axes[0, 1].set_title('Average Salary by Gender')
axes[0, 1].set_ylabel('Salary')

# Score distribution
axes[1, 0].boxplot(df['Score'], patch_artist=True,
                   boxprops=dict(facecolor='lightgreen'))
axes[1, 0].set_title('Score Boxplot')

# Correlation heatmap
corr = df[['Age', 'Salary', 'Score']].corr()
im = axes[1, 1].imshow(corr, cmap='coolwarm')
axes[1, 1].set_xticks(range(len(corr)))
axes[1, 1].set_yticks(range(len(corr)))
axes[1, 1].set_xticklabels(corr.columns)
axes[1, 1].set_yticklabels(corr.columns)
axes[1, 1].set_title('Correlation Heatmap')
plt.colorbar(im, ax=axes[1, 1])

plt.tight_layout()
plt.savefig('eda_output.png')
plt.show()
print("\nPlot saved as eda_output.png")