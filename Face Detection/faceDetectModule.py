import cv2 as cv
import mediapipe as mp
import time

class faceDetector():
    
    def __init__(self, minDetectionCon = 0.5, modelSelection = 1):
        
        # min_detection_confidence :--> Minimum confidence value ([0.0, 1.0]) for face detection to be considered successful.
        # model_selection :--> 0 or 1. 0 to select a short-range model that worksbest for faces within 2 meters from the camera,
        #                      and 1 for a full-range model best for faces within 5 meters.
    
        self.minDetectionCon = minDetectionCon
        self.modelSelection = modelSelection
        self.mpfaceDetection = mp.solutions.face_detection
        self.faceDetection = self.mpfaceDetection.FaceDetection(minDetectionCon, modelSelection)
        self.mpDraw = mp.solutions.drawing_utils
    
    def findFaces(self, img, draw = True):
        bBoxes = []
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.results = self.faceDetection.process(imgRGB)
        if self.results.detections:
            if draw:
                for id, detection in enumerate(self.results.detections):
                    bBoxC = detection.location_data.relative_bounding_box
                    ih, iw, ic = img.shape
                    bBox = int(bBoxC.xmin*iw), int(bBoxC.ymin*ih),\
                           int(bBoxC.width*iw), int(bBoxC.height*ih)
                    bBoxes.append([id, bBox, detection.score])
                    img = self.fancyDraw(img, bBox)
                    cv.rectangle(img, bBox, (255, 0, 255), 2)
                    cv.putText(img, f'{int(detection.score[0]*100)}% ', (bBox[0], bBox[1]-20),
                              cv.FONT_HERSHEY_PLAIN, 2, (255,0,255), 2)
            
        return img, bBoxes
    
    def fancyDraw(self, img, bBox, color = (50, 0, 255), l=30, t=5, rt= 1):
        x, y, w, h = bBox
        x1, y1 = x + w, y + h
        cv.rectangle(img, bBox, rt)
        # Top Left  x,y
        cv.line(img, (x, y), (x + l, y), color, t)
        cv.line(img, (x, y), (x, y+l), color, t)
        # Top Right  x1,y
        cv.line(img, (x1, y), (x1 - l, y), color, t)
        cv.line(img, (x1, y), (x1, y+l), color, t)
        # Bottom Left  x,y1
        cv.line(img, (x, y1), (x + l, y1), color, t)
        cv.line(img, (x, y1), (x, y1 - l), color, t)
        # Bottom Right  x1,y1
        cv.line(img, (x1, y1), (x1 - l, y1), color, t)
        cv.line(img, (x1, y1), (x1, y1 - l), color, t)
        return img

#-----------------------------------------------------------------------------------------------
# Dummy code :

# def main():
      
#     path = 'D:\Programming\Python_Tutorials\Resources\Videos\dance4.mp4'
#     cap = cv.VideoCapture(path)
#     detector = faceDetector()
#     pTime = 0
#     while True:
#         isTrue, frame = cap.read()
#         img = cv.resize(frame, (1280,720))
      
#         #--
#         img, bBoxes = detector.findFaces(img)

#         cTime = time.time()
#         fps = 1/(cTime - pTime)
#         pTime = cTime
#         cv.putText(img, f"FPS : {int(fps)}", (30,50), cv.FONT_HERSHEY_PLAIN, 2, (0,255,0), 2)
#         #--
       
#         cv.imshow("Output", img)
#         if cv.waitKey(1) & 0xFF == ord('x'):
#             break
           
#     cap.release()
#     cv.destroyAllWindows()

# if __name__ == "__main__":
#     main()