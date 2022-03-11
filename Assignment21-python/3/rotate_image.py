import numpy as np
import cv2

image = cv2.imread('sad.jpg',0)


height , width = image.shape

new_image = np.zeros((height,width),dtype=np.uint8)

for i in range(height):
    for j in range(width):
        new_image[i,j] = image[height-i-1,j]
        new_image = new_image[0:height,0:width]

img = cv2.resize(new_image,(366,550))

cv2.imshow('Rotate',img)

cv2.waitKey()