import os
import cv2

# read image
lena = cv2.imread('./assets/lena.png')

# blur image
# lena_out = cv2.blur(lena, (40,40)) # blur

# gaussian
lena_out = cv2.GaussianBlur(lena, (40,40), 5)
# visualize image
cv2.imshow('frame', lena_out)

cv2.waitKey(0)