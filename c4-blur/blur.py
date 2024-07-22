import os
import cv2
import numpy as np

# read image
lena = cv2.imread('./assets/lena.png')


lena_out = lena

def averaging_blocks(x, y):
    for i in range(0, lena_out.shape[0], x):
        for j in range(0, lena_out.shape[1], y):
            avg_color = np.mean(lena_out[i:i+x, j:j+y], axis=(0, 1))
            lena_out[i:i+x, j:j+y] = avg_color

def averaging(y,x):
    inp = np.copy(lena)
    a, c = x // 2, y // 2
    b, d = x - a, y - c
    out = np.zeros_like(inp)
    for i in range(out.shape[0]):
        for j in range(out.shape[1]):
            out[i, j] = inp[max(0, i - a) : i + b, max(0, j - c) : j + d].mean(axis=(0, 1))
    cv2.imshow('frame', out)
    cv2.waitKey(0)

k = 10
averaging(10,20)
cv2.imshow('frame', cv2.blur(np.copy(lena), (10, 20)))
cv2.waitKey(0)