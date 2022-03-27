
import numpy as np
import cv2


video_cap = cv2.VideoCapture(0)
width= int(video_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height= int(video_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


output = cv2.VideoWriter("5/cam_video.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 20.0,(width,height))

while True:
    ret,frame = video_cap.read()
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    filter = np.ones((35,35),np.float32) / 35**2
    
    rect = frame[250:350,200:300]


    blur_frame = cv2.filter2D(frame,-1,filter)

    blur_frame[250:350,200:300] = rect

    color_detect = blur_frame[250:350,200:300] 

    if 0 < np.average(color_detect) <= 80:
        cv2.putText(blur_frame,'Black',(30,60),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)

    elif 80 < np.average(color_detect) <= 150:
        cv2.putText(blur_frame,'Gray',(30,60),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)

    else:
        cv2.putText(blur_frame,'White',(30,60),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2) 

    if ret == False:
        break

    output.write() 
    cv2.imshow('camera', blur_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_cap.release()
output.release()
cv2.destroyAllWindows()


