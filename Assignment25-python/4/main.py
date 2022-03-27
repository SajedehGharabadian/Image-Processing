import numpy as np
import cv2

img = cv2.imread('4/g1.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


def average_filter(img,n):
    
    result = np.zeros((img.shape))

    mask = np.ones((n,n)) / n**2

    rows,cols = img.shape

    for i in range((n//2),rows - (n//2)):
        for j in range((n//2), cols - (n//2)):
            small_img = img[i-(n//2):i+((n//2)+1),j-(n//2):j+((n//2)+1)]
            result[i,j] = np.sum(small_img * mask)

    cv2.imwrite('4/result'+str(n)+'.jpg',result)

    cv2.waitKey()

average_filter(img,3)
average_filter(img,5)
average_filter(img,7)
average_filter(img,15)