#canny

import cv2

FILE_NAME='images/sokrates.jpg'
try:
    img = cv2.imread(FILE_NAME)
    
    edges = cv2.Canny(img, 50, 50)
    
    cv2.imwrite('images/sokrates_canny.jpg', edges)
except IOError:
    print('File not found !')
