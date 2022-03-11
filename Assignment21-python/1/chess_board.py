import numpy as np
import cv2

list_num = np.zeros((800,800))

cnt_row = 0
cnt_col = 0

for row in range(0,800,100):
    if cnt_row % 2 == 0:
        for col in range(0,800,100):
            if cnt_col %  2 == 0:
                for i in range(row,row+100):
                    for j in range(col,col+100):
                        list_num[i,j] = 255

                cnt_col += 1

            else:
                for i in range(row,row+100):
                    for j in range(col,col+100):
                        list_num[i,j] = 0
                cnt_col += 1

        cnt_row += 1

    else:
        for col in range(0,800,100):
            if cnt_col %  2 == 0:
                for i in range(row,row+100):
                    for j in range(col,col+100):
                        list_num[i,j] = 0

                cnt_col += 1

            else:
                for i in range(row,row+100):
                    for j in range(col,col+100):
                        list_num[i,j] = 255

                cnt_col += 1
        cnt_row += 1
  
cv2.imshow('Chess Board',list_num)

cv2.waitKey()