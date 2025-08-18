from imblearn.over_sampling import SMOTE
from sklearn.datasets import make_classification
import pandas as pd
import matplotlib.pyplot as plt

x,y =make_classification(n_samples=1000,n_redundant=0,n_features=2, n_clusters_per_class=1, weights=[0.90],random_state=12)

df_1= pd.DataFrame(x,columns=['f1','f2'])
df_2 = pd.DataFrame(y,columns=['target'])
final_df = pd.concat([df_1,df_2],axis=1)
print(final_df.head())
print(final_df['target'].value_counts())

plt.scatter(final_df['f1'],final_df['f2'],c=final_df['target'])

oversample= SMOTE()
X = final_df[['f1', 'f2']]
y = final_df['target']
x,y = oversample.fit_resample(final_df[['f1','f2']],final_df['target'])
print(x.shape,y.shape)

df1= pd.DataFrame(x,columns=['f1','f2'])
df2= pd.DataFrame(y,columns=['target'])
oversample_df= pd.concat([df1,df2],axis=1)
plt.scatter(oversample_df['f1'],oversample_df['f2'],c=oversample_df['target'])
plt.show()