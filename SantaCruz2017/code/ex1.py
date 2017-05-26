import cv2

from sys import argv, exit

if len(argv) < 3:
    filename = 'friends.jpg'
else:
    filename = argv[3]

# Load image from a file
img = cv2.imread(filename)

# Show image in a window
cv2.imshow('Window Title', img)
# Wait for a key to be pressed (0 - forever)
cv2.waitKey(0)
# Destroy all created windows, releasing resources
cv2.destroyAllWindows()
