#!/usr/bin/env python2

from sys import argv, exit

import cv2

if len(argv) > 1:
    filename = argv[1]
else:
    filename = 'data/friends.jpg'

img = cv2.imread(filename)

cv2.imshow('Window Title',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
