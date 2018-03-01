#!/usr/bin/env python
import cv2
import skin_detector
import argparse
import logging
import cv2


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-b', '--debug', dest='debug', action='store_true', help='enable debug logging')
    parser.add_argument('-t', '--thresh', dest='thresh', default=0.5, type=float, help='threshold for skin mask')
    args = parser.parse_args()

    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("main")


#img_path = input('/home/pi/SkinDetector/test_image.png')

#image = cv2.imread('/home/pi/book/code/test_set/lena_color_512.tif',1)
image = cv2.imread('/home/pi/SkinDetector/test_image.png',1)

mask = skin_detector.process(image)

cv2.imshow("input", image)
cv2.imshow("mask", mask)
cv2.waitKey(0)
