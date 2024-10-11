import cv2
import numpy as np
import face_recognition as fr
from datetime import datetime, timedelta
import os

image_folder = './pictures/'
known_face = []
known_face_name = []

image_files = [f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]

for image_file in image_files:
    image_path = os.path.join(image_folder, image_file)
    image = fr.load_image_file(image_path)
    face_encodings = fr.face_encodings(image)
    if face_encodings:
        known_face.append(face_encodings[0])
        person_name = os.path.splitext(image_file)[0]
        person_name = person_name.split(' ')[0]
        known_face_name.append(person_name)

print("Known faces:")
for name in known_face_name:
    print(name)

vid_cap=cv2.VideoCapture(0)

end_time = datetime.now() + timedelta(seconds=5)
name="Unknown"
while True:
    if datetime.now() > end_time:
        break
    ret,frame=vid_cap.read()
    rgb_frame=frame[:,:,::-1]
    fc_location=fr.face_locations(rgb_frame)
    fc_encode=fr.face_encodings(rgb_frame,fc_location)
    for (top,right,bottom,left), face_encoding in zip(fc_location,fc_encode):
        matches=fr.compare_faces(known_face,face_encoding)
        name="Unknown"
        fc_distances=fr.face_distance(known_face,face_encoding)
        match_index=np.argmin(fc_distances)
        if matches[match_index]:
            name=known_face_name[match_index]
        cv2.rectangle(frame,(left,top),(right,bottom),(0,0,255),2)
        cv2.rectangle(frame,(left,bottom-35),(right,bottom),(0,0,255),cv2.FILLED)
        font=cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame,name,(left+6,bottom-6),font,1.0,(255,255,255),1)
    cv2.imshow('Face Recognition System',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
vid_cap.release()
cv2.destroyAllWindows()
