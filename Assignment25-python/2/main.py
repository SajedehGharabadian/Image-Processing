import numpy as np
import cv2

img = cv2.imread('2/lion.png')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

result = np.zeros((img.shape))

mask = np.array([[0,-1,0],
                 [-1,4,-1],
                 [0,-1,0]])

rows,cols = img.shape

for i in range(1,rows-1):
    for j in range(1,cols-1):
        small_img = img[i-1:i+2,j-1:j+2]
        result[i,j] = np.sum(small_img * mask)

cv2.imwrite('2/result.jpg',result)
