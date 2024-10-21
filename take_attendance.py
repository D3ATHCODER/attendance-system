import cv2
import face_recognition
import os
import csv
import datetime

def mark_attendance(name):
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    if not os.path.exists("attendance.csv"):
        with open("attendance.csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Date", "Time", "Status"])

    already_marked = False
    with open("attendance.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == name and row[1] == date:
                already_marked = True
                break

    if not already_marked:
        with open("attendance.csv", 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, date, time, "Present"])
        print(f"Attendance marked for {name} on {date} at {time}")
    else:
        print(f"Attendance already marked for {name} today.")

def take_attendance():
    face_folder = "faces"
    known_faces = []
    known_names = []

    for filename in os.listdir(face_folder):
        if filename.endswith(".png"):
            img_path = os.path.join(face_folder, filename)
            img = face_recognition.load_image_file(img_path)
            encoding = face_recognition.face_encodings(img)[0]
            known_faces.append(encoding)
            name = filename.split("_")[0]
            known_names.append(name)

    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Attendance")

    while True:
        ret, frame = cam.read()
        if not ret:
            print("Failed to grab frame.")
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)

        if face_locations:
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

            for face_encoding, face_location in zip(face_encodings, face_locations):
                matches = face_recognition.compare_faces(known_faces, face_encoding)
                name = "Unknown"

                if True in matches:
                    match_index = matches.index(True)
                    name = known_names[match_index]
                    mark_attendance(name)

                top, right, bottom, left = face_location
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            print("No faces detected.")

        cv2.imshow("Attendance", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()