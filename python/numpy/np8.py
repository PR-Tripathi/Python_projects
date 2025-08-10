import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load image and convert to grayscale
image = Image.open('sample_image.jpg').convert('L')
image_array = np.array(image)

# Invert grayscale values (255 - pixel)
inverted_image_array = 255 - image_array

# Display original and inverted
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(image_array, cmap='gray')

plt.subplot(1, 2, 2)
plt.title("Inverted")
plt.imshow(inverted_image_array, cmap='gray')

plt.show()
