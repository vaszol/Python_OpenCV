import cv2
import numpy as np

photo = np.zeros((450, 450, 3), dtype='uint8')

# RGB - стандарт
# BGR - формат в OpenCV
# photo[100:150, 200:280] = 119, 201, 105

cv2.rectangle(photo, (50, 50), (100, 100), (119, 201, 105), thickness=3)

cv2.line(photo, (0, photo.shape[0] // 2), (photo.shape[1], photo.shape[0] // 2), (119, 201, 105), thickness=3)

cv2.circle(photo, (photo.shape[1] // 2, photo.shape[0] // 2), 50, (119, 201, 105), thickness=cv2.FILLED)

cv2.putText(photo, 'vaszol', (100, 150), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 0), thickness=2)

cv2.imshow('Photo', photo)
cv2.waitKey(0)
