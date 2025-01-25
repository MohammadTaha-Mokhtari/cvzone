import cv2 as cv
from cvzone.FaceMeshModule import FaceMeshDetector
FM = FaceMeshDetector()
cam = cv.VideoCapture(0)
if not cam.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cam.read()
    if not ret or frame is None:
        print("Failed to grab frame")
        break
    frame, Mfaces = FM.findFaceMesh(frame, draw=True)
    cv.imshow('webcam', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv.destroyAllWindows()