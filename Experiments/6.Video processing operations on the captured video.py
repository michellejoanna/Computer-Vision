import cv2

video = cv2.VideoCapture("/Users/michellejoanna/Downloads/WhatsApp Video 2026-07-24 at 01.41.14.mp4")

if not video.isOpened():
    print("Error: Cannot open video.")
    exit()

print("1 - Fast Motion")
print("2 - Slow Motion")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    delay = 5
    window = "Fast Motion Video"
elif choice == "2":
    delay = 100
    window = "Slow Motion Video"
else:
    print("Invalid choice!")
    video.release()
    exit()

while True:
    ret, frame = video.read()

    if not ret:
        break

    cv2.imshow(window, frame)

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()