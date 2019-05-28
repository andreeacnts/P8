import cv2
import pandas as pd
import numpy as np

smilePath = "D:/opencv/sources/data/haarcascades/haarcascade_smile.xml"
facePath = "D:/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml"
face_classifier = cv2.CascadeClassifier(facePath)
smile_classifier = cv2.CascadeClassifier(smilePath)

startxs = []
endxs = []
startys = []
endys = []

cap = cv2.VideoCapture(r"movie_resized.mp4")
#cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #gray = cv2.GaussianBlur(gray, (21, 21), 0)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 1)
        roi_gray = gray[y:y + h, x:x + w]
        roi_img = img[y:y + h, x:x + w]
        smile = smile_classifier.detectMultiScale(roi_gray, scaleFactor=1.2,
                                                  minNeighbors=22,
                                                  minSize=(25, 25))
        for (sx, sy, sw, sh) in smile:
            cv2.rectangle(roi_img, (sx, sy), (sx + sw, sy + sh),
                          (0, 255, 0), 1)
            startx = str(round(sx))
            endx = str(round(sw))
            starty = str(round(sy))
            endy = str(round(sh))
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, 'Smile meter : ', (10, 50), font, 1,
                        (200, 255, 155), 2, cv2.LINE_AA)

            startxs.append(startx)
            endxs.append(endx)
            startys.append(starty)
            endys.append(endy)

    cv2.imshow('Smile Detector', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break


ds = {'startx': startxs, 'endx': endxs, 'starty': startys, 'endy': endys}
df = pd.DataFrame(ds)
df.to_csv('smile_records.csv')

cap.release()
cv2.destroyAllWindows()
