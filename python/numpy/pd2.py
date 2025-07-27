import pandas as pd

data ={'a':1, 'b':2, 'c':3,}
series_dict = pd.Series(data)
print(series_dict)

print("\n")
data2 ={
    'Name':['Jonathan','Ricky','Jack'],
    'Age':[25,30,45],
    'City':['Edenburgh','Florida','New York']
}
df=pd.DataFrame(data2)
print(df)
print(type(df))