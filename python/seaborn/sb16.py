import pandas as pd

df = pd.DataFrame({
    'city' : ['new york', 'london', 'paris', 'tokyo', 'new york', 'paris'],
    'price' : [200, 150, 300, 250, 180, 320 ]
})
print((df.groupby('city')['price'].mean()))
print((df.groupby('city')['price'].mean().to_dict()))