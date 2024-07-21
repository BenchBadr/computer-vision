import cv2

# read image
lena = cv2.imread('./assets/lena.png')
print(f'Original : {lena.shape}')

# resize
lena_resize = cv2.resize(lena, (2**11, 2**11))
print(f'Resized : {lena_resize.shape}')

# write image
cv2.imwrite('./assets/lena_resized.png', lena)

# visualize image
cv2.imshow('frame', lena_resize)
cv2.waitKey(0)