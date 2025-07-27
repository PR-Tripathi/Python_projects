import numpy as np

data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

#Data greater than 5
p1= data>5
print(p1)

#retrieving data greater than 5
p2 = data[data>5]
print(p2)

#finding data between two fixed value
p3 = data[(data>5) & (data<9)]
print(p3)