import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [1, 4, 9, 16, 25]

# ## 1. First plot (optional)
# plt.plot(x, y)
# plt.xlabel('X Axis')
# plt.ylabel('Y Axis')
# plt.title("Basic Line Plot")

##2. Customized plot
# plt.plot(x, y, color='red', linestyle='--', marker='o')
# plt.grid(True)
# plt.show()

##3. Multiple Plots
## Sample Data
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 =[1, 2, 3, 4, 5]

plt.figure(figsize=(9,5))

plt.subplot(2,2,1)
plt.plot(x,y1,color='green')
plt.title('Plot 1')

plt.subplot(2,2,2)
plt.plot(y1,x,color='blue')
plt.title("Plot 2")

plt.subplot(2,2,3)
plt.plot(x,y2,color='red')
plt.title('Plot 3')

plt.subplot(2,2,4)
plt.plot(x,y2,color='orange')
plt.title('Plot 4')

plt.show()

