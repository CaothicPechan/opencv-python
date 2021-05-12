import numpy as np
import cv2 as cv
flower2 = "../mysamples/flower2.jpg"
img = cv.imread(flower2)
px = img[100,100]
print( px )

# accessing only blue pixel
blue = img[100,100,0]
print( blue )

img[100,100] = [255,255,255]
print( img[100,100] )
for x in range(100,140):
    for y in range(100,140):
        img[x,y] = [255,255,255]

# Better way to access and change pixels due to numpy
# accessing RED value
print(img.item(10,10,2))

# modifying RED value
img.itemset((10,10,2),100)
print(img.item(10,10,2))


cv.imshow("pixel changed", img)
cv.waitKey(15000)

cv.destroyAllWindows()
exit(0)


