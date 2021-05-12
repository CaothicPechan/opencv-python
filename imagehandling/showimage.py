import cv2 as cv
import sys

from cv2 import IMREAD_GRAYSCALE

fullpath_flower = "../mysamples/flower2.jpg"
img = cv.imread(cv.samples.findFile(fullpath_flower),IMREAD_GRAYSCALE )
if img is None:
    sys.exit("Could not read the image.")
cv.imshow("Display window", img)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("mysavedimage.jpg", img)