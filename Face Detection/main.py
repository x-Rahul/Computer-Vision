import cv2 as cv
import time
import faceDetectModule as fd

detector = fd.faceDetector()
cap = cv.VideoCapture(0)

pTime = 0
while True:
    isTrue, frame = cap.read()
    img = cv.resize(frame, (1280,720))

    #--
    img, bBoxes = detector.findFaces(img)
    #--

    cv.imshow("Output", img)
    if cv.waitKey(1) & 0xFF == ord('x'):
        break

cap.release()
cv.destroyAllWindows()