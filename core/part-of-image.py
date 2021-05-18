import numpy as np
import cv2 as cv
flower2 = "../mysamples/flower2.jpg"
# flower2 = "/home/mmni/projects/opencv-python/mysamples/flower2.jpg"
img = cv.imread(flower2)

someflowers = img[2000:2200, 2300:2500]

# someflowers = img[200:400, 600:800]
img[100:300, 200:400] = someflowers

cv.imshow("flowers", img)
cv.imshow("flowers some", someflowers)
cv.waitKey(150000)

cv.destroyAllWindows()
exit(0)