import cv2

# Read the image from Downloads folder
image = cv2.imread("/Users/michellejoanna/Downloads/meee.jpeg")

# Check if the image was loaded successfully
if image is None:
    print("Image not found!")
    exit()

# Enlarge the image (2x)
bigger = cv2.resize(
    image,
    None,
    fx=2,
    fy=2,
    interpolation=cv2.INTER_LINEAR
)

# Shrink the image (0.5x)
smaller = cv2.resize(
    image,
    None,
    fx=0.5,
    fy=0.5,
    interpolation=cv2.INTER_AREA
)

# Display the images
cv2.imshow("Original Image", image)
cv2.imshow("Bigger Image", bigger)
cv2.imshow("Smaller Image", smaller)

# Wait until a key is pressed
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()