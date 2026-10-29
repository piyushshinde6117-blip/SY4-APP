import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# STEP 1: Generate Synthetic Dataset
# ==========================================
np.random.seed(42)
n_samples = 1000

data = {
    'CustomerID': range(1001, 1001 + n_samples),
    'Age': np.random.randint(18, 70, size=n_samples),
    'Tenure': np.random.randint(0, 72, size=n_samples),
    'MonthlyCharges': np.random.uniform(20.0, 120.0, size=n_samples),
    'TotalCharges': np.random.uniform(100.0, 8000.0, size=n_samples),
    'ContractType': np.random.choice(['Month-to-Month', 'One Year', 'Two Year'], size=n_samples, p=[0.5, 0.3, 0.2]),
    'Churn': np.random.choice(['Yes', 'No'], size=n_samples, p=[0.25, 0.75])
}

df = pd.DataFrame(data)

# Introduce some missing values randomly for practice
df.loc[np.random.choice(df.index, 30), 'MonthlyCharges'] = np.nan
df.loc[np.random.choice(df.index, 20), 'TotalCharges'] = np.nan

print("=== 1. DATASET CREATED (First 5 rows) ===")
print(df.head(), "\n")

# ==========================================
# STEP 2: Data Cleaning & Missing Values
# ==========================================
print("=== 2. MISSING VALUES BEFORE CLEANING ===")
print(df.isnull().sum(), "\n")

# Fill missing values with the median of each column
df['MonthlyCharges'] = df['MonthlyCharges'].fillna(df['MonthlyCharges'].median())
df['TotalCharges'] = df['TotalCharges'].fillna(df['TotalCharges'].median())

print("=== MISSING VALUES AFTER CLEANING ===")
print(df.isnull().sum(), "\n")

# ==========================================
# STEP 3: Summary Statistics
# ==========================================
print("=== 3. NUMERICAL SUMMARY STATISTICS ===")
print(df.describe(), "\n")

print("=== CATEGORICAL SUMMARY STATISTICS ===")
print(df.describe(include=['object']), "\n")

churn_counts = df['Churn'].value_counts(normalize=True) * 100
print(f"=== CHURN RATE PERCENTAGE ===\n{churn_counts}\n")

# ==========================================
# STEP 4: Visualizations
# ==========================================
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1. Churn Distribution
sns.countplot(x='Churn', data=df, ax=axes[0, 0], palette='Set2')
axes[0, 0].set_title('Customer Churn Distribution')

# 2. Tenure vs Churn
sns.boxplot(x='Churn', y='Tenure', data=df, ax=axes[0, 1], palette='Set2')
axes[0, 1].set_title('Tenure vs Churn')

# 3. Monthly Charges vs Churn
sns.boxplot(x='Churn', y='MonthlyCharges', data=df, ax=axes[1, 0], palette='Set2')
axes[1, 0].set_title('Monthly Charges vs Churn')

# 4. Contract Type vs Churn
sns.countplot(x='ContractType', hue='Churn', data=df, ax=axes[1, 1], palette='Set2')
axes[1, 1].set_title('Churn by Contract Type')

plt.tight_layout()
plt.show()