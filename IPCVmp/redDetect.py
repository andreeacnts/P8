# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 14:53:02 2019

@author: laumo
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red = cv2.bitwise_and(frame, frame, mask = red_mask)
    conts, h=cv2.findContours(red_mask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    for i in range(len(conts)):
        x,y,h,w = cv2.boundingRect(conts[i])
        cv2.rectangle(frame,(x,y),(x+w, y+h),(0,0,225),2)
        
    cv2.imshow("Frame", frame)
    cv2.imshow("Red", red)
    key = cv2.waitKey(1)
    if key == 27: 
        break