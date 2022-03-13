
import cv2

img1 = cv2.imread('1/a.tif',0)

row1 , col1 = img1.shape

for i in range(row1):
    for j in range(col1):
        if img1[i,j] == 255:
            img1[i,j] = 0

        elif img1[i,j] == 0:
            img1[i,j] = 255

img2 = cv2.imread('1/b.tif',0)

row2 , col2 = img2.shape

for i in range(row2):
    for j in range(col2):
        if img2[i,j] == 255:
            img2[i,j] = 0

        elif img2[i,j] == 0:
            img2[i,j] = 255

result = cv2.subtract(img1,img2)

row,col = result.shape

for i in range(row):
    for j in range(col):
        if result[i,j] == 255:
            result[i,j] = 0

        elif result[i,j] == 0:
            result[i,j] = 255


cv2.imwrite('1/outout.jpg',result)

cv2.waitKey()
