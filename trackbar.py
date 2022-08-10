# import cv2 as cv
# import numpy as np

# def nothing(x):
#     print(x)

# img1=np.zeros((512,512,3),np.uint8)
# img=cv.imread("messi.jpg",1)
# cv.namedWindow('image')

# trackbar=cv.createTrackbar('B','image',0,255,nothing)
# trackbar=cv.createTrackbar('G','image',0,255,nothing)
# trackbar=cv.createTrackbar('R','image',0,255,nothing)


# while(1):
#     cv.imshow('image',img1)
#     k=cv.waitKey(1) & 0xFF
#     if k==27:
#         break


#     b=cv.getTrackbarPos('B','image')
#     g=cv.getTrackbarPos('G','image')
#     r=cv.getTrackbarPos('R','image')

#     img1[:]=[b,g,r]

# cv.destroyAllWindows    


import cv2
from cv2 import destroyAllWindows
import numpy as np

def nothing(x):
    print(x)



cv2.namedWindow('image')
cv2.createTrackbar('B','image',10,400,nothing)


while True:
    img=cv2.imread("messi.jpg",1)
    b=cv2.getTrackbarPos('B','image')
    b=str(b)
    font=cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(img,b,(100,200),font,2,(200,143,254),6,cv2.LINE_AA)
    cv2.imshow('image',img)

    key=cv2.waitKey(1)
    if key == 27:
        break


destroyAllWindows()
