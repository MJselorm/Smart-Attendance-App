import cv2
import os
import numpy as np

dataset_path = "dataset"

faces = []
labels = []

label_map = {}
current_label = 0

for file in os.listdir(dataset_path):

    path = os.path.join(dataset_path, file)

    name = file.split("_")[0]

    if name not in label_map:
        label_map[name] = current_label
        current_label += 1

    label = label_map[name]

    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    faces.append(image)
    labels.append(label)

recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.train(faces, np.array(labels))

recognizer.save("face_model.yml")

print("Model trained successfully")
print(label_map)