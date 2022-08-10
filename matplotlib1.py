# import cv2
# from matplotlib import pyplot as plt
# import numpy as np

# img=cv2.imread("messi.jpg")
# img1=cv2.imread("messi.jpg")
# img2=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)#actually plt show in the rgb form so we need to convert it to show original
# plt.imshow(img2)
# plt.show()

# cv2.imshow("frame",img1)

# cv2.waitKey(0)
# cv2.destroyAllWindows



import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('messi.jpg')
img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,a1=cv2.threshold(img1,50,255,cv2.THRESH_BINARY)
ret,a2=cv2.threshold(img1,50,255,cv2.THRESH_BINARY_INV)
ret,a3=cv2.threshold(img1,50,255,cv2.THRESH_MASK)
ret,a4=cv2.threshold(img1,50,255,cv2.THRESH_TOZERO)
ret,a5=cv2.threshold(img1,50,255,cv2.THRESH_TRUNC)
# ret,a6=cv2.threshold(img,50,255,cv2.THRESH_TRIANGLE)

titles=['img','a1','a2','a3','a4','a5']
images=[img,a1,a2,a3,a4,a5]

for i in range(6):
    plt.subplot(3,2,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])


plt.show()