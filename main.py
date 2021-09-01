import cv2
import numpy as np


img = cv2.imread('images/faces_foto.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

focus = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

results = focus.detectMultiScale(gray, scaleFactor=2, minNeighbors=3)

for (x,y,w,h) in results:
    cv2.rectangle(img,(x,y,),(x+w,y+h),(0,0,255),thickness=3)

cv2.imshow("Result", img)
cv2.waitKey(0)
