import cv2
import numpy as np

img = np.zeros((300, 300), dtype='uint8')

circle = cv2.circle(img.copy(), (0, 0), 80, 255, -1)
square = cv2.rectangle(img.copy(), (25, 25), (250, 350), 255, -1)

# Побитовые операции и маски
img = cv2.bitwise_and(circle,square)
img = cv2.bitwise_or(circle,square)
img = cv2.bitwise_xor(circle,square)
img = cv2.bitwise_not(circle)

cv2.imshow("Result", img)
cv2.waitKey(0)
