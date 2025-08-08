import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the 'tips' dataset
tips = sns.load_dataset("tips")

# Create a FacetGrid grouped by sex (columns) and smoker (rows)
g = sns.FacetGrid(tips, col="sex", row="smoker", margin_titles=True)

# Map a histogram with KDE to each facet
g.map_dataframe(sns.histplot, x="total_bill", kde=True)

# Adjust spacing and add a title
g.fig.subplots_adjust(top=0.9)
g.fig.suptitle("FacetGrid of Total Bill Distribution")

# Show plot
plt.show()
