import cv2
import numpy as np

img=cv2.imread("smarties.png")
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

thresh1=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,0)
thresh2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,3,0)

cv2.imshow('frame',img)
cv2.imshow('frame1',thresh1)
cv2.imshow('frame2',thresh2)
cv2.waitKey(0)
cv2.destroyAllWindows()