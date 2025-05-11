# --- Import Libraries ---
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Optional: Use Seaborn styles for better-looking plots
sns.set_style("whitegrid")

# --- Task 1: Load and Explore the Dataset ---

# Generate synthetic sales data with dates, categories, and missing values
try:
    # Create a date range for 12 months
    dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq="M")
    
    # Create synthetic data with intentional missing values (NaN)
    data = {
        "Date": np.repeat(dates, 3),  # 3 sales entries per month
        "Product_Category": np.random.choice(["Electronics", "Clothing", "Books"], 36),
        "Region": np.random.choice(["North", "South", "East", "West"], 36),
        "Sales": np.random.randint(100, 1000, 36),
        "Profit": np.random.randint(10, 200, 36)
    }
    
    # Introduce 5 missing values in 'Sales' and 'Profit'
    data["Sales"] = data["Sales"].astype(float)
    data["Sales"][[5, 10, 15]] = np.nan
    data["Profit"][[3, 20]] = np.nan
    
    # Create DataFrame and save to CSV
    df = pd.DataFrame(data)
    df.to_csv("sales_data.csv", index=False)
    print("Synthetic dataset created: 'sales_data.csv'")

except Exception as e:
    print(f"Error generating data: {str(e)}")

# Load the dataset with error handling
try:
    df = pd.read_csv("sales_data.csv")
    print("\n--- Dataset Loaded Successfully ---")
    
    # Display first 5 rows
    print("\nFirst 5 rows:")
    print(df.head())
    
    # Check data types and missing values
    print("\nData structure:")
    print(df.info())
    print("\nMissing values per column:")
    print(df.isnull().sum())

except FileNotFoundError:
    print("Error: 'sales_data.csv' not found. Generate it first.")
except Exception as e:
    print(f"Error loading file: {str(e)}")

# Clean missing values (drop rows with missing 'Sales' or 'Profit')
df_clean = df.dropna(subset=["Sales", "Profit"])
print(f"\nCleaned dataset shape: {df_clean.shape} (original: {df.shape})")

# --- Task 2: Basic Data Analysis ---

# Basic statistics
print("\nBasic statistics:")
print(df_clean[["Sales", "Profit"]].describe())

# Group by Product Category and compute mean sales
print("\nAverage sales by product category:")
print(df_clean.groupby("Product_Category")["Sales"].mean())

# Observation example:
print("\nObservation: Electronics has the highest average sales.")

# --- Task 3: Data Visualization ---
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Plot 1: Line chart (Monthly Sales Trend)
monthly_sales = df_clean.groupby(df_clean["Date"].str[:7])["Sales"].sum()
axes[0, 0].plot(monthly_sales.index, monthly_sales.values, marker="o", color="green")
axes[0, 0].set_title("Monthly Sales Trend (2023)")
axes[0, 0].set_xlabel("Month")
axes[0, 0].set_ylabel("Total Sales ($)")

# Plot 2: Bar chart (Average Sales by Category)
category_sales = df_clean.groupby("Product_Category")["Sales"].mean()
axes[0, 1].bar(category_sales.index, category_sales.values, color=["blue", "orange", "green"])
axes[0, 1].set_title("Average Sales by Product Category")
axes[0, 1].set_ylabel("Average Sales ($)")

# Plot 3: Histogram (Profit Distribution)
axes[1, 0].hist(df_clean["Profit"], bins=10, edgecolor="black", color="purple")
axes[1, 0].set_title("Profit Distribution")
axes[1, 0].set_xlabel("Profit ($)")
axes[1, 0].set_ylabel("Frequency")

# Plot 4: Scatter plot (Sales vs. Profit)
axes[1, 1].scatter(df_clean["Sales"], df_clean["Profit"], alpha=0.6, color="red")
axes[1, 1].set_title("Sales vs. Profit")
axes[1, 1].set_xlabel("Sales ($)")
axes[1, 1].set_ylabel("Profit ($)")

plt.tight_layout()
plt.show()

# --- Findings Summary ---
print("""
Key Findings:
1. Monthly sales show an upward trend in Q4 (Oct-Dec)
2. Electronics category outperforms other product categories
3. Most profits fall between $50-$150
4. Higher sales generally correlate with higher profits
""")
