import cv2 as cv
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.HandTrackingModule import HandDetector
from cvzone.PoseModule import PoseDetector
FM = FaceMeshDetector()
HD = HandDetector()
FD = FaceDetector()
PD = PoseDetector()
cam = cv.VideoCapture(0)
if not cam.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cam.read()
    if not ret or frame is None:
        print("Failed to grab frame")
        break
    frame, faces = FD.findFaces(frame, draw=True)
    frame, Mfaces = FM.findFaceMesh(frame, draw=True)
    frame, hands = HD.findHands(frame)
    frame = PD.findPose(frame, draw=True)
    cv.imshow('webcam', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv.destroyAllWindows()