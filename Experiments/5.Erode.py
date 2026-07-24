import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("/Users/michellejoanna/Downloads/meee.jpeg")

rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

kernel = np.ones((5,5), np.uint8)

eroded = cv2.erode(rgb, kernel, iterations=1)

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(eroded)
plt.title("Eroded Image")
plt.axis("off")

plt.show()