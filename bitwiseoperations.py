import cv2
from cv2 import destroyAllWindows
import numpy as np
img1=cv2.imread("chessboard.png",1)
img1=cv2.resize(img1,(512,512))
img2=cv2.bitwise_not(img1)
bitwiseand1=cv2.bitwise_and(img1,img2,)
bitwiseor1=cv2.bitwise_or(img1,img2,)
bitwisexor1=cv2.bitwise_xor(img1,img2)

cv2.imshow('',bitwisexor1)
cv2.imshow('image1',bitwisexor1)
cv2.imshow('image1',bitwisexor1)
cv2.imshow('image1',bitwisexor1)
# cv2.imshow('image',img1)
cv2.waitKey(0)
destroyAllWindows()