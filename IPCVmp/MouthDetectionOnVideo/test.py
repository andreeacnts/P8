import cv2
import numpy as np

#cascPath = "D:/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml"
#eyePath = "D:/opencv/sources/data/haarcascades/haarcascade_eye.xml"
smilePath = "D:/opencv/sources/data/haarcascades/haarcascade_smile.xml"

#faceCascade = cv2.CascadeClassifier(cascPath)
#eyeCascade = cv2.CascadeClassifier(eyePath)
smileCascade = cv2.CascadeClassifier(smilePath)

font = cv2.FONT_HERSHEY_SIMPLEX
video_capture = cv2.VideoCapture('little-girl-laughing12.mp4')


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

    # Draw a rectangle around the faces
    for (x, y, w, h) in smile:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        cv2.putText(frame,'SMILEEEEEEEEE',(x, y), font, 2,(255,0,0),5)
    """

    for (sx, sy, sw, sh) in smile:
        cv2.rectangle(roi_color, (sh, sy), (sx+sw, sy+sh), (255, 0, 0), 2)
        cv2.putText(frame,'Smile',(x + sx,y + sy), 1, 1, (0, 255, 0), 1)
    # Display the resulting frame
        
    """
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()

with open("coords.txt","w+") as file:
    for idx in range(len(frame)):
        x, y, w, h = cv2.boundingRect(frame[idx])
        frame[y:y+h, x:x+w] = 0
        file.write("Box {0}: ({1},{2}), ({3},{4}), ({5},{6}), ({7},{8})".format(idx,x,y,x+w,y,x+w,y+h,x,y+h))
        cv2.drawContours(frame, frame, idx, (255, 255, 255), -1)
        r = float(cv2.countNonZero(frame[y:y+h, x:x+w])) / (w * h)
"""


    eyes = eyeCascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        cv2.putText(frame,'Eye',(x + ex,y + ey), 1, 1, (0, 255, 0), 1)

"""


# When everything is done, release the capture
