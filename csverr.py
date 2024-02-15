import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime
import tkinter as tk
from threading import Thread

video_capture = cv2.VideoCapture(0)

# Loading all the images from the database

# # 1 Himanshu
# himanshu_image = face_recognition.load_image_file("faces/himanshu.jpeg")
# himanshu_face_encoding = face_recognition.face_encodings(himanshu_image)[0]

# # 2 Manu
# manu_image = face_recognition.load_image_file("faces/manu.jpeg")
# manu_face_encoding = face_recognition.face_encodings(manu_image)[0]

# # 3 Chhari
# chhari_image = face_recognition.load_image_file("faces/chhari.jpeg")
# chhari_face_encoding = face_recognition.face_encodings(chhari_image)[0]

# 4 Jitendra
jitendra_image = face_recognition.load_image_file("faces/jitendra.jpeg")
jitendra_face_encoding = face_recognition.face_encodings(jitendra_image)[0]

# 5 Hrishi
# hrishi_image = face_recognition.load_image_file("faces/hrishi.jpeg")
# hrishi_face_encoding = face_recognition.face_encodings(hrishi_image)[0]

# # 6 Hariom
# hariom_image = face_recognition.load_image_file("faces/hariom.jpeg")
# hariom_face_encoding = face_recognition.face_encodings(hariom_image)[0]

# write down a list of known face encodings and their names
known_face_encoding = [
    # himanshu_face_encoding,
    # manu_face_encoding,
    # chhari_face_encoding,
    jitendra_face_encoding,
    # hrishi_face_encoding,
    # hariom_face_encoding
]

# write down a list of known face names
known_face_names = [
    # "Himanshu",
    # "Manu",
    # "Chhari",
    "Jitendra"
    # "Hrishi",
    # "Hariom"
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
filename = "attendance_" + current_date + ".csv"
print(filename)
file = open(filename, "w+", newline='')
lnwriter = csv.writer(file)

# Tkinter UI
root = tk.Tk()
root.title("Attendance Management System")

# Frame to hold student boxes
students_frame = tk.Frame(root)
students_frame.pack(pady=10)

student_boxes = {}

status_label = tk.Label(root, text="", font=("Helvetica", 12))
status_label.pack(pady=10)

attendance_list = tk.Listbox(root, font=("Helvetica", 12))
attendance_list.pack(pady=10)

percentage_label = tk.Label(root, text="", font=("Helvetica", 12))
percentage_label.pack(pady=10)

# Dictionary to store attendance time for each student
attendance_time = {name: None for name in known_face_names}

# Function to calculate percentage of students present
def calculate_percentage():
    total_students = len(known_face_names)
    present_students = total_students - len(students)
    return (present_students / total_students) * 100 if total_students > 0 else 0

# Function to update CSV file with logout time
# Function to update CSV file with logout time
def update_csv_logout(name, logout_time):
    if name in known_face_names and attendance_time[name] is not None:
        login_time = attendance_time[name].strftime("%H:%M:%S")
        lnwriter.writerow([name, login_time, logout_time])






# Function to update UI with percentage of students present
def update_ui_percentage():
    percentage = calculate_percentage()
    percentage_label.config(text=f"Percentage of students present: {percentage:.2f}%")

# Function to update UI
def update_ui(name):
    if name:
        status_label.config(text=f"{name} marked as present")
        attendance_list.insert(tk.END, name)

        if name in student_boxes:
            student_boxes[name].config(bg="green")
        
        update_ui_percentage()

# Modify video_capture_loop function
def video_capture_loop():
    global s
    while True:
        _, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]

        key = cv2.waitKey(1)
        if key & 0xFF == ord("q"):
            break
        elif key & 0xFF == ord("l"):
            for name in face_names:
                logout(name)

        if s:
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            face_names = []

            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                matches = face_recognition.compare_faces(known_face_encoding, face_encoding)
                name = "Unknown"
                face_distances = face_recognition.face_distance(known_face_encoding, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                face_names.append(name)

                if name in known_face_names:
                    if name in students:
                        print(name + " marked as present")
                        students.remove(name)
                        current_time = datetime.now()
                        lnwriter.writerow([name, current_time.strftime("%H:%M:%S")])
                        attendance_time[name] = current_time
                        update_ui(name)

                        # Display the name on the camera feed
                        font = cv2.FONT_HERSHEY_SIMPLEX
                        bottom_left_corner = (left, bottom)
                        font_scale = 1.5
                        font_color = (255, 0, 0)
                        thickness = 3
                        line_type = 2
                        cv2.putText(frame, name + " Present", bottom_left_corner, font, font_scale, font_color,
                                    thickness, line_type)

            # Create/update student boxes
            for student_name in known_face_names:
                if student_name not in student_boxes:
                    box = tk.Label(students_frame, text=student_name, bg="lightgray", padx=10, pady=5,
                                   font=("Helvetica", 12))
                    box.pack(side=tk.LEFT, padx=5)
                    student_boxes[student_name] = box

        cv2.imshow("Attendance Management System", frame)

    video_capture.release()
    cv2.destroyAllWindows()
    file.close()

# Function to handle log out
# Function to handle log out
# Function to handle log out
# Function to handle log out
def logout(name):
    if name in known_face_names:
        if attendance_time[name] is not None:
            time_diff = (datetime.now() - attendance_time[name]).total_seconds()
            if time_diff >= 120:  # 2 minutes
                attendance_list.delete(0, tk.END)
                logout_time = datetime.now().strftime("%H:%M:%S")
                update_csv_logout(name, logout_time)
                attendance_time[name] = None
                status_label.config(text=f"{name} logged out")
                if name in students:
                    students.append(name)
                if name in student_boxes:
                    student_boxes[name].config(bg="lightgray")
                update_ui_percentage()




# Start video capture loop in a separate thread
video_thread = Thread(target=video_capture_loop)
video_thread.start()

# Tkinter main loop
root.mainloop()
