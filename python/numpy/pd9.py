import pandas as pd

# Create Sample DataFrames
df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'Value1': [1, 2, 3]})
df2 = pd.DataFrame({'key': ['A', 'B', 'D'], 'Value2': [4, 5, 6]})  

print("\n", df1)
print('\n', df2)

# Merge DataFrame on the 'key' column
df3 = pd.merge(df1, df2, on="key", how="inner")
print("\n", df3)
