import cv2
from cv2 import destroyAllWindows
import numpy as np


points=[]

def click_event(event,x,y,flag,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        cv2.line(img,(0,0),(x,y),(115,255,255),2)
        cv2.imshow('image',img)
        points.append((x,y))
    if len(points)>=2:
        cv2.line(img,points[-1],points[-2],(200,115,254),1)
        cv2.imshow('image',img)    




# img=np.zeros((512,512,3),np.uint8)
img=cv2.imread('2.png',1)
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
destroyAllWindows()