import cv2

import numpy as np
#Create a 3D array of zeros ( Black Canvas ( row , colum , depth - 3 color))
# type : unsigned integers

image = np.zeros((200,200,3), np.uint8)

# initial point @ 2 arg , final point at @ 3 argument , thickness
cv2.line(image,(0,199), (199,0) , (0,0,255) , 2)

# creates rectangle
cv2.rectangle(image , (20,20) , (60,60) , (255,0,0), 1)

# circle with (80,80) center , radius of 10

cv2.circle ( image , (80,80) ,10 , (0,255,0) , -1  )

# print words
cv2.putText(image , 'TEST' ,(80,180) , cv2.FONT_HERSHEY_DUPLEX , 1 , (255,0,255))

cv2.imshow('Shapes', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
