#!/usr/bin/env python2

from sys import argv, exit
from random import random

import cv2

if len(argv) > 1:
    filename = argv[1]
else:
    filename = 'data/friends.jpg'

img = cv2.imread(filename)
cv2.imshow('Window Title',img)
cv2.waitKey(0)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# processamento
cv2.imshow('Window Title',gray)
cv2.waitKey(0)

img = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
#
for r in range(5):
    x0 = int(random()*300) + 100
    y0 = int(random()*300) + 100
    x1 = int(random()*300) + 100
    y1 = int(random()*300) + 100
    r = int(random()*255) + 50
    g = int(random()*255) + 50
    b = int(random()*255) + 50
    cv2.rectangle(img, (x0,y0), (x1,y1), (b,g,r), 3)
#
cv2.imshow('Window Title',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
