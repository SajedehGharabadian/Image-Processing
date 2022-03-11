import numpy as np

import cv2

image = np.zeros((400,400),dtype=np.uint8)

image[100:120,160:230] = 255

image[120:140,230:250] = 255

image[120:180,140:160] = 255

image[180:200,160:230] = 255

image[200:260,230:250] = 255

image[260:280,160:230] = 255

image[240:260,140:160] = 255

cv2.imshow('Leaves',image)

cv2.waitKey()