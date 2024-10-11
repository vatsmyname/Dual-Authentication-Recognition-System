import cv2
# for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


screen_width = 1280       
screen_height = 720

stream = cv2.VideoCapture(0)

while(True):
    (grabbed, frame) = stream.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    faces = face_cascade.detectMultiScale(rgb, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        color = (0, 255, 255) 
        stroke = 5
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, stroke)

    cv2.imshow("Image", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):    
        break              

stream.release()
cv2.waitKey(1)
cv2.destroyAllWindows()
cv2.waitKey(1)