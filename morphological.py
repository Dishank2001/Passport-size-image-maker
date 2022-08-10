import imghdr
import cv2
from cv2 import dilate
from cv2 import imshow
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('smarties.png',1)

img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,mask=cv2.threshold(img1,130,255,cv2.THRESH_BINARY)

kernel=np.ones((3,3),np.uint8)

dilation=cv2.dilate(mask,kernel,iterations=2)
erosion=cv2.erode(mask,kernel,iterations=2)
morpho=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
morphocls=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)

titles=['img','mask','dilation','erosion','morpho','morphocls']
image=[img,mask,dilation,erosion,morpho,morphocls]

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(image[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])


plt.show()
cv2.destroyAllWindows()