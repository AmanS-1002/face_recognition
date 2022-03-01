import cv2
#using wecam to capture the vedio
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    if ret==False:
        continue
    gray_scale=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("vedio frame",frame)
    cv2.imshow('gray vedio',gray_scale)

    #wait for user to stop

    key_pressed=cv2.waitKey(1) & 0xFF #converting 32bit number to 8bit as ord lies bw 0-255 and bitwise and with 0xFF gives last 8 bits
    if key_pressed==ord('q'):#ord gives ascii values
        break
cap.release()
cv2.destroyAllWindows()