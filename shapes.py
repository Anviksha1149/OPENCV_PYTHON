import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)  #to get the black window i.e the black image

#cv2.rectangle(img,(0,0),(250,250),(0,255,0),2)  #to make an outline of a rectangle in green color 

#cv2.rectangle(img,(0,0),(250,250),(0,0,255),cv2.FILLED)  #to create a filled rectangle

cv2.circle(img,(400,50),(30),(255,255,0),5) # to create an outline of the circle 

cv2.imshow("output",img)
cv2.waitKey(0)
