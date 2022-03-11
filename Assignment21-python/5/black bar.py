import cv2
import numpy as np

image = np.ones((100, 100, 3), np.uint8) * 255
image = cv2.imread('mirzakhani.jpg',0)

print(image.shape)

for i in range(100):
    image[i:40+i,98-i] = 0

# for i in range(62):
#     image[i,60-i] = 0

for i in range(60):
    image[i:i+23,115-i] = 0
 

#image[0:20,95:115] = 0

pt1 = (139,0)
pt2 = (110,0)
pt3 = (80, 50)

cv2.circle(image, pt1, 2, (0,0,255), -1)
cv2.circle(image, pt2, 2, (0,0,255), -1)
cv2.circle(image, pt3, 2, (0,0,255), -1)


triangle_cnt = np.array( [pt1, pt2, pt3] )

cv2.drawContours(image, [triangle_cnt], 0, (0,0,0), -1)



cv2.imshow('Mirzakhani',image)

cv2.waitKey()