import cv2
import numpy as np
img=cv2.imread("messi.jpg",1)
img1=cv2.imread("2.png",1)

img=cv2.resize(img,(512,512))
img1=cv2.resize(img1,(512,512))
#For adding image always resize the image to same otherwise adding image is not pssible
add=cv2.add(img,img1)
addWeighted1=cv2.addWeighted(img,0.6,img1,0.8,0)#In this we can add percentage of image 



cv2.imshow('image',addWeighted1)
cv2.waitKey(0)