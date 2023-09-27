import cv2
import numpy as np
img=np.zeros((512,512,3),np.uint8)
cv2.putText(img,"OPENCV",(250,250),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,0),1)
cv2.imshow("output",img)
cv2.waitKey(0)
