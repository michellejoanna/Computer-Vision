import cv2

# Read the image from Downloads folder
image = cv2.imread("/Users/michellejoanna/Downloads/meee.jpeg")

# Check if the image is loaded successfully
if image is None:
    print("Image not found!")
    exit()

# Rotate 90° Clockwise
clockwise = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

# Rotate 90° Counter Clockwise
counter_clockwise = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

# Display Images
cv2.imshow("Original Image", image)
cv2.imshow("90° Clockwise Rotation", clockwise)
cv2.imshow("90° Counter Clockwise Rotation", counter_clockwise)

# Wait until a key is pressed
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()