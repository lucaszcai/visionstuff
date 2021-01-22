import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    edges = cv2.Canny(frame, 100, 200)

    #plt.subplot(121), plt.imshow(frame, cmap='gray')
    #plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    #plt.subplot(122), plt.imshow(edges, cmap='gray')
    #plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

    cv2.imshow('frame', frame)
    cv2.imshow('edges', edges)

    # plt.show()

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
