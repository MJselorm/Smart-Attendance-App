import cv2
import os

# Ask for student name
name = input("Enter student name: ")

# Create folder if it doesn't exist
dataset_path = "dataset"
if not os.path.exists(dataset_path):
    os.makedirs(dataset_path)

# Face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Start camera
cap = cv2.VideoCapture(0)

count = 0

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        count += 1

        face = gray[y:y+h, x:x+w]

        file_name = f"{dataset_path}/{name}_{count}.jpg"
        cv2.imwrite(file_name, face)

        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow("Capturing Faces", frame)

    # stop after 20 images
    if count >= 20:
    
        break
    key= cv2.waitKey(1) & 0xFF
    if key==ord('q') or key==ord('Q') or key==27:
        break

cap.release()
cv2.destroyAllWindows()

print("Face capture completed")