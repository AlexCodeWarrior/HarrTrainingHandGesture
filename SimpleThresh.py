import cv2

import matplotlib.pyplot as plt

img = cv2.imread('/home/pi/book/code/test_set/gray21.512.tiff',0)
th = 127
max_val=255

ret,o1 = cv2.threshold(img , th , max_val , cv2.THRESH_BINARY)
ret ,o2 = cv2.threshold(img , th , max_val , cv2.THRESH_BINARY_INV)
ret ,o3 = cv2.threshold(img, th, max_val , cv2.THRESH_TOZERO)
ret, o4 = cv2.threshold(img, th, max_val , cv2.THRESH_TOZERO_INV)
ret, o5 = cv2.threshold(img , th , max_val , cv2.THRESH_TRUNC)

titles = [ 'Input Images ' , 'BINARY ' , 'Binary Inv' , 'TOZERO' ,
'TOZERO_INV', 'TRUNC']

output = [img , o1 , o2 , o3 , o4 , o5 ]

for i in range(6):
    plt.subplot( 2 , 3 , i+1), plt.imshow ( output [i] , cmap='gray')
    plt.title(titles [i])
    plt.xticks([]),plt.yticks([])
plt.show()
