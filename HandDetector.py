import cv2 as cv
from cvzone.HandTrackingModule import HandDetector
HD = HandDetector()
cam = cv.VideoCapture(0)
if not cam.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cam.read()
    if not ret or frame is None:
        print("Failed to grab frame")
        break
    frame, hands = HD.findHands(frame, draw=True)
    cv.imshow('webcam', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv.destroyAllWindows()