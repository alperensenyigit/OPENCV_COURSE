import cv2

WIDTH = 480
HEIGHT = 480

img = cv2.imread('images/python.png')
imgR= cv2.resize(img, (WIDTH, HEIGHT))

gray = cv2.cvtColor(imgR, cv2.COLOR_BGR2GRAY)

cv2.imshow('image', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()