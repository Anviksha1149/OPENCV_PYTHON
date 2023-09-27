import cv2
import numpy as np

img=cv2.imread("Resources/images/img2.jpg")

imgHor=np.hstack((img,img))

cv2.imshow("Output",imgHor)
cv2.waitKey(0)
