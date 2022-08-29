import cv2 as cv
import mediapipe as mp
import time

import handTrackingModule as htm

# Dummy Code
pTime = 0
cTime = 0
cap = cv.VideoCapture(0)
detector = htm.handDetector()
while True:
    isTrue, frame = cap.read()
    img = cv.resize(frame, (640,480))

    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw = False)

    #FPS
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv.putText(img, str(int(fps)), (5, 20), cv.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255), 1)

    cv.imshow("webCam", img)
    if cv.waitKey(1) & 0xFF == ord('x'):
        break
    
cap.release()
cv.destroyAllWindows()