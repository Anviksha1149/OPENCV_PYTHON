import cv2
import numpy as np

img=cv2.imread("Resources/images/img2.jpg")
print(img.shape)

#imgResize=cv2.resize(img,(300,200))
#print(imgResize.shape)
imgCrop=img[0:200,200:500]   #first part is for the height and the secong part is for the width
cv2.imshow("Image",img)
#cv2.imshow("Resized image",imgResize)
cv2.imshow("Cropped image",imgCrop)
cv2.waitKey(0)
