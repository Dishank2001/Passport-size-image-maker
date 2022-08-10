from tkinter import font
import cv2
import numpy as np


def click_event(event,x,y,flag,param):
    if event == cv2.EVENT_FLAG_LBUTTON:
        print(x," ",y)
        font=cv2.FONT_HERSHEY_COMPLEX
        strXY=str(x)+" ,"+str(y)
        cv2.putText(img,strXY,(x,y),font,1,(255,0,255),1,cv2.LINE_AA)
        cv2.imshow('image',img)

       


img=cv2.imread('2.png',1)
img=np.zeros((580,580,3),np.uint8)# For creating image by numpy with black bg
img1=cv2.line(img,(0,0),(255,255),(0,255,0),5) #line
img1=cv2.arrowedLine(img,(0,0),(45,150),(0,255,0),5) #arrowed line
img1=cv2.rectangle(img,(0,300),(90,180),(0,0,255),5) #Rectangle
img1=cv2.circle(img,(200,100),(50),(0,255,0),-1) #Ciecle
img1=cv2.rectangle(img,(118,219),(187,308),(255,0,255),5)
font=cv2.FONT_HERSHEY_COMPLEX #font style for text 
img1=cv2.putText(img,'Text',(5,300),font,5,(255,255,0),5,cv2.LINE_4)#Text on image

cropped_image = img1[220:307, 118:187] 

# cv2.imshow('image',img1)
# cv2.setMouseCallback('image',click_event)
cv2.imshow('image',cropped_image)

cv2.waitKey(0)



# cv2.imwrite('image1.png',img)
cv2.destroyAllWindows