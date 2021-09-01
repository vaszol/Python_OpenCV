import cv2
import numpy as np

img = cv2.imread('images/2020-01-05_213603.jpg')

# цветовые форматы
# img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
img = cv2.cvtColor(img, cv2.COLOR_LAB2BGR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# разделение по цветовым слоям и обединение слоев
r, g, b = cv2.split(img)
# cv2.imshow("Result", r)
img = cv2.merge([b, g, r])

cv2.imshow("Result", img)
cv2.waitKey(0)
