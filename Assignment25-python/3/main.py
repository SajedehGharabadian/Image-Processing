import cv2 
import numpy as np

img = cv2.imread('3/building.tif')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

result_mask1 = np.zeros((img.shape))
result_mask2 = np.zeros((img.shape))

mask1 =  np.array([[-1,0,1],
                   [-1,0,1],
                   [-1,0,1]])

mask2 =  np.array([[-1,-1,-1],
                   [0,0,0],
                   [1,1,1]])
            
rows,cols = img.shape

for i in range(1,rows-1):
    for j in range(1,cols-1):
        small_img_mask1 = img[i-1:i+2,j-1:j+2]
        result_mask1[i,j] = np.sum(small_img_mask1 * mask1)

cv2.imwrite('3/result_mask1.jpg',result_mask1)

for i in range(1,rows-1):
    for j in range(1,cols-1):
        small_img_mask2 = img[i-1:i+2,j-1:j+2]
        result_mask2[i,j] = np.sum(small_img_mask2 * mask2)

cv2.imwrite('3/result_mask2.jpg',result_mask2)



