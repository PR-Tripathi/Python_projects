## DATA AGGRREGATING AND GROUPING
import pandas as pd

df=pd.read_csv('data.csv')

#Mean Of Data
grouped_mean = df.groupby('Product')['Value'].mean()
print(grouped_mean,"\n ")

#Sum of data
grouped_sum = df.groupby(['Product', 'Region'])['Value'].sum()
print("\n",grouped_sum)

##Aggregate Data
grouped_aggt = df.groupby('Region')['Value'].agg(['mean','sum','count'])
print("\n",grouped_aggt)
