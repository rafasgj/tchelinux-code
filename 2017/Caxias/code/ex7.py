import cv2
from time import sleep

camera = cv2.VideoCapture(0)

face_classifier = cv2.CascadeClassifier('data/facedet.model')

while True:
    retval, frame = camera.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray)

    # Draw face rectangles on the image
    for (x,y,w,h) in faces:
        color = (255,255,0)
        cv2.rectangle(frame, (x,y), (x+w,y+w), color, 2)

    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()

camera.release()

