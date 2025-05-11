# --- Import Libraries ---
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# --- Error Handling & Data Loading ---
try:
    # Load Iris dataset from sklearn and convert to DataFrame
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target_names[iris.target]
    
    # Save to CSV for the "load from file" requirement
    df.to_csv("iris.csv", index=False)
    
    # Load from CSV (simulating real-world file handling)
    df = pd.read_csv("iris.csv")
    
    print("✅ Dataset loaded successfully!")
    print("--------------------------------")

except FileNotFoundError:
    print("❌ Error: 'iris.csv' not found")
except Exception as e:
    print(f"❌ Unexpected error: {str(e)}")

# --- Task 1: Explore & Clean Data ---
print("\nFirst 5 rows:")
print(df.head())

print("\nData structure:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

# Simulate missing values for cleaning demonstration
df.iloc[10:12, 1] = None
df_clean = df.dropna()
print(f"\nCleaned data shape: {df_clean.shape} (Original: {df.shape})")

# --- Task 2: Data Analysis ---
print("\nBasic statistics:")
print(df_clean.describe())

print("\nMean sepal length by species:")
print(df_clean.groupby('species')['sepal length (cm)'].mean())

# --- Task 3: Visualizations ---
plt.figure(figsize=(15, 10))
sns.set_style("darkgrid")

# Line Chart (Petal Length Trends by Index)
plt.subplot(2, 2, 1)
plt.plot(df_clean['petal length (cm)'], color='purple')
plt.title("Petal Length Variation Across Samples")
plt.xlabel("Sample Index")
plt.ylabel("Petal Length (cm)")

# Bar Chart (Mean Measurements by Species)
plt.subplot(2, 2, 2)
df_clean.groupby('species').mean().plot(kind='bar', ax=plt.gca())
plt.title("Average Measurements by Species")
plt.xticks(rotation=45)

# Histogram (Sepal Width Distribution)
plt.subplot(2, 2, 3)
sns.histplot(df_clean['sepal width (cm)'], bins=15, kde=True, color='green')
plt.title("Sepal Width Distribution")

# Scatter Plot (Sepal Length vs Petal Length)
plt.subplot(2, 2, 4)
sns.scatterplot(data=df_clean, 
                x='sepal length (cm)', 
                y='petal length (cm)', 
                hue='species',
                palette='viridis')
plt.title("Sepal vs Petal Length Relationship")

plt.tight_layout()
plt.show()

# --- Findings ---
print("""
Key Observations:
1. Setosa species has significantly smaller petal measurements
2. Sepal width shows normal distribution around 3.0 cm
3. Strong positive correlation between sepal/petal lengths
4. Versicolor and Virginica overlap in some measurements
""")
