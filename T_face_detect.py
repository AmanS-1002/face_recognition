import cv2
#using wecam to capture the vedio
cap=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier("harrcascase_frontalface_alt.xml")
while True:
    ret,frame=cap.read()
    if ret==False:
        continue
    gray_scale=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(gray_scale,1.3,5)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow("vedio frame",frame)
   # cv2.imshow('gray vedio',gray_scale)

    #wait for user to stop

    key_pressed=cv2.waitKey(1) & 0xFF #converting 32bit number to 8bit as ord lies bw 0-255 and bitwise and with 0xFF gives last 8 bits
    if key_pressed==ord('q'):#ord gives ascii values
        break
cap.release()
cv2.destroyAllWindows()