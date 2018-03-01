import cv2

import matplotlib.pyplot as plt
img = cv2.imread('/home/pi/book/code/test_set/tank_star.tiff',0)

# ret is boolean , ouput contain next frame
ret, output = cv2.threshold(img, 0 , 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

imgplot = plt.imshow(output , cmap = 'gray')
plt.show()
