
import cv2

image_1 = cv2.imread('girl.jpg',0)
image_2 = cv2.imread('boy.jpg',0)

img_girl = 255 - image_1[:,:]
img_boy = 255 - image_2[:,:]

cv2.imshow('Leaves',img_girl)
cv2.imshow('Leaves',img_boy)

cv2.waitKey()