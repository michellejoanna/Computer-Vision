import cv2

# Load the video
video = cv2.VideoCapture("/Users/michellejoanna/Downloads/WhatsApp Video 2026-07-24 at 01.41.14.mp4")

if not video.isOpened():
    print("Cannot open video")
    exit()

print("========== Video Speed ==========")
print("1. Normal Speed")
print("2. Fast Motion")
print("3. Slow Motion")

choice = input("Enter your choice (1/2/3): ")

if choice == "1":
    delay = 30
    title = "Normal Speed Video"
elif choice == "2":
    delay = 5
    title = "Fast Motion Video"
elif choice == "3":
    delay = 100
    title = "Slow Motion Video"
else:
    print("Invalid Choice!")
    video.release()
    exit()

while True:
    ret, frame = video.read()

    if not ret:
        break

    cv2.imshow(title, frame)

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()