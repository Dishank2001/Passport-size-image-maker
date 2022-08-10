import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

img=cv2.imread('images/bacha.jpg')

segmentor=SelfiSegmentation()
segmentor.removeBG(img,(255,0,255))

cv2.imshow('rmg',img)
cv2.waitKey(0)