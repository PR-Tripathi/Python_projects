import pandas as pd

df=pd.read_csv('data.csv')
##fetch The First 5 rows
first5=df.head(5)
print(first5)
##Tail
tail=df.tail(5)
print("\n",tail)