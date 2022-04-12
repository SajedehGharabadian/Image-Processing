import cv2
import numpy as np

video_cap = cv2.VideoCapture(0)
lower = np.array([0, 48, 80], dtype = "uint8")
upper = np.array([20, 255, 255], dtype = "uint8")

while True:
    ret,frame = video_cap.read()

    frame_rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    frame_hsv = cv2.cvtColor(frame_rgb,cv2.COLOR_RGB2HSV)
    
    Mask = cv2.inRange(frame_hsv, lower, upper)

    skinMask = cv2.GaussianBlur(Mask, (3, 3), 0)
    
    skin = cv2.bitwise_and(frame, frame, mask = skinMask)



    
    if ret == False:
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


    cv2.imshow('frame',skin)
    cv2.waitKey(1)