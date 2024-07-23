import numpy as np
import cv2

# read image
text = cv2.imread('../assets/text.png')

img_gray = cv2.cvtColor(np.copy(text), cv2.COLOR_BGR2GRAY)

tresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 30)
# visualize image
cv2.imshow('frame', tresh)

cv2.waitKey(0)