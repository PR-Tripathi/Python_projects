import seaborn as sns

df= sns.load_dataset('titanic')

print(df.head())

print("\n",df.isnull().sum())

##Delete The Rows or data point to handle missing value
print("\n",df.shape)
print("\n",df.dropna().shape)

##Column wise deletion
print("\n",df.dropna(axis=1))


