🎓 Smart Attendance System (Face Recognition)
📌 Problem

Manual attendance takes time, can be inaccurate, and students can sign in for others.

💡 Solution

A face recognition attendance system that automatically detects and records attendance when a student appears in front of a camera.

⚙️ Technologies / Tools

Python

OpenCV – face detection

NumPy – data processing

Pandas – exporting attendance

Face Recognition – identify students

Webcam / laptop camera

Optional:

SQLite for storing records

Flask for a dashboard

🧠 How It Works
1️⃣ Register Students

Capture student images.

Store their face encodings in a database.

2️⃣ Detect Faces

Camera turns on.

System detects faces in real time.

3️⃣ Recognize Faces

The system compares the detected face with stored faces.

4️⃣ Mark Attendance

If a match is found:

Name

Date

Time
are automatically recorded.

5️⃣ Export Data

Attendance is saved as:

CSV

Excel spreadsheet

✨ Main Features

✔ Face detection from camera
✔ Automatic attendance marking
✔ Duplicate attendance prevention
✔ Timestamp recording
✔ Export to spreadsheet
✔ Admin dashboard (optional)
