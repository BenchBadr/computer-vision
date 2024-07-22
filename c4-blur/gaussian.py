import os
import cv2
import numpy as np

# read image
lena = cv2.imread('./assets/lena.png')

k = 10
img_blurred = cv2.GaussianBlur(np.copy(lena), (11,11), 5)
cv2.imshow('frame', img_blurred)
cv2.waitKey(0)