import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

flights = sns.load_dataset("flights")
sns.lineplot(data=flights, x="year", y="passengers", ci=None)
plt.title("Passengers Over Time")
plt.show()
