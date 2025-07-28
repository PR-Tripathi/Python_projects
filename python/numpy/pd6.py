import pandas as pd

df=pd.read_csv('data.csv')
#Handling Missing Values
nul=df.isnull()
# print(nul)

##filling missing values with the mean of the column
nul=df['Sales_fillNA']=df['Sales'].fillna(df['Sales'].mean())
print(nul)