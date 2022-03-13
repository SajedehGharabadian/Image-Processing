
import cv2

origin = cv2.imread('3/board - origin.bmp',0)
test = cv2.imread('3/board - test.bmp',0)

test = cv2.flip(test,1)

result = cv2.absdiff(origin,test)

cv2.imwrite('3/output.jpg',result)

cv2.waitKey()
