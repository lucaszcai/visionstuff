import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')


#blank[:] = 0, 255, 0
#cv.imshow('Green', blank)

cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=2)

cv.imshow('Blank', blank)

cv.waitKey(0)
