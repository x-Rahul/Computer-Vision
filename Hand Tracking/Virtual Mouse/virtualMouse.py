import cv2 as cv
import handTrackingModule as htm
import numpy as np

# Colors--
green = (0, 255, 0)
purple = (255, 0, 255)
blue = (255, 0, 0)
red =  (10, 10, 230)
orange = (15, 97, 212)
indigo = (130, 0, 75)
yello = (60, 210, 245)
cyan = (180, 180, 15)
white = (255, 255, 255)
black = (0,0,0)

detector = htm.handDetector()
cap = cv.VideoCapture(0)
while True:
    isTrue, img = cap.read()
    img = cv.flip(cv.resize(img, (1280, 720)), 1)
    detector.findHands(img, draw = False)
    lmList = detector.findPosition(img, False)
    if len(lmList) != 0:
        fingers = detector.fingersUp()
        print(fingers)
            
    cv.imshow("Output", img)
    if cv.waitKey(1) & 0xFF == ord('x'):
        break
cap.release()
cv.destroyAllWindows()