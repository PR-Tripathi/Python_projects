###Ordinal Encoding
import pandas as pd 
from sklearn.preprocessing import OrdinalEncoder
df= pd.DataFrame({
    'size' : ['small','medium','large','medium','small','large']
})
encoder = OrdinalEncoder(categories=[['small','medium','large']])

print(encoder.fit_transform(df[['size']]))