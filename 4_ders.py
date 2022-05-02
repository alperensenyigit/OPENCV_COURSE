import cv2
from cv2 import waitKey

img = cv2.imread('images/sokrates.jpg')

cv2.imshow('image', img)
cv2.waitKey(0)

#gaussian blur
Gaus = cv2.GaussianBlur(img, (5, 5), 0)
cv2.imshow('Gaus', Gaus)
cv2.waitKey(0)

#Median Blur
Median = cv2.medianBlur(img, 5)
cv2.imshow('Median', Median)
cv2.waitKey(0)
