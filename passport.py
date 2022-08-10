import cv2
import numpy as np
from matplotlib import pyplot as plt
haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img=cv2.imread('images/bacha.jpg')
# img=cv2.imread('dishank.jpg')
# img=cv2.imread('dishank1.jpg')
# img=cv2.resize(img,(850,1300))
faces=haar_cascade.detectMultiScale(img,1.1,9)




for(x,y,w,h) in faces:
    
    print(x,y,w,h)
    # crop = img[y+5:y+h+5, x+5:x+w+5] 
    xcenter=x+w+x
    xcenter1=int(xcenter/2)
    ycenter=y+h+y
    ycenter2=int(ycenter/2)

    x1=int(xcenter1-(1*w))
    x2=int(xcenter1+(1*w))

    y1=int(ycenter2-(h))
    y2=int(ycenter2+(2*h))

    print(xcenter1,ycenter2)
    # print(xcenter1-110,ycenter2-110,xcenter1+110,ycenter2+150)

    # cv2.rectangle(img,(xcenter1-110,ycenter2-110),(xcenter1+110,ycenter2+150),(0,255,0),5)
    cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),5)

    crop=img[y1:y2,x1:x2]


cv2.imwrite('passport2.jpg',img)
cv2.imwrite('new.jpg',crop)
plt.imshow(img)
plt.imshow(crop)
plt.show()
# cv2.imshow('img',img)
# cv2.waitKey(0)



