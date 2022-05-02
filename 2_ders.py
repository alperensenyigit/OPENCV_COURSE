import cv2

img = cv2.imread('images/python.png')

cv2.putText(img, 'Hello World!', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
cv2.rectangle(img, (10, 10), (100, 100), (0, 255, 0), 4)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()