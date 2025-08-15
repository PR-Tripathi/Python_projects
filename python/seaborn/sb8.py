import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd
df = sns.load_dataset('titanic')

# Before imputation: Age distribution
sns.displot(df['age'],kde=True)
# plt.title('Age Distribution Before Imputation')

# plt.title('Age Distribution after Imputation')
df['Age_mean']=df['age'].fillna(df['age'].mean())
print(df[['Age_mean','age']])

df['Age_median']=df['age'].fillna(df['age'].median())
print("\n",df[['Age_median','age']])

##3. mode imputation techninque
print("\n",df[df['embarked'].isnull()])

# Print unique values in the 'embarked' column
print("\n", df['embarked'].unique())

# Correct way to get mode while excluding NaN values
mode_value = df[df['embarked'].notna()]['embarked'].mode()[0]
df['embarked_mode']=df['embarked'].fillna(mode_value)
print("\n",df[['embarked_mode','embarked']])
