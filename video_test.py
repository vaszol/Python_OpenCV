import cv2

# cap = cv2.VideoCapture(0) # захват с камеры
cap = cv2.VideoCapture('videos/VID-20210803-WA0004.mp4')
while True:
    success, img = cap.read()
    cv2.imshow('Result', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break