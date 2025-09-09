# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Task 1: Load and Explore Dataset

try:
    iris = load_iris(as_frame=True)
    df = iris.frame
    df['species'] = iris.target_names[iris.target]
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("Error: Dataset file not found.")
except Exception as e:
    print("An error occurred while loading dataset:", e)

# Display first 5 rows
print("\nFirst 5 rows of the dataset:")
print(df.head())

# Check structure
print("\nData types and null values:")
print(df.info())
print("\nMissing values per column:")
print(df.isnull().sum())

# Task 2: Basic Data Analysis

# Basic statistics
print("\nDescriptive statistics:")
print(df.describe())

# Group by species and compute mean of numerical columns
grouped = df.groupby("species").mean()
print("\nMean values by species:")
print(grouped)

# Observation example
print("\nObservations:")
print("- Iris-setosa generally has the smallest petals.")
print("- Iris-virginica tends to have the largest measurements.")

# Task 3: Data Visualization
plt.style.use("seaborn-v0_8")  # Apply seaborn style for better visuals

# 1. Line chart - just for demo, we’ll plot sepal length values
plt.figure(figsize=(8,5))
plt.plot(df.index, df["sepal length (cm)"], label="Sepal Length", color="blue")
plt.title("Sepal Length Trend")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# 2. Bar chart - average petal length per species
plt.figure(figsize=(8,5))
sns.barplot(x="species", y="petal length (cm)", data=df, estimator="mean", ci=None)
plt.title("Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# 3. Histogram - distribution of sepal width
plt.figure(figsize=(8,5))
plt.hist(df["sepal width (cm)"], bins=20, color="green", alpha=0.7)
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot - sepal length vs petal length
plt.figure(figsize=(8,5))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="species", data=df)
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.show()

# Findings

print("\nFindings:")
print("1. Setosa has shorter petals and sepals compared to other species.")
print("2. Versicolor is intermediate in size for most features.")
print("3. Virginica has the longest petals and sepals, making it easier to distinguish.")