from importlib.resources import path
import cv2 as cv
import mediapipe as mp
import numpy as np
import time
import os
import handTrackingModule as htm


folderPath = 'D:\Programming\Python\Resources\Images\FingerCount'
myList = os.listdir(folderPath)
# print(myList)

imgList = []
for imPath in myList:
    image = cv.imread(f'{folderPath}\{imPath}')
    imgList.append(image)

green = (0, 255, 0)
purple = (255, 0, 255)
blue = (255, 0, 0)
red =  (23, 23, 156)
orange = (15, 97, 212) 

detector = htm.handDetector(detectionCon = 0.75)
tipIds = [4, 8, 12, 16, 20]


cap = cv.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

pTime = 0
while True:
    isTrue, img = cap.read()
    #---
    
    img = detector.findHands(img, draw=False)
    landmarkList = detector.findPosition(img, draw = False)
    if len(landmarkList) != 0:
        # print(landmarkList[8])  
        totalFingers = detector.fingersUp()
        # print(fingers)
        totalFingers = totalFingers.count(1)
        # print(totalFingers)
        if totalFingers != 0:
            h, w, c = imgList[totalFingers-1].shape
            img[0:h, 0:w] = imgList[totalFingers-1]
            
    # FPS
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv.putText(img, f'FPS : {int(fps)}',(490, 30), cv.FONT_HERSHEY_PLAIN, 2, green, 2)

    #---
    cv.imshow("Output", img)
    if cv.waitKey(1) & 0xFF == ord('x'):
        break
cap.release()
cv.destroyAllWindows()