import numpy as np
import pandas as pd

# Set the random seed for reproducibility
np.random.seed(123)

# Create a dataframe with classes
n_samples = 1000
class_0_ratio = 0.9

n_class_0 = int(n_samples * class_0_ratio)
n_class_1 = n_samples - n_class_0

print(n_class_1, n_class_0)

# Creating DataFrame with imbalanced dataset
class_0 = pd.DataFrame({
    'feature_1': np.random.normal(loc=0, scale=1, size=n_class_0),
    'feature_2': np.random.normal(loc=0, scale=1, size=n_class_0),  # Fixed
    'target': [0]*n_class_0
})

class_1 = pd.DataFrame({
    'feature_1': np.random.normal(loc=2, scale=1, size=n_class_1),
    'feature_2': np.random.normal(loc=2, scale=1, size=n_class_1),
    'target': [1]*n_class_1
})

# Combine the data and reset index
df = pd.concat([class_0, class_1]).reset_index(drop=True)
print(df)
