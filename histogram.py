import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# img=np.zeros((400,400),np.uint8)
img=cv.imread("images/apple.jpg")

hist=cv.calcHist(img,[0],None,[256],[0,256])
plt.plot(hist)
# cv.rectangle(img,(0,100),(100,200),(256),3)
b,g,r=cv.split(img)



# plt.hist(b.ravel(),256,[0,256])
# plt.hist(g.ravel(),256,[0,256])
# plt.hist(r.ravel(),256,[0,256])
plt.show()
# cv.imshow('b',b)
# cv.imshow('g',g)
# cv.imshow('r',r)

# cv.imshow("img",img)
cv.waitKey(0)