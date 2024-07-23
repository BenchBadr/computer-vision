import os
import cv2

img = cv2.imread('../assets/lena.png')

# line
cv2.line(img, (100,0), (512, 512), (0,255,0), 10)

# rectangle
cv2.rectangle(img, (200, 200), (350, 400), (255,0,0), -1) #put negative thickness to fill rectangle

#circle
cv2.circle(img, (100, 350), 100, (0,0,255), 3)

#text
cv2.putText(img, 'Lenna Forsen', (300,300), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,0), 5)
cv2.imshow('frame', img)
cv2.waitKey(0)