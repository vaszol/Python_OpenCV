import cv2
import numpy as np

photo = np.zeros((450, 450, 3), dtype='uint8')

# RGB - стандарт
# BGR - формат в OpenCV
# photo[100:150, 200:280] = 119, 201, 105

cv2.rectangle(photo, (0, 0), (100, 100), (119, 201, 105), thickness=3)

cv2.imshow('Photo', photo)
cv2.waitKey(0)
