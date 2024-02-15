import face_recognition
import cv2
import numpy as np
import csv
import os
# import  glob
import time
from datetime import datetime

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Loading all the images from the database

#1 Himanshu
himanshu_image = face_recognition.load_image_file("faces/himanshu.jpeg")
himanshu_face_encoding = face_recognition.face_encodings(himanshu_image)[0]

#2 Manu
manu_image = face_recognition.load_image_file("faces/manu.jpeg")
manu_face_encoding = face_recognition.face_encodings(manu_image)[0]


#3 chhari 
chhari_image = face_recognition.load_image_file("faces/chhari.jpeg")
chhari_face_encoding = face_recognition.face_encodings(chhari_image)[0]

#4 jitendra
jitendra_image = face_recognition.load_image_file("faces/jitendra.jpeg")
jitendra_face_encoding = face_recognition.face_encodings(jitendra_image)[0]

#5 hrishi
hrishi_image = face_recognition.load_image_file("faces/hrishi.jpeg")
hrishi_face_encoding = face_recognition.face_encodings(hrishi_image)[0]

# write down a list of known face encodings and their names
known_face_encoding = [
    himanshu_face_encoding,
    manu_face_encoding,
    chhari_face_encoding,
    jitendra_face_encoding,
    hrishi_face_encoding
]

# write down a list of known face names 
known_face_names = [
    "Himanshu",
    "Manu",
    "Chhari",
    "Jitendra",
    "Hrishi"
]





# copy the names in students variable
students = known_face_names.copy()

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
s = True

now = datetime.now()
current_date = now.strftime("%d-%m-%Y")
filename = "attendance" + current_date + ".csv"
print(filename)
file = open(filename, "w+" , newline='')
lnwriter = csv.writer(file)

while True:
    _ , frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25) # resize the frame to 1/4 size for faster face recognition processing
    rgb_small_frame = small_frame[:, :, ::-1] # convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    if s:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(
            rgb_small_frame, face_locations
        )
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(
                known_face_encoding, face_encoding
            )
            name = ""
            face_distances = face_recognition.face_distance(
                known_face_encoding, face_encoding
            )
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            face_names.append(name)
            if name in known_face_names:
                if name in students:
                    print(name + " marked as present")
                    students.remove(name)
                    current_time = now.strftime("%H:%M:%S")
                    lnwriter.writerow([name, current_time])
    cv2.imshow("Attendence Management System", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
video_capture.release()
cv2.destroyAllWindows()
file.close()