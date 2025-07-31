import seaborn as sns
import matplotlib.pyplot as plt

###Basic Plotting with Seaborn
tips=sns.load_dataset('tips')

sns.scatterplot(x='total_bill',y='tip',data=tips ,)
plt.title("Scatter Plot Of Total Bill Vs Tip")

#2
sns.lineplot(x='size',y='total_bill', data=tips)
plt.title("Line Plot of Total Bill by Size")

#3
sns.barplot(x='day',y='total_bill',data=tips)
plt.title('BAR PLOT OF TOTAL BILL BY DAY')

4
sns.boxplot(x='day',y='total_bill', data= tips)

#5. Violin Plot
sns.violinplot(x='day', y='total_bill', data= tips)

#6 histograms 
sns.histplot(tips['total_bill'],bins=10,kde=True)

#7 KDE plot
sns.kdeplot(tips['total_bill'],fill=True)

#8 Pairplot
sns.pairplot(tips)

#9Heatmap
corr=tips[['total_bill','tip','size']].corr()
sns.heatmap(corr,annot=True,cmap='coolwarm')



plt.show()

