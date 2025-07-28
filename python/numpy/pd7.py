import pandas as pd

df=pd.read_csv('data.csv')
df['Value_new'] = df['Value'].fillna(df['Value'].mean()).astype(int)
df1=df.head()
df['New Value']=df['Value'].apply(lambda x:x*2)
df2=df.head()
print(df,"\n")
print(df1)
print("\n",df2)
