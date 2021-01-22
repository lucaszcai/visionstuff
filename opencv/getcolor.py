
import numpy as np
import cv2

cap = cv2.VideoCapture(0)


def empty(a):
    pass


# trackbars for adjusting hsv
cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 300, 300)
cv2.createTrackbar("HUE Min", "HSV", 0, 179, empty)
cv2.createTrackbar("HUE Max", "HSV", 179, 179, empty)
cv2.createTrackbar("SAT Min", "HSV", 0, 255, empty)
cv2.createTrackbar("SAT Max", "HSV", 255, 255, empty)
cv2.createTrackbar("VALUE Min", "HSV", 0, 255, empty)
cv2.createTrackbar("VALUE Max", "HSV", 255, 255, empty)


while True:
    ret, img = cap.read()
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # read trackbar positions
    h_min = cv2.getTrackbarPos("HUE Min", "HSV")
    h_max = cv2.getTrackbarPos("HUE Max", "HSV")
    s_min = cv2.getTrackbarPos("SAT Min", "HSV")
    s_max = cv2.getTrackbarPos("SAT Max", "HSV")
    v_min = cv2.getTrackbarPos("VALUE Min", "HSV")
    v_max = cv2.getTrackbarPos("VALUE Max", "HSV")

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    # color mask
    mask = cv2.inRange(hsv_img, lower, upper)

    cv2.imshow('image', mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("HUE min: " + str(h_min))
        print("HUE max: " + str(h_min))
        print("SAT min: " + str(s_min))
        print("SAT max: " + str(s_max))
        print("VALUE min: " + str(v_min))
        print("VALUE max: " + str(v_max))
        break

cv2.destroyAllWindows()
