import cv2
import numpy as np

faceDetection = \
    cv2.CascadeClassifier('D:\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml'
                          )

VideoFeed = cv2.VideoCapture(0)  # Value can be either 0 or 1

out = cv2.VideoWriter('output.avi', -1, 20.0, (640, 480))

while 1:
    (ret, img) = VideoFeed.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, (36, 25, 25), (70, 0xff, 0xff))

## slice the green

imask = mask > 0
green = np.zeros_like(img, np.uint8)
green[imask] = img[imask]

## save

cv2.imwrite('green.mp4', green)

faces = faceDetection.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0xff, 0, 0), 2)
    roi_gray = gray[y:y + h, x:x + w]
    roi_color = img[y:y + h, x:x + w]

    # cv2.imshow('img',img)

cv2.imshow('gray', gray)
out.write(img)

k = cv2.waitKey(30) & 0xff
if k == 27:
   break

VideoFeed.release()
out.release()
cv2.destroyAllWindows()


			