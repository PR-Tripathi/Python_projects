import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the built-in 'tips' dataset
tips = sns.load_dataset("tips")

# Plot the histogram
sns.histplot(data=tips, x="total_bill", kde=True, bins=20)
plt.title("Distribution of Total Bill")
plt.show()
