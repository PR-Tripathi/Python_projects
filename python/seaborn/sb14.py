from sklearn.preprocessing import LabelEncoder
import pandas as pd
Lbl_encoder = LabelEncoder()

df= pd.DataFrame({
    'color' : ['red','blue','green','green','red','blue']
})
print(Lbl_encoder.fit_transform(df[['color']]) )
