import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

video_capture = cv2.VideoCapture(0)

# Load Known Faces
akash_image = face_recognition.load_image_file("faces/akash.jpg")
# Encoder image ko number me convert kar deta to easy comaprison
akash_encoding = face_recognition.face_encodings(akash_image)[0]
ayush_image = face_recognition.load_image_file("faces/ayush.jpg")
ayush_encoding = face_recognition.face_encodings(ayush_image)[0]
amit_image = face_recognition.load_image_file("faces/amit.jpg")
amit_encoding = face_recognition.face_encodings(amit_image)[0]

known_face_encodings = [akash_encoding,ayush_encoding,amit_encoding]
known_face_names = ["Akash","Ayush","Amit"]

#list of expected students
students = known_face_names.copy()
face_locations = []
face_encodings = []

# Get the current Date And Time
now = datetime.now()
current_date = now.strftime("%d-%m-%Y")

#csv file(current date ko write kar rahe h)
f = open(f"{current_date}.csv", "w+", newline="")
lnwriter = csv.writer(f)

while True:
    _, frame = video_capture.read() #--> pahla argument  _ hota h ki aapka video capture successful tha ki nahi or dusra frame ke liye
    small_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame,cv2.COLOR_BGR2RGB)

    # Recognize faces...
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encodings in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encodings)
        face_distance = face_recognition.face_distance(known_face_encodings, face_encodings)
        best_match_index = np.argmin(face_distance)

        if(matches[best_match_index]):
            name = known_face_names[best_match_index]

            # ADD THE TEXT IF PERSON IS PRESENT
            if name in known_face_names:
                font = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText = (10,100)
                fontScale = 1.5
                fontColor = (255,0,0)
                thickness = 3
                lineType = 2
                cv2.putText(frame, name + " Present ",bottomLeftCornerOfText,font,fontScale,fontColor,thickness,lineType)

                if name in students:
                    students.remove(name)
                    current_time = now.strftime("%H-%M%S")
                    lnwriter.writerow([name, current_time])


        cv2.imshow("Attendance", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

            video_capture.release()
            cv2.destroyAllWindows()
            f.close()

