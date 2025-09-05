# ============================================
#           ELIAS ALBERTO LAQUIMANE
#=============================================
# Analyzing Data with Pandas and Matplotlib
# Assignment Solution
# ============================================

## Overview

This assignment demonstrates how to analyze and visualize the classic Iris dataset using Python libraries: **pandas**, **matplotlib**, and **seaborn**.

## Steps

1. **Load and Explore the Dataset**
    - The Iris dataset is loaded directly from the UCI repository.
    - Data is checked for missing values and basic info is displayed.

2. **Basic Data Analysis**
    - Descriptive statistics are computed for all features.
    - The dataset is grouped by species (`class`) to show average measurements per species.

3. **Data Visualization**
    - **Line Chart:** Shows sepal length across all samples.
    - **Bar Chart:** Displays average petal length for each species.
    - **Histogram:** Illustrates the distribution of sepal width.
    - **Scatter Plot:** Visualizes the relationship between sepal length and petal length, colored by species.

## Findings / Observations

- Each species has distinct average measurements (petal length and width are strong separators).
- The histogram shows that sepal width is normally distributed with some skew.
- The scatter plot clearly shows clustering of species – especially Setosa, which is well separated.
- Trends across sample indices (line chart) show variation in sepal length, but no clear seasonality (since it’s not time-series data).

## How to Run

1. Ensure you have Python installed.
2. Install required libraries:
    ```
    pip install -r requirements.txt
    ```
   Or, if you prefer manual installation:
    ```
    pip install pandas matplotlib seaborn
    ```
3. Run the script:
    ```
    python main.py
    ```

## Notes

- Plots are displayed using `matplotlib` and `seaborn`. If running in a non-interactive environment, warnings about `plt.show()` may appear but can be ignored.
- The code is robust to missing values, though the Iris dataset typically has none.

## Author

**Elias Alberto Laquimane**
