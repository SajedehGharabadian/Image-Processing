import numpy as np
import cv2

images = []

for i in range(15):
    image = cv2.imread(f"4/highway/h{i}.jpg",0)

    images.append(image)

    row,col = image.shape

results = np.zeros((row,col),dtype=np.uint8)

for image in images:
    results += image//15

cv2.imwrite('4/output.jpg',results)

cv2.waitKey()
