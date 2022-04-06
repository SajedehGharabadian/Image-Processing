import cv2


video = cv2.VideoCapture(0)

while True:
    ret,frame = video.read()
    
    if ret == False:
        break

    img_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    img_blurred = cv2.GaussianBlur(img_gray,(5,5),3)

    thresh = cv2.adaptiveThreshold(img_blurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)

    contours = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contours =  contours[0]

    contours = sorted(contours,key=cv2.contourArea,reverse=True)

    sodoku_contour = None

    for contour in contours:
        epsilon = 0.15 * cv2.arcLength(contour,True)
        approx = cv2.approxPolyDP(contour,epsilon,True)
        if len(approx) == 4:
            sodoku_contour = approx
            break

    if sodoku_contour is None:
        print("Not found sodoku table!")


    else:
        result = cv2.drawContours(frame,[sodoku_contour],-1,(0,255,0),4)
        x,y,w,h = cv2.boundingRect(sodoku_contour)

    if cv2.waitKey(1) == ord('s'):
        cv2.imwrite('result.jpg',result[y:y+h,x:x+w])
    

    elif cv2.waitKey(1) == ord('q'):
        break

    cv2.imshow('frame',frame)
