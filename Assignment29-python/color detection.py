import numpy as np
import cv2


video_cap = cv2.VideoCapture(0)
width= int(video_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height= int(video_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


output = cv2.VideoWriter("5/cam_video.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 20.0,(width,height))

while True:
    ret,frame = video_cap.read()
    # frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    filter = np.ones((35,35),np.float32) / 35**2
    
    rect = frame[250:350,200:300]
    # rect = cv2.equalizeHist(rect)


    blur_frame = cv2.filter2D(frame,-1,filter)

    blur_frame[250:350,200:300] = rect

    
    color_detect = blur_frame[250:350,200:300] 
    gamma = 2

    lookUpTable = np.empty((1,256), np.uint8)
    for i in range(256):
        lookUpTable[0,i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)
    color_detect = cv2.LUT(color_detect, lookUpTable)

    b = color_detect[:, :, :1]
    g = color_detect[:, :, 1:2]
    r = color_detect[:, :, 2:]
    
  
    b_mean = np.mean(b)
    g_mean = np.mean(g)
    r_mean = np.mean(r)

    avg = (b_mean + g_mean + r_mean) // 3 

    
  

    if np.average(color_detect) > 225:
        cv2.putText(blur_frame,'White',(30,60),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)

    elif np.average(color_detect) < 30:
        cv2.putText(blur_frame,'Black',(30,60),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)

    elif 127 < np.average(color_detect) < 140:
        cv2.putText(blur_frame,'Gray',(30,60),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)

    elif r_mean < 140 and g_mean < 200 and b_mean > 200:
        cv2.putText(blur_frame,'Blue',(30,60),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)

    elif b_mean > 110 and g_mean > 110 and r_mean > 110:
        cv2.putText(blur_frame,'Gray',(30,60),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)

    

    

    # elif b_mean > g_mean and b_mean > r_mean:
    #     cv2.putText(blur_frame,'Blue',(30,60),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)



    # elif 60 < np.average(color_detect) <= 120:
    #     cv2.putText(blur_frame,'Gray',(30,60),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)

    # else:
    #     cv2.putText(blur_frame,'White',(30,60),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2) 

    if ret == False:
        break

    output.write(blur_frame) 
    cv2.imshow('camera', blur_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_cap.release()
output.release()
cv2.destroyAllWindows()


