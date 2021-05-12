import numpy as np
import cv2 as cv
fountain = "/home/mike/IdeaProjects/influencer/opencv-demo/mysamples/fountain2.mp4"
cap = cv.VideoCapture(fountain)
while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        cap = cv.VideoCapture(fountain)
        ret, frame = cap.read()
        # break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()