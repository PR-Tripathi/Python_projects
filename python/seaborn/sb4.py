import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
tips = sns.load_dataset("tips")

# Set Seaborn style
sns.set_style("whitegrid")

# First histogram (without hue)
#sns.histplot(data=tips, x="total_bill", kde=True, bins=20, color="skyblue")

# Second histogram (with hue)
sns.histplot(data=tips, x="total_bill", hue="sex", kde=True, bins=20)

# Show plot
plt.show()
