import pandas as pd

data =[
   { 'Name':'Jonathan','Age':25,'city':'Banglore'},
   { 'Name':'Jonny','Age':26,'city':'pondicherry'},
   { 'Name':'mack','Age':27,'city':'netherland'},
   { 'Name':'Jacky','Age':28,'city':'austria'},
   { 'Name':'bingo','Age':29,'city':'wales'},
   { 'Name':'luka','Age':22,'city':'London'},
   { 'Name':'hidden','Age':35,'city':'Florida'},
   { 'Name':'samsti','Age':45,'city':'NYC'}
   ]

df = pd.DataFrame(data)
print(df)
print(type(df))