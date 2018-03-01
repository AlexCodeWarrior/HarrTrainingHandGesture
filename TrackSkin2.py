import numpy as np

import cv2

# get hold of camera
cam = cv2.VideoCapture(0)

while (True):
    # read frame of camera
    ret, frame = cam.read()

    #  convert to HSV
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # check if it is an color range of skin
    skinMask = cv2.inRange(hsv,np.array([0,48,80]), np.array([20,255,255]))

    # apply a series of erosions and dilations to the mask
    # using an elliptical kernel

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    skinMask = cv2.erode(skinMask, kernel, iterations = 2)
    skinMask = cv2.dilate(skinMask, kernel, iterations = 2)

    # blur the mask to help remove noise, then apply the
    # mask to the frame
    skinMask = cv2.GaussianBlur(skinMask, (3, 3), 0)


    #cut out the rest and shows only the green
    output = cv2.bitwise_and(frame, frame , mask= skinMask)

    cv2.imshow ('Original',frame)
    cv2.imshow ('Output',output)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
cam.release()
