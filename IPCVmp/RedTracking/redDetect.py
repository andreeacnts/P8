import cv2
import numpy as np

#capture from file
cap = cv2.VideoCapture('video11.mp4')

#capture from webcam
#might have to change value 0 to 1
#cap = cv2.VideoCapture(0)


while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #setting lower and upper threasholds for the color red
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])

    #mask on the frame to show the red areas
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red = cv2.bitwise_and(frame, frame, mask = red_mask)
    conts, h=cv2.findContours(red_mask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    #creating a bounding box around the areas containing red
    #coordinates for rextangle given by x,y,w,h
    for i in range(len(conts)):
        x,y,h,w = cv2.boundingRect(conts[i])
        cv2.rectangle(frame, (x,y), (x+h, y+w), (0,0,255),2)

        #printing x y coordinates 
        print(x,y)

    #displaying original frame with bounding box
    cv2.imshow("Frame", frame)
    #displaying masked image
    cv2.imshow("Red", red)
    key = cv2.waitKey(1)
    if key == 27: 
        break

