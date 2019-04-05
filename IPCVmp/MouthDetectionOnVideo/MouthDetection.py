import cv2
import os
import sys
import matplotlib.pyplot as plt
import numpy as np

#path to opencv built in haar cascades used for object reognition
smilePath = "D:/opencv/sources/data/haarcascades/haarcascade_smile.xml" 
smileCascade = cv2.CascadeClassifier(smilePath)

font = cv2.FONT_HERSHEY_SIMPLEX #font used for text on bounding box
video_capture = cv2.VideoCapture('video11.mp4')

#use this for another video:
#video_capture = cv2.VideoCapture('laugh.mp4') 

#use this to capture via webcam:
#Note! 0 might have to be replaced with 1
#video_capture = cv2.VideoCapture(0)


while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    smile = smileCascade.detectMultiScale(
        gray,
        scaleFactor= 1.16,
        minNeighbors=35,
        minSize=(25, 25),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces = bounding box
    for (x, y, w, h) in smile:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        cv2.putText(frame,'SMILEEEEEEEEE',(x, y), font, 2,(255,0,0),5)
        cv2.putText(frame,'Number of Faces : ' + str(len(smile)),(40, 40), font, 1,(255,0,0),2)      

    #display the video with the bounding box
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()

