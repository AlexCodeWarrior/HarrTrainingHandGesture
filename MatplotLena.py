import cv2

import matplotlib.pyplot as plt

img = cv2.imread('/home/pi/book/code/test_set/lena_color_512.tif',0)

plt.imshow(img,cmap='gray')

plt.title('Lena')

plt.xticks([])

plt.yticks([])

plt.show()
