import cv2

img = cv2.imread('data/friends.jpg')

cv2.imshow("Titulo", img)

cv2.waitKey(0)

cv2.destroyAllWindows()
