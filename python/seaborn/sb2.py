import seaborn as sns
import matplotlib.pyplot as plt

# Load another dataset
iris = sns.load_dataset("iris")

sns.pairplot(iris, hue="species")
plt.suptitle("Pairplot of Iris Dataset", y=1.02)
plt.show()
