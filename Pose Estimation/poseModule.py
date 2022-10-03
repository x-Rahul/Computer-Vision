import cv2 as cv
import mediapipe as mp
import time


class poseDetector():

    def __init__(self, mode = False, upBody = False,modelComplexity= 1, smooth = True , detectionCon = 0.5, trackCon = 0.5): 
        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.modelComplexity = modelComplexity
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.upBody, self.modelComplexity, self.smooth, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findPose(self, img, draw = True):
        imgRGB = cv.cvtColor((img), cv.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                # for poselmrk in self.results.pose_landmarks:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        return img

    def findPosition(self, img, draw = True):
        self.lmList = []
        if self.results.pose_landmarks:
            myPose = self.results.pose_landmarks
            for id, lm in enumerate(myPose.landmark):
                # print(id,lm)
                h, w, c = img.shape 
                cx, cy = int(lm.x*w), int(lm.y*h)
                self.lmList.append([id, cx, cy])
                if draw:
                    cv.circle(img,(cx,cy), 5 , (0,0,150), cv.FILLED) 
        return self.lmList

    def findAngle(self, img, p1, p2, p3, draw = True):
        # print(f'{self.lmList[p1]}, {self.lmList[p2]}, {self.lmList[p3]}')

        x1, y1 = self.lmList[p1][1:]
        x2, y2 = self.lmList[p2][1:]
        x3, y3 = self.lmList[p3][1:]

        if draw:
            color = (255, 0, 0)
            cv.circle(img,(x1,y1), 5, color, cv.FILLED)
            cv.circle(img,(x1,y1), 12, color, 2)
            cv.circle(img,(x2,y2), 5, color, cv.FILLED)
            cv.circle(img,(x2,y2), 12, color, 2)
            cv.circle(img,(x3,y3), 5, color, cv.FILLED)
            cv.circle(img,(x3,y3), 12, color, 2)
        



#---------------------------------------------------------------------------------------------------------------

# # Dummy Code
# def main():
    
#     pTime = 0
#     cap = cv.VideoCapture(0)
#     detector = poseDetector()
#     while True:
#         isTrue, frame = cap.read()
#         img = cv.resize(frame, (640,480))

#         img = detector.findPose(img, draw = True)
#         lmList = detector.findPosition(img, draw = False)
#         detector.findAngle(img, 4, 6, 8)

#         # lmList[P] = [P x y], Access particular landmark Point
#         # where P is Pose landmark point and x,y are coordinates of the point of that particular image or frame

#         # if len(lmList) != 0:
#         #     cv.circle(img,(lmList[0][1],lmList[0][2]), 10 , (180,120,150), cv.FILLED) 
        
#         # FPS
#         cTime = time.time()
#         fps = 1/(cTime-pTime)
#         pTime = cTime
#         cv.putText(img, str(int(fps)), (5, 20), cv.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255), 1)

#         cv.imshow("webCam", img)
#         if cv.waitKey(1) & 0xFF == ord('x'):
#             break
        
#     cap.release()
#     cv.destroyAllWindows()

# if __name__ == "__main__":
#     main()