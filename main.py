import cv2
import numpy as np


# foto
img = cv2.imread('images/2020-01-05_213603.jpg')
# cv2.imshow('Result', img)
# cv2.waitKey( )
print(img.shape)

# примеры
# задать размер
# new_img = cv2.resize(img, (720, 1280))
# уменьшить в два раза
# new_img = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2))
# cv2.imshow('Result', new_img)
# обрезка
# cv2.imshow('Result', img[50:250, 150:350])
# размытие
# img = cv2.GaussianBlur(img, (9,9), 0)


# работа с цветом
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# углы изображения(контуры)
img = cv2.Canny(img, 100,100)
# ширина контуров
kernel = np.ones( (5,5), np.uint8)
# увеличение обводки контуров
img = cv2.dilate(img, kernel, iterations=1)
# уменьшаем колличество точек
img = cv2.erode(img, kernel, iterations=1)

cv2.imshow('Result', img)



cv2.waitKey( )