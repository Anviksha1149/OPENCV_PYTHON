import cv2
import numpy as np

#Giving a grey image,a blur image,a canny image and dialated images
img=cv2.imread("Resources/images/img1.jpg")
kernel=np.ones((5,5),np.uint8)


imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imBlur=cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny=cv2.Canny(img,150,200)
imgDialation=cv2.dilate(imgCanny,kernel,iterations=1)


cv2.imshow("Gray image",imgGray)
cv2.imshow("Blur Image",imBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dilated Image",imgDialation)
cv2.waitKey(0)
