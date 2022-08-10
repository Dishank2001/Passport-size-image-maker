import cv2
from cv2 import imread
import numpy as np
from matplotlib import pyplot as plt

img1=cv2.imread("images/chessboard.png")
img1=cv2.resize(img1,(400,512))
img=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(img,200,255,cv2.THRESH_BINARY)
contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print("number of contours are"+str(len(contours)))
cv2.drawContours(img1,contours,-1,(255,0,0),3)


cv2.imshow("img",thresh)
cv2.imshow("img",img1)
cv2.waitKey(0)
