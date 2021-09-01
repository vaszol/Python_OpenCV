import cv2
import numpy as np

photo = cv2.imread("images/2020-01-05_213603.jpg")
img = np.zeros(photo.shape[:2], dtype='uint8')

circle = cv2.circle(img.copy(), (250, 200), 200, 255, -1)
square = cv2.rectangle(img.copy(), (25, 25), (250, 350), 255, -1)

# Побитовые операции и маски
img = cv2.bitwise_and(photo, photo, mask=circle)
# img = cv2.bitwise_or(circle, square)
# img = cv2.bitwise_xor(circle, square)
# img = cv2.bitwise_not(circle)

cv2.imshow("Result", img)
cv2.waitKey(0)
