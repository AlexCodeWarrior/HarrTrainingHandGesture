import cv2

img = cv2.imread('/home/pi/book/code/test_set/lena_color_512.tif',1)

cv2.imshow('Lena',img)
#get the key pressed by user
keyPress = cv2.waitKey(0)
# check if key pressed is q
if keyPress == ord('q'):
    cv2.destroyWindow('Lena')
#check if the key pressed is s 
elif keyPress == ord('s'):
    cv2.imwrite('/home/pi/book/output/chapter2_prog2_output.jpg',img)
    cv2.destroyWindow('Lena')
