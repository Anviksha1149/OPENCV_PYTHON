import cv2#Giving a grey image,a blur image,a canny image
img=cv2.imread("Resources/images/img1.jpg")
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imBlur=cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny=cv2.Canny(img,150,200)

cv2.imshow("Gray image",imgGray)
cv2.imshow("Blur Image",imBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.waitKey(0)