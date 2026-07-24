import cv2
import numpy as np

# Read the image from Downloads folder
image = cv2.imread("/Users/michellejoanna/Downloads/meee.jpeg")

# Check if the image is loaded successfully
if image is None:
    print("Image not found!")
    exit()

# Get image dimensions
rows, cols = image.shape[:2]

# Translation values
tx = 100   # Move 100 pixels to the right
ty = 50    # Move 50 pixels downward

# Translation Matrix
M = np.float32([
    [1, 0, tx],
    [0, 1, ty]
])

# Apply Translation
translated = cv2.warpAffine(image, M, (cols, rows))

# Display Images
cv2.imshow("Original Image", image)
cv2.imshow("Translated Image", translated)

# Wait until a key is pressed
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()