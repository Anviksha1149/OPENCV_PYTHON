import cv2
img=cv2.imread("Resources/images/img1.jpg")
imgGrey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Grey Image",imgGrey)
cv2.waitKey(0)
