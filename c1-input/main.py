import os
import cv2

# read image
lena = cv2.imread('./assets/lena.png')

# write image
cv2.imwrite('./assets/lena_out.png', lena)

# visualize image
cv2.imshow('frame', lena)
cv2.waitKey(0)