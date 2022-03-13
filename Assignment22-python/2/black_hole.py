

import numpy as np
import cv2

image1 = []
image2 = []
image3 = []
image4 = []

for i in range(1,6):
    image = cv2.imread(f"2/1/{i}.jpg",0)

    image1.append(image)
    row,col = image.shape

result1 = np.zeros((row,col),dtype=np.uint8)
for image in image1:
    result1 += image//5

for i in range(1,6):
    image = cv2.imread(f"2/2/{i}.jpg",0)

    image2.append(image)
    row,col = image.shape

result2 = np.zeros((row,col),dtype=np.uint8)
for image in image2:
    result2 += image//5

for i in range(1,6):
    image = cv2.imread(f"2/3/{i}.jpg",0)

    image3.append(image)
    row,col = image.shape

result3 = np.zeros((row,col),dtype=np.uint8)
for image in image3:
    result3 += image//5

for i in range(1,6):
    image = cv2.imread(f"2/4/{i}.jpg",0)

    image4.append(image)
    row,col = image.shape

result4 = np.zeros((row,col),dtype=np.uint8)
for image in image4:
    result4 += image//5

cv2.imwrite('2/output1.jpg',result1)

cv2.imwrite('2/output2.jpg',result2)

cv2.imwrite('2/output3.jpg',result3)

cv2.imwrite('2/output4.jpg',result4)

final_image = np.zeros((2000,2000),dtype=np.uint8)

final_image[0:1000,0:1000] = result1
final_image[0:1000,1000:2000] = result2
final_image[1000:2000,0:1000] = result3
final_image[1000:2000,1000:2000] = result4

cv2.imwrite('2/finally.jpg',final_image)

cv2.waitKey()
