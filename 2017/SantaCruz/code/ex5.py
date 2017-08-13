import cv2
from time import sleep

camera = cv2.VideoCapture(0)

sleep(5)

retval, frame = camera.read()

del(camera)

cv2.imshow("Frame", frame)
cv2.waitKey(0)
cv2.destroyWindows()
