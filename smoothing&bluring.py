import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("2.png")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

kernel=np.ones((5,5),np.uint8)/25
dst=cv2.filter2D(img,-1,kernel=kernel)
blur1=cv2.blur(img,(5,5))
gblur=cv2.GaussianBlur(img,(5,5),0)
median1=cv2.medianBlur(img,5)






titles=['img','dst','blur','gblur','median1']
images=[img,dst,blur1,gblur,median1]

for i in range(5):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])


plt.show()
