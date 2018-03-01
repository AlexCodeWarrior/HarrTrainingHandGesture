import cv2

#read source image
img = cv2.imread('/home/pi/book/code/test_set/lena_color_512.tif',1)

#shows image
cv2.imshow('Lena',img)

#waits indefently for key press
cv2.waitKey(0)


cv2.destroyWindow('Lena')
