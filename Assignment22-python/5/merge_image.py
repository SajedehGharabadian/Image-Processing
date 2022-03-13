import numpy as np
import cv2

images = []
concat_images = results = np.zeros((480,1920),dtype=np.uint8)

img1 = cv2.imread('5/girl.jpg',0)

img2 = cv2.imread('5/Tiger.jpg',0)

print(img1.shape)
new_img2 = cv2.resize(img2,(480,480))

row,col = img1.shape
print(img2.shape)

new_img2 = cv2.resize(img2,(480,480))

result1 = img1//8 + new_img2//5

result2 = img1//5 + new_img2//8

result = img1//10 + new_img2//10


concat_images[0:480,0:480] = img1
concat_images[:,480:960] = result2
concat_images[:,960:1440] = result1
concat_images[:,1440:1960] = new_img2


cv2.imwrite('5/output1.jpg',result1)
cv2.imwrite('5/output2.jpg',result2)

cv2.imwrite('5/output.jpg',result)

cv2.imwrite('5/final.jpg',concat_images)



cv2.waitKey()
