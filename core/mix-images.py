import cv2 as cv

fullpath_flower = "../mysamples/flower2.jpg"
img = cv.imread(cv.samples.findFile(fullpath_flower))

sky = img[0:400, 0:400]
someflowers1 = img[2000:2400, 2300:2700]
someflowers2 = img[1300:1700, 1600:2000]

dst = cv.addWeighted(sky,0.7,someflowers1,0.3,0)
cv.imshow('dst',dst)
cv.imshow('someflowers 1',someflowers1)
cv.imshow('sky',sky)
# cv.imshow('someflowers 2',someflowers2)
cv.waitKey(150000)
cv.destroyAllWindows()
exit(0)