# Facial-recognition-based-attendance-system-

This project is a **Face Recognition-based Attendance System** built using Python, Django, and **AWS Rekognition**. The system allows users to check in and check out by recognizing their faces, tracking attendance, and storing data efficiently.

## Features

- **Face Recognition**: The system uses AWS Rekognition for identifying and verifying users based on facial features.
- **Check-in/Check-out System**: Employees or students can check in and check out, and their attendance is recorded.
- **Real-time Processing**: Real-time face recognition for attendance tracking.
- **AWS Integration**: Utilizes AWS Rekognition for face analysis and verification.
- **Django Web Interface**: A Django-based web application for managing users and viewing attendance data.
- **Database Storage**: Attendance records are stored in a database (e.g., PostgreSQL, SQLite).
- **Secure Authentication**: Users authenticate via a web interface for face recognition or log-in.

## Technologies Used

- **Django**: For the backend web framework.
- **Python**: Programming language for logic and backend services.
- **AWS Rekognition**: To process and verify faces from images or video streams.
- **AWS S3**: For storing images or videos used in face recognition.
- **PostgreSQL/SQLite**: For storing attendance data and user details.
- **HTML/CSS/JavaScript**: Frontend for the web interface.

## Requirements

Before running the project, make sure you have the following installed:

- Python 3.7+
- Django 3.x+
- AWS Account with Rekognition and S3 access
- `boto3` (AWS SDK for Python) installed
- `django-storages` for integrating S3 storage in Django
- `opencv-python` for handling image capture

 Install the required Python packages:

