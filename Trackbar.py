import cv2

import numpy as np

def empty(z):
    pass

#Create a black background

image = np.zeros((300,512,3),np.uint8)
cv2.namedWindow('Palette')

#create trackbars for colors and associated those with Pallete
cv2.createTrackbar('B','Palette',0,255,empty)
cv2.createTrackbar('G','Palette',0,255,empty)
cv2.createTrackbar('R','Palette',0,255,empty)

while(True):
    cv2.imshow('Palette',image)
    if cv2.waitKey(1)==27:
        break

    #fetch color value
    blue = cv2.getTrackbarPos('B','Palette')
    green = cv2.getTrackbarPos('G','Palette')
    red = cv2.getTrackbarPos('R','Palette')

    image[:]=[blue,green,red]


#cv2.destroyWindow('Palette')
cv2.destroyAllWindows()
