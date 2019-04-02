import cv2
import numpy as np


faceDetection = cv2.CascadeClassifier('D:\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml')
   
VideoFeed = cv2.VideoCapture(0) #Value can be either 0 or 1

while 1:
    ret, img = VideoFeed.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    faces = faceDetection.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
    cv2.imshow('img',img)
    cv2.imshow('gray', gray)
    cv2.imshow('hsv', hsv)
    #cv2.imshow('h',h)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

VideoFeed.release()
cv2.destroyAllWindows()

