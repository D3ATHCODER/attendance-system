# attendance-system
This project implements an attendance management system using face recognition technology. The system provides an easy-to-use interface for registering students, taking attendance, and viewing attendance records.

## Features

- **Admin Login**: Admin can log in using the username `admin` and password `password`.
- **Register Student**: Capture and store student images for face recognition.
- **Take Attendance**: Mark attendance by recognizing registered students.
- **View Attendance**: Check attendance records for each student.

## File Structure
/attendance-system/ ├── admin_interface.py ├── attendance.csv ├── register_student.py ├── registered_students.csv ├── take_attendance.py ├── tkinter_interface.py ├── view_attendance.py └── face/ # Folder to store captured registered student images

## Technologies Used

- OpenCV
- Face Recognition
- Datetime
- OS
- CSV
- Tkinter

## Usage

1. Run the `tkinter_interface.py` file to launch the application.
2. Log in with the credentials:
   - **Username**: `admin`
   - **Password**: `password`
3. Choose one of the following options:
   - **Register Student**: Press the spacebar to capture the student's image. Once done, press `q` to finish the registration.
   - **Take Attendance**: Press the spacebar to mark attendance for recognized students. After completing the attendance, press `q` to exit.
   - **View Attendance**: Access and review the attendance records.

## Installation

To run this project, ensure you have the following libraries installed:

```bash
pip install opencv-python face_recognition datetime os csv tkinter
