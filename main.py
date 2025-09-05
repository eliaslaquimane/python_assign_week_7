# ============================================
#           ELIAS ALBERTO LAQUIMANE
#=============================================
# Analyzing Data with Pandas and Matplotlib
# Assignment Solution
# ============================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------
# Load and Explore the Dataset
# ------------------------------
try:
    # Load Iris dataset from UCI repository using pandas
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
    columns = ["sepal length", "sepal width", "petal length", "petal width", "class"]
    df = pd.read_csv(url, header=None, names=columns)

    print("First five rows of the dataset:")
    print(df.head())

    print("\nDataset Info:")
    print(df.info())

    print("\nMissing values:")
    print(df.isnull().sum())

    # Clean missing values if any (Iris dataset usually has none)
    df = df.dropna()

except FileNotFoundError:
    print("Error: Dataset file not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# ------------------------
# Basic Data Analysis
# ------------------------
print("\nBasic Statistics:")
print(df.describe())

# Group by species and calculate mean of numerical features
group_means = df.groupby("class").mean(numeric_only=True)
print("\nAverage measurements per species:")
print(group_means)


# ------------------------
#  Data Visualization
# ------------------------

# 1. Line Chart - Sepal length across samples
plt.figure(figsize=(8, 5))
plt.plot(df.index, df["sepal length"], label="Sepal Length")
plt.title("Line Chart - Sepal Length Across Samples")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
try:
    plt.show()
except UserWarning:
    pass

# 2. Bar Chart - Average petal length per species
plt.figure(figsize=(8, 5))
sns.barplot(x="class", y="petal length", hue="class", data=df, errorbar=None, palette="viridis", legend=False)
plt.title("Bar Chart - Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
try:
    plt.show()
except UserWarning:
    pass

# 3. Histogram - Distribution of Sepal Width
plt.figure(figsize=(8, 5))
plt.hist(df["sepal width"], bins=15, color="skyblue", edgecolor="black")
plt.title("Histogram - Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
try:
    plt.show()
except UserWarning:
    pass

# 4. Scatter Plot - Sepal Length vs Petal Length
plt.figure(figsize=(8, 5))
sns.scatterplot(x="sepal length", y="petal length", hue="class", data=df, palette="deep")
plt.title("Scatter Plot - Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
try:
    plt.show()
except UserWarning:
    pass


# ---------------------------
#   Findings | Observations
# ---------------------------
"""
    Observations:
    1. Each species has distinct average measurements (petal length and width are strong separators).
    2. The histogram shows that Sepal Width is normally distributed with some skew.
    3. The scatter plot clearly shows clustering of species – especially Setosa, which is well separated.
    4. Trends across sample indices (line chart) show variation in sepal length, but no clear seasonality 
        (since it’s not time-series data).
"""
