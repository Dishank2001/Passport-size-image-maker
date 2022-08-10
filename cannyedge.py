import cv2
from cv2 import createTrackbar
from cv2 import namedWindow
from cv2 import getTrackbarPos
import numpy as np
from matplotlib import pyplot as plt

def nothing(x):
    pass

img=cv2.imread("2.png")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

namedWindow('track')
createTrackbar('A','track',0,255,nothing)
createTrackbar('B','track',0,255,nothing)



while True:
    a=getTrackbarPos('A','track')
    b=getTrackbarPos('B','track')
    cannyedge=cv2.Canny(img,a,b)
    cv2.imshow('frame',img)
    cv2.imshow('frame1',cannyedge)

    k=cv2.waitKey(1)
    if k==27:
        break

