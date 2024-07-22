import cv2
import numpy as np
# read webcam
webcam = cv2.VideoCapture(0)

# visualize webcam
while True:
    ret, frame = webcam.read()
    cv2.imshow('Video Frame', cv2.medianBlur(np.copy(frame), 51))
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()