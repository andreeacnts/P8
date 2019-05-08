import cv2 
import pandas as pd 

#path to opencv built in haar cascades for smile and face recognition
smilePath = "D:/opencv/sources/data/haarcascades/haarcascade_smile.xml"
facePath = "D:/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml"
face_classifier = cv2.CascadeClassifier(facePath) 
smile_classifier = cv2.CascadeClassifier(smilePath)


#capture video from file
cap = cv2.VideoCapture('video11.mp4')
#capture video via webcam
#might have to change value 0 to 1
#cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    
    #make bounding box around detected face
    #face bounding box coordinates given by x,y,w,y
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 1)
        roi_gray = gray[y:y + h, x:x + w]
        roi_img = img[y:y + h, x:x + w]
        smile = smile_classifier.detectMultiScale(roi_gray, scaleFactor=1.2,
                                                  minNeighbors=22,
                                                  minSize=(25, 25))
        #make bounding box around detected smile
        #face bounding box coordinates given by sx,sy,sw,sy
        for (sx, sy, sw, sh) in smile:
            cv2.rectangle(roi_img, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 1)

            #define width/height ratio in order to detect a smile
            sm_ratio = str(round(sw / (sx+2), 3)) 
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, 'Smile meter : ' + sm_ratio, (10, 50), font, 1, (200, 255, 155), 2, cv2.LINE_AA)

            #print x,y coordinates for face and smile bounding box
            print(x,y,sx,sy)

    cv2.imshow('Smile Detector', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break



cap.release()
cv2.destroyAllWindows()