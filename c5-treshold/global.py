import numpy as np
import cv2

# read image
lena = cv2.imread('../assets/lena.png')

img_gray = cv2.cvtColor(np.copy(lena), cv2.COLOR_BGR2GRAY)

ret, tresh = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY)
# visualize image
cv2.imshow('frame', tresh)

cv2.waitKey(0)