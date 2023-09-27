import cv2
import numpy as np

#Giving a grey image,a blur image,a canny image , dialated images and eroded image
img=cv2.imread("Resources/images/img1.jpg")
kernel=np.ones((5,5),np.uint8)


imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imBlur=cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny=cv2.Canny(img,150,200)
imgDialation=cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded=cv2.erode(imgDialation, kernel,iterations=1)

cv2.imshow("Gray image",imgGray)
cv2.imshow("Blur Image",imBlur)
cv2.imshow("Canny Image",imgCanny)#shows the edges of the image
cv2.imshow("Dilated Image",imgDialation)#shows the thicker edges 
cv2.imshow("Eroded image",imgEroded)#shows kind of thinner edges
cv2.waitKey(0)
