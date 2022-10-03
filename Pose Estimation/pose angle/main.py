import cv2 as cv
import numpy as np
import time

import poseModule as pm

# path = "D:\Programming\Python\Resources\Videos\gym.mp4"
cap = cv.VideoCapture(0)
wCam, hCam = 640,480
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0
detector = pm.poseDetector()
while True:
    isTrue, img = cap.read()
    detector.findPose(img, draw=False)
    detector.findPosition(img, draw=False)
    
    detector.findAngle(img, 12, 14, 16)
    detector.findAngle(img, 11, 13, 15)
    cv.imshow("Output", img)
    if cv.waitKey(1) & 0xFF == ord('x'):
        break

cap.release()
cv.destroyAllWindows()