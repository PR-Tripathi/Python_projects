import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_excel('flight_price.xlsx')
print(df.head(), '\n')
print(df['Price'].unique(), "\n")

# Create a copy to work on
df_copy = df.copy()

# Clean only the 'Price' column
chars_to_remove = ['+', ',', '$']
col_to_clean = 'Price'

# Convert to string to safely use .str.replace
df_copy[col_to_clean] = df_copy[col_to_clean].astype(str)

# Remove unwanted characters
for char in chars_to_remove:
    df_copy[col_to_clean] = df_copy[col_to_clean].str.replace(char, '', regex=False)

# Convert cleaned Price to numeric
df_copy[col_to_clean] = pd.to_numeric(df_copy[col_to_clean], errors='coerce')

# Check cleaned unique values
print("\nCleaned Price values:\n", df_copy['Price'].unique())

avg_price_by_airline = df_copy.groupby('Airline')['Price'].mean().sort_values(ascending=False)
print(avg_price_by_airline)

# Optional barplot
plt.figure(figsize=(12, 6))
sns.barplot(x=avg_price_by_airline.index, y=avg_price_by_airline.values)
plt.xticks(rotation=45)
plt.title('Average Flight Price by Airline')
plt.ylabel('Average Price')
plt.xlabel('Airline')
plt.show()
