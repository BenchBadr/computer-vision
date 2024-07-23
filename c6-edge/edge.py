import numpy as np
import os
import cv2

# read image
basket = cv2.imread('../assets/basket.png')
img_edge = cv2.Canny(basket, 0, 150)
img_edge_d = cv2.dilate(img_edge, np.ones((3, 3), dtype=np.int8))
img_edge_e = cv2.erode(img_edge_d, np.ones((3, 3), dtype=np.int8))
# visualize image
cv2.imshow('frame', img_edge)
cv2.waitKey(0)
cv2.imshow('frame', img_edge_d)
cv2.waitKey(0)
cv2.imshow('frame', img_edge_e)
cv2.waitKey(0)