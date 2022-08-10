import cv2
from matplotlib import image
import numpy as np

def nothing(x):
    pass

cv2.namedWindow('track',cv2.WINDOW_NORMAL)
cv2.createTrackbar('LH','track',0,255,nothing)
cv2.createTrackbar('LS','track',0,255,nothing)
cv2.createTrackbar('LV','track',0,255,nothing)

cv2.createTrackbar('UH','track',255,255,nothing)
cv2.createTrackbar('US','track',255,255,nothing)
cv2.createTrackbar('UV','track',255,255,nothing)

while True:
    img=cv2.imread('smarties.png')

    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    l_h=cv2.getTrackbarPos('LH','track')
    l_s=cv2.getTrackbarPos('LS','track')
    l_v=cv2.getTrackbarPos('LV','track')

    u_h=cv2.getTrackbarPos('UH','track')
    u_s=cv2.getTrackbarPos('US','track')
    u_v=cv2.getTrackbarPos('UV','track')

    l_b=np.array([l_h,l_s,l_v])
    u_b=np.array([u_h,u_s,u_v])

    mask=cv2.inRange(hsv,l_b,u_b) 

    res =cv2.bitwise_and(img,img,mask=mask)


    cv2.imshow('frame',img)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
     

    wait=cv2.waitKey(1)
    if wait == 27:
        break

cv2.destroyAllWindows()  

