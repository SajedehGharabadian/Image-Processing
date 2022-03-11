import numpy as np

import cv2

new_image = np.zeros((200,200),dtype=np.uint8)

height,width = new_image.shape

for i in range(height):
    for j in range(width):
        new_image[i,j] = 225 - i 


cv2.imshow('Draw',new_image)

cv2.waitKey()