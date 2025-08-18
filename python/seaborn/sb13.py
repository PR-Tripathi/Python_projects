#### DATA ENCODING ####
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

##Create Data frame 
df= pd.DataFrame({
    'color' : ['red','blue','green','green','red','blue']
})

print(df.head())

#create an instance of onehotencoder

encoder= OneHotEncoder()

##perfom fit and transform 
encoded = encoder.fit_transform(df[['color']]).toarray()

encode_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out())

print('\n',encoded,'\n\t\n',encode_df)