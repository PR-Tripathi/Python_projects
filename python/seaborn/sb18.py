import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df =  pd.read_excel('flight_price.xlsx')
print(df.columns,'\n')
# import pandas as pd
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

df_copy[col_to_clean] = df_copy[col_to_clean].astype(str)


for char in chars_to_remove:
    df_copy[col_to_clean] = df_copy[col_to_clean].str.replace(char, '', regex=False)

df_copy[col_to_clean] = pd.to_numeric(df_copy[col_to_clean], errors='coerce')

print("\nCleaned Price values:\n", df_copy['Price'].unique())
