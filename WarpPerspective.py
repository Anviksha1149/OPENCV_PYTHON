import cv2
import numpy as np
img=cv2.imread("Resources/images/img3.jpg")

width,height=300,300
ps1=np.float32([[150,60],[280,90],[110,250],[240,280]])
ps2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv2.getPerspectiveTransform(ps1,ps2)
imgWarp=cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Output",img)
cv2.imshow("Warp",imgWarp)
cv2.waitKey(0)
