import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

lst_marks = [45,32,56,75,89,54,32,89,90,87,67,54,45,98,99,67,74]
##Minimum, Maximum, Median, Q1, Q3, Maximum
minimum,Q1,meadian,Q3,maximum=np.quantile(lst_marks,[0,0.25,0.50,0.75,1.0])
print(minimum, meadian, Q1,Q3,maximum)
IQR= Q3-Q1
print(IQR)
sns.boxplot(lst_marks)
plt.show()