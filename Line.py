import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)
#cv2.line(img,(0,0),(300,300),(0,255,0),3)  #line having origin at 0,0 and end coordinates at 300,300
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,0,255),3) #line across the whole window

cv2.imshow("Output",img)
cv2.waitKey(0)
