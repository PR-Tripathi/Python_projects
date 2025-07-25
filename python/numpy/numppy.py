import numpy as np

##1d array
# arr1=np.array([1,2,3,4,5])
# print(arr1)
# print(type(arr1))

##2d array
# arr2=np.array([[1,2,3,4,5],[2,3,4,5,6]])
# print(arr2)
# print(arr2.shape)

##array arange
# hell1=np.arange(0,10,2).reshape(5,1)
# print(hell1)

#ones
# n1 = np.ones((3, 4))
# print(n1)

arr = np.array([[1, 2, 3],[4, 5, 6]])

print("Array:\n",arr)
print("Shape:",arr.shape)
print("Number of dimension:",arr.ndim)
print("Size(number of elements):",arr.size)
print("Data type :",arr.dtype)
print("Item size (in bytes):",arr.itemsize)
