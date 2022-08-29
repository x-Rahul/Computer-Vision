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
drawColor = white

detector = htm.handDetector()
cap = cv.VideoCapture(0)
while True:
    isTrue, img = cap.read()
    img = cv.flip(cv.resize(img, (1280, 720)), 1)
    detector.findHands(img, draw = False)
    lmList = detector.findPosition(img, False)
    if len(lmList) != 0:
        x1,y1 = lmList[8][1:]
        x2,y2 = lmList[12][1:]
        fingers = detector.fingersUp()
        # print(fingers)
        thumb, index, middle, ring, pinky = fingers[0:5]

        # Selection Mode
        if index and middle and thumb == 0 and pinky == 0 and ring == 0:
            print("selection mode")
            xp, yp = 0, 0
            cv.circle(img, ((x1+x2)//2, (y1+y2)//2), 30, drawColor, 3)
            
    cv.imshow("Output", img)
    if cv.waitKey(1) & 0xFF == ord('x'):
        break
cap.release()
cv.destroyAllWindows()