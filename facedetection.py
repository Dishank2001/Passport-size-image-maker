from multiprocessing.connection import wait
import cv2
import numpy as np

img=cv2.imread("images/bacha.jpg")
# cap=cv2.VideoCapture(0)

haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


# img=cv2.imread('images/messi.jpg')
# while True:
#     _,img=cap.read()
#     # img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=haar_cascade.detectMultiScale(img,1.1,9)

for(x,y,w,h) in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)
    print(x,y,w,h)


cv2.imshow('crop',img)
cv2.imwrite("crop1.jpg",img)

cv2.waitKey(0)
# key=cv2.waitKey(1)
# if key==27:
#     brake
    

    








   


