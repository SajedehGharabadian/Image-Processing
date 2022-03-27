import numpy as np
import cv2

img = cv2.imread('1/flower_input.jpg')

img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

result1 = np.zeros((img.shape))
result2 = np.zeros((img.shape))

mask = np.ones((35,35)) / 1225


rows,cols = img.shape

for i in range(17,rows - 17):
    for j in range(17, cols - 17):
        
        small_img = img[i-17:i+18,j-17:j+18]
        result1[i,j] = np.sum(small_img * mask)


for i in range(17,rows-17):
    for j in range(17,cols-17):
        if img[i,j] > 200:
            small_img = img[i-17:i+18,j-17:j+18]
            small_img_1d = small_img.reshape(1225)
            small_img_1d_sort = np.sort(small_img_1d)

            result2[i,j] = small_img_1d_sort[612]


result = result1 + result2
       
cv2.imwrite('1/result.jpg',result)

cv2.waitKey()