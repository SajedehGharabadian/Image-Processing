
import numpy as np
import cv2


video_cap = cv2.VideoCapture(0)
face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eyes_left_detector = cv2.CascadeClassifier("haarcascade_lefteye_2splits.xml")
eyes_right_detector = cv2.CascadeClassifier("haarcascade_righteye_2splits.xml")
smile_detector = cv2.CascadeClassifier("haarcascade_smile.xml")

img2 = cv2.imread('img/smile.png')
img3 = cv2.imread('img/mouth.png')
img4 = cv2.imread('img/eye.png')

def add_sticker(img1,img,x,y,w,h):
    rows,cols,chnnels = img.shape
    
    roi = img1[y:y+cols,x:x+rows]
    print(x,y)
    
    # Now create a mask of logo and create its inverse mask also
    img2gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    row,col,channel = roi.shape
    
    mask = cv2.resize(mask,(col,row))
    mask_inv = cv2.bitwise_not(mask)
    mask_inv = cv2.resize(mask_inv,(col,row))
    img = cv2.resize(img,(col,row))
    # Now black-out the area of logo in ROI
    img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
    # Take only region of logo from logo image.
    img2_fg = cv2.bitwise_and(img,img,mask = mask)
    # Put logo in ROI and modify the main image
    dst = cv2.add(img1_bg,img2_fg)
    img1[y:y+cols,x:x+rows] = dst
    cv2.imshow('res',img1)
    cv2.waitKey(0)

while True:
    ret,frame = video_cap.read()
    
    if ret == False:
        break

    faces = face_detector.detectMultiScale(frame,1.8) 
    eyes_left = eyes_left_detector.detectMultiScale(frame,1.8,5)
    eyes_right = eyes_right_detector.detectMultiScale(frame,1.8,5)
    smiles = smile_detector.detectMultiScale(frame,1.8,20) 

    if cv2.waitKey(1) == ord('1'):
       for i,face in enumerate(faces):
            x,y,w,h = face
            img2 = cv2.resize(img2,(w,h))
            row,col,chnnels = img2.shape
            print(x,y,w,h)
            # print(img2.shape)
            # print(img1.shape)
            add_sticker(frame,img2,x,y,w,h)
            
            

    elif cv2.waitKey(1) == ord('2'):
        for i,right_eye in enumerate(eyes_right):
            x,y,w,h = right_eye
            img4 = cv2.resize(img4,(h,w))
            row,col,chnnels = img4.shape
            add_sticker(frame,img4,x,y,w,h)

        for i,left_eye in enumerate(eyes_left):
            x,y,w,h = left_eye
            img4 = cv2.resize(img4,(h,w))
            row,col,chnnels = img4.shape
            add_sticker(frame,img4,x,y,w,h)



        for i,smile in enumerate(smiles):
            x,y,w,h = smile
            print(x,y,w,h)
            img3 = cv2.resize(img3,(h-20,w-40))
            row,col,chnnels = img3.shape
            print(img3.shape)
            print(frame.shape)
            add_sticker(frame,img3,x+15,y,w,h)

    elif cv2.waitKey(1) == ord('3'):
        for i,face in enumerate(faces):
            x,y,w,h = face
            frame[y:y+h, x:x+h] = cv2.blur(frame[y:y+h, x:x+h],(10,10))

            square = cv2.resize(frame[y:y+h,x:x+w], (10,10))
            output = cv2.resize(square, (w, h), interpolation=cv2.INTER_NEAREST)
            frame[y:y+h, x:x+h] = output



    elif cv2.waitKey(1) == ord('4'):
        for i,face in enumerate(faces):
            x,y,w,h = face   
            face = frame[y:y+h,x:x+w]         
            img = cv2.flip(face,-1)
            # img = cv2.resize(img,(w,h))
            frame[y:y+h,x:x+w] = img
        

    cv2.imshow('frame',frame)

    cv2.waitKey(1)  #ejra 10ms


    