import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while (True):
    ret , frame = cap.read()

    #coversion from color to gray
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)

    #make edge detection , and countours easy by blending pixels reduces noise

    blur =  cv2.GaussianBlur(gray, (3,3), 0)

    #Extract the area of the hand from background
    #segment the image by binarizing it  (threshold)
    # OTSU good for back and forre-ground images
    ret , otsu = cv2.threshold( blur ,0 , 255 , cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    #thresh = cv2.erode(otsu,None, iterations = 2)
    thresh = cv2.dilate (otsu, None , iterations = 2)
    # show image
    cv2.imshow ('Original',gray)
    #cv2.imshow ('Blur' , blur)
    cv2.imshow ('OTSU' , otsu)
    cv2.imshow('thresh' , thresh )
  #find the countors in the image
    im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# find the largest countour
    areas = [cv2.contourArea(temp) for temp in contours]
    max_index = np.argmax(areas)
    largest_contour = contours[max_index]


# draw the largest countours

    #cv2.drawContours(frame, largest_contour, -1, (0,255,0), 3)
    #cv2.imshow('frame' , frame )

# take out vertices
    approx = cv2.approxPolyDP(largest_contour, .01*cv2.arcLength(largest_contour,True), True)

    cv2.drawContours(frame, approx, -1, (0,255,0), 3)
    cv2.imshow('approx' , frame )

# Determine convex hull of the  polygon, Using Vertices for forming convex hull
# return a set of points that can be used to draw a convex hull of the hand

    hull = cv2.convexHull (approx, returnPoints = True  )

#write how many fingers to screen is the user holding

    cv2.putText(frame ,'Number of Fingers ' + str (len(hull)-2),(10,30),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,0,0))

#draws convex hull around the hand
    cv2.drawContours(frame,[hull],0,(0,0,255),1)

    cv2.imshow('new frame' , frame )
    # see if ESC key is pressed every  1 MS
    keyPressed = cv2.waitKey(1)
    print(str(keyPressed))

    if  keyPressed == 27:
        break

cv2.destroyAllWindows()
cam.release()
