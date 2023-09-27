import cv2
import numpy as np
img=np.zeros((512,512,3),np.uint8)
#img[:]=255,0,0  #color blue for the whole window
img[200:300,100:300]=255,0,0  #color blue in a part
cv2.imshow("Image",img)
cv2.waitKey(0)
