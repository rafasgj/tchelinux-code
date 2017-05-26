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

# convert image back to color
img = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
# Draw random rectangles on the image
for r in range(5):
    color = (int(random()*200)+50,int(random()*200)+50,int(random()*200)+50)
    x0 = int(random()*300) + 100
    y0 = int(random()*300) + 100
    x1 = int(random()*300) + 100
    y1 = int(random()*300) + 100
    print (color)
    cv2.rectangle(img, (x0,y0), (x1,y1), color, 2)
# update image shown, as there's always only one image
cv2.imshow('Display', img)

# Wait for a key to be pressed (0 - forever)
cv2.waitKey(0)
# Destroy all created windows, releasing resources
cv2.destroyAllWindows()
