import cv2
import numpy as np
img=cv2.imread('images/bacha.jpg')
# Image zoom 
img = cv2.resize(img,None,fx=0.5,fy=0.5)
rows,cols,channels = img.shape
print(rows,cols,channels)
cv2.imshow('img',img)
# Picture to grayscale 
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('hsv',hsv)
# Binarization of pictures 
lower_blue=np.array([90,70,70])
upper_blue=np.array([110,255,255])
mask = cv2.inRange(hsv, lower_blue, upper_blue)
# Corrosion expansion  
erode=cv2.erode(mask,None,iterations=1)
cv2.imshow('erode',erode)
dilate=cv2.dilate(erode,None,iterations=1)
cv2.imshow('dilate',dilate)
# Traversal substitution 
for i in range(rows):
    for j in range(cols):
        if erode[i,j]==255: # The pixels are 255 It means white , We just want to put the pixels in white , Replace with red 
            img[i,j]=(255,0,255) # Replace the color here , by BGR passageway , No RGB passageway 
cv2.imshow('res',img)
# Window waiting for commands ,0 It means infinite waiting 
cv2.waitKey(0)