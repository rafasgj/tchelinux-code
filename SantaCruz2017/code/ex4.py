import cv2

from sys import argv, exit
from random import random

if len(argv) < 3:
    filename = 'friends.jpg'
else:
    filename = argv[3]

# Load image from a file
img = cv2.imread(filename)

# Show image in a window
cv2.imshow('Display', img)
# Wait for a key to be pressed (0 - forever)
cv2.waitKey(0)

# convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# update image shown, as there's always only one image
cv2.imshow('Display', gray)
# Wait for a key to be pressed (0 - forever)
cv2.waitKey(0)

face_classifier = cv2.CascadeClassifier('facedet.model')
faces = face_classifier.detectMultiScale(gray)

print len(faces)

# convert image back to color
img = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
# Draw face rectangles on the image
for (x,y,w,h) in faces:
    color = (255,255,0)
    cv2.rectangle(img, (x,y), (x+w,y+w), color, 2)

# update image shown, as there's always only one image
cv2.imshow('Display', img)

# Wait for a key to be pressed (0 - forever)
cv2.waitKey(0)
# Destroy all created windows, releasing resources
cv2.destroyAllWindows()
