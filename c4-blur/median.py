import os
import cv2
import numpy as np

# read image
lena = cv2.imread('./assets/lena.png')

k = 10
img_median_blur = cv2.medianBlur(np.copy(lena), 51)
cv2.imshow('frame', img_median_blur)
cv2.waitKey(0)