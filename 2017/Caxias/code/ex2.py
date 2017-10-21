import cv2

img = cv2.imread('data/friends.jpg')

cv2.imshow("Titulo", img)
cv2.waitKey(0)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray Scale", gray)
cv2.waitKey(0)

classificador = cv2.CascadeClassifier("data/facedet.model")
faces = classificador.detectMultiScale(gray)

for (x,y,h,w) in faces:
    cv2.rectangle(gray,(x,y),(x+w,y+h), 255, 2)

cv2.imshow("Gray Scale", gray)
cv2.waitKey(0)

cv2.destroyAllWindows()
