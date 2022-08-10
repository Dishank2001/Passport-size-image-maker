import cv2
from cv2 import Laplacian
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("3.jpg")
img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

lap=Laplacian(img,2,cv2.CV_16U,ksize=3)
lap=np.uint8(np.absolute(lap))

sobelx=cv2.Sobel(img,cv2.CV_64F,1,0)
sobely=cv2.Sobel(img,cv2.CV_64F,0,1)

sobelx=np.uint8(np.absolute(sobelx))
sobely=np.uint8(np.absolute(sobely))


titles=['img','lap','sobelx','sobely']
images=[img,lap,sobelx,sobely]

for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])


plt.show()
