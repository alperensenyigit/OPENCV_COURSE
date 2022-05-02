import cv2
import numpy as np

lower_blue = np.array([60,35,140])
upper_blue = np.array([133,255,255])

cap = cv2.VideoCapture("images/blueball.mp4")

while True:
    ret, video = cap.read()
    
    img = cv2.cvtColor(video, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(img, lower_blue, upper_blue)
    
    mask_contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    if len(mask_contours) != 0:
        for mask_contour in mask_contours:
            if cv2.contourArea(mask_contour) > 500:
                x, y, w, h = cv2.boundingRect(mask_contour)
                cv2.rectangle(video, (x, y), (x+w, y+h), (0, 255, 0), 2)
                
                cp_x = x + w/2
                cp_y = y + h/2
                
                cv2.circle(video, (int(cp_x), int(cp_y)), 3, (0, 0, 255), -1)
                # otonom algoritmalar
                #hedef tespit algoritmaları
                
    cv2.imshow('video', video)
    cv2.imshow('mask', mask)
    
    cv2.waitKey(20)
                
            