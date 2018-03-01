import numpy as np
import cv2

# cv2.rectangle( destination, (x0,y0), ( width . height)...)
# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier('data/haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    #convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # configure settings
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # go through each face recognized and create a square around it
    for (x,y,w,h) in faces:
        #draw rectangle where face located and put in image
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        # grab the particular faces identified for further processing
        roi_gray = gray[y:y+h, x:x+w]
        # grab the particular faces identified in color to be use to place eye in it
        roi_color = img[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            #draw eyes within the face identified
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
