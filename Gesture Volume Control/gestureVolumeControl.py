import cv2 as cv
import mediapipe as mp
import numpy as np
import handTrackingModule as htm
import time 
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()
# print(volRange)
minVol = volRange[0]
maxVol = volRange[1]


green = (0, 255, 0)
purple = (255, 0, 255)
blue = (255, 0, 0)
red =  (23, 23, 156)
orange = (15, 97, 212)


detector = htm.handDetector(detectionCon=0.5)
cap = cv.VideoCapture(0)
wCam, hCam = 640, 480
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

while True:

    isTrue, img = cap.read()
    
    #--
    img = detector.findHands(img, draw = False)
    lmList = detector.findPosition(img, draw = False)
    if len(lmList) != 0:
        # print(lmList[4], lmList[8])
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1+x2)//2, (y1+y2)//2
        
        # Draw points
        # cv.circle(img, (x1, y1), 10, orange, cv.FILLED)
        # cv.circle(img, (x2, y2), 10, orange, cv.FILLED)
        # cv.circle(img, (cx, cy), 10, purple, cv.FILLED)
        # cv.line(img, (x1, y1), (x2, y2), purple, 2)
        
        length = math.hypot(x2-x1, y2-y1)
        # if length < 50:
        #     cv.circle(img, (cx, cy), 10, red, cv.FILLED)
        
        # Hand Range = 20 - 200
        # Volume Range = -65 - 0
        vol = np.interp(length, (20, 200), (minVol, maxVol)) 
        # print(int(length), vol)
        volume.SetMasterVolumeLevel(vol, None)
        
        # Draw Volume Meter
        volBar = np.interp(length, (20, 200), (400, 150))
        volPer = np.interp(length, (20, 200), (0, 100))
        cv.rectangle(img, (50, int(volBar)), (75, 400), green, cv.FILLED)
        cv.rectangle(img, (50, 150), (75, 400), green, 2)
        cv.putText(img, f'{int(volPer)}%', (40, 430), cv.FONT_HERSHEY_PLAIN, 2, blue, 2 )
          
    #FPS
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv.putText(img, f'FPS : {int(fps)}', (30, 40), cv.FONT_HERSHEY_PLAIN, 2, green, 2 )
    #--
    
    cv.imshow("Output", img)
    if cv.waitKey(1) & 0xFF == ord('x'):
        break
        
cap.release()
cv.destroyAllWindows()