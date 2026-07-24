import cv2
import matplotlib.pyplot as plt

image = cv2.imread("/Users/michellejoanna/Downloads/meee.jpeg")

rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Apply Gaussian Blur
blur = cv2.GaussianBlur(rgb, (15,15), 0)

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(blur)
plt.title("Gaussian Blur")
plt.axis("off")

plt.show()