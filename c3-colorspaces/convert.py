import cv2

img = cv2.imread('./assets/lena.png')
'''
BGR2RGB
BGR2GRAY
BGR2HSV
...
https://docs.opencv.org/3.4/de/d25/imgproc_color_conversions.html
'''

img_cvt = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('Lena',img_cvt)
cv2.waitKey(0)