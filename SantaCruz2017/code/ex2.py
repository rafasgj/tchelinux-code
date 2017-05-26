import cv2

from sys import argv, exit

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
# Destroy all created windows, releasing resources
cv2.destroyAllWindows()
