import cv2
import matplotlib.pyplot as plt

img = cv2.imread('/home/pi/book/code/test_set/Peppers.tiff',1 )

img = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)

plt.imshow (img) , plt.title('COLOR IMAGE')
plt.xticks([]) , plt.yticks([])
plt.show()
