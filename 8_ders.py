import cv2
import numpy as np

cap = cv2.VideoCapture("images/blueball.mp4")

while(1):
    ret, frame = cap.read()
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_blue = np.array([60,35,140])
    upper_blue = np.array([133,255,255])
    
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    result = cv2.bitwise_and(frame, frame, mask= mask)
    
    
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)
    
    cv2.waitKey(0)
    
cv2.destroyAllWindows()
cap.release()
