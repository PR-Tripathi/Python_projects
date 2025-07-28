##Data Manipulation with Data Frames
import pandas as pd
data2 ={
    'Name':['Jonathan','Ricky','Jack'],
    'Age':[25,30,45],
    'City':['Edenburgh','Florida','New York']
}
data2['Salary']=[50000,65000,150000]
df =pd.DataFrame(data2)
print(df) 
print("\n")

#Remove a column
df2=df.drop('Salary',axis=1)
print(df2)

