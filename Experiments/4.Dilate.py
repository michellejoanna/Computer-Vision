import cv2
import matplotlib.pyplot as plt
import numpy as np

# Read image
image = cv2.imread("/Users/michellejoanna/Downloads/meee.jpeg")

# Convert to RGB
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Kernel
kernel = np.ones((5,5), np.uint8)

# Dilate image
dilated = cv2.dilate(rgb, kernel, iterations=1)

# Display
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(dilated)
plt.title("Dilated Image")
plt.axis("off")

plt.show()