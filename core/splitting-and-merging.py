import numpy as np
import cv2 as cv
flower2 = "../mysamples/flower2.jpg"
img = cv.imread(flower2)

b,g,r = cv.split(img)
img = cv.merge((b,g,r))
b = img[:,:,0]
print("blue " + str(b))
img[:,:,2] = 0

cv.imshow("red removed", img)

cv.waitKey(15000)
cv.destroyAllWindows()
exit(0)