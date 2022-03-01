#simple programme to show an  imagee
import cv2
img=cv2.imread('1127036.jpg')
gray_img=cv2.imread('1127036.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('generic wallpaper',img)#reads as bgr rather than matplotlib that reads as rgb
cv2.imshow('lmao',gray_img)
cv2.waitKey(0)#pyts programme to hold until image croossed if not 0 then the input is considered as ms
cv2.destroyAllWindows()