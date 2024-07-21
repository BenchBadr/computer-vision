import cv2

# read image
lena = cv2.imread('./assets/lena.png')
print(f'Original : {lena.shape}')

# crop
lena_crop = lena[200:312, 200:312]
print(f'Resized : {lena_crop.shape}')

# write image
cv2.imwrite('./assets/lena_resized.png', lena)

# visualize image
cv2.imshow('frame', lena_crop)
cv2.waitKey(0)