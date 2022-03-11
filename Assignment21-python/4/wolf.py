
from turtle import width
import cv2 


wolf = cv2.imread('wolf.jpg',0)
new_wolf = cv2.resize(wolf,(480,768))

height , width = new_wolf.shape
print(new_wolf.shape)
threshold = 120

for i in range(height):
    for j in range(width):
        if new_wolf[i,j] < threshold:
            new_wolf[i,j] = 0

    


cv2.imshow('Leaves',new_wolf)

cv2.waitKey()