# from tkinter import font
# import cv2
# from matplotlib.pyplot import text

# cap=cv2.VideoCapture(0)

# while(True):
#     ret,frame=cap.read()

#     font=cv2.FONT_HERSHEY_COMPLEX
#     text="bale bale"
#     frame=cv2.putText(frame,text,(50,200),font,2,(0,0,255),4,cv2.LINE_AA)

#     cv2.imshow('frame',frame)
#     if cv2.waitKey(1) & 0xff == ord('q'):
#         break


# cap.release()
# cv2.destroyAllWindows()
#print date and time on video

from tkinter import font
import cv2
from matplotlib.pyplot import text
import datetime

cap=cv2.VideoCapture(0)

while(True):
    ret,frame=cap.read()

    font=cv2.FONT_HERSHEY_COMPLEX
    text=str(datetime.datetime.now())
    frame=cv2.putText(frame,text,(50,200),font,2,(0,0,255),4,cv2.LINE_AA)

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()