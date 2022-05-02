import cv2

FILE_NAME = 'images/sokrates.jpg'

try:
    img = cv2.imread(FILE_NAME)
    
    (height, width) = img.shape[:2]
    
    res = cv2.resize(img, (int(width / 2), int(height / 2)), interpolation = cv2.INTER_CUBIC)
    
    cv2.imwrite('images/sokrates_resized.jpg', res)
    
except IOError:
    print('File not found !')