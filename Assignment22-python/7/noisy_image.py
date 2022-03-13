import random
import numpy as np
import cv2

image = cv2.imread('7/nature.jpg',0)

result = np.zeros(image.shape,np.uint8)

row,col = image.shape

threshold = 0.95
prob = 0.05

for i in range(row):
    for j in range(col):
        rand_num = random.random()

        if rand_num < prob:
                result[i][j] = 0
        elif rand_num > threshold:
            result[i][j] = 255
        else:
            result[i][j] = image[i][j]


cv2.imwrite('7/outout.jpg',result)

cv2.waitKey()
