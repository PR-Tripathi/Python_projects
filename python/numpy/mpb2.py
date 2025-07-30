import matplotlib.pyplot as plt

categories = ['A','B','C','D','E']
values = [5,7,3,8,6]

##Create Bar Plot
plt.bar(categories,values, color='magenta')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('BAR PLOT')

#Histogram
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
plt.hist(data,bins=5,color='orange', edgecolor='black' )

plt.show()

#Create a Scatter plot
x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 5, 6]
plt.scatter(x,y, color='blue', marker='x')
plt.show()

###Pipe Charts

labels =['A', 'B', 'C', 'D']
sizes =[30,20,40,10]
colors = ['gold','yellowgreen', 'lightcoral', 'lightskyblue']
explode=(0.2,0,0,0)
#create a pie chart

plt.pie(sizes,explode=explode,labels=labels,colors=colors, autopct="%1.1f%%",shadow=True)
plt.show()