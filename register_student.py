import cv2
import os
import csv

def register_student(name, roll_number):
    # Save student details to registered_students.csv
    with open('registered_students.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, roll_number])
    
    # Capture the student's face using OpenCV
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Capture Face")
    
    face_folder = "faces"
    
    if not os.path.exists(face_folder):
        os.makedirs(face_folder)
    
    while True:
        ret, frame = cam.read()
        if not ret:
            break
        cv2.imshow("Capture Face", frame)

        k = cv2.waitKey(1)
        if k % 256 == 32:  # Press space to capture face
            img_name = f"{face_folder}/{name}_{roll_number}.png"
            cv2.imwrite(img_name, frame)
            break
    
    cam.release()
    cv2.destroyAllWindows()
    print(f"Student {name} registered successfully.")