import cv2
import numpy as np

# Reigon of intrest (ROI) helps to move a particular part in a image or cropped a image seprately

img=cv2.imread("messi.jpg",1)

cropped_image=img[280:340, 330:390]
img[270:330,320:380]=cropped_image

cv2.imshow('image',img)
cv2.waitKey(0)