import numpy as np
import cv2
import math


# Define object specific variables
dist = 0
focal = 450
pixels = 30
width = 4


# find the distance from then camera
def get_dist(rectangle_params, image):
    # find no of pixels covered
    pixels = rectangle_params[1][0]
    print(pixels)
    # calculate distance
    dist = (width*focal)/pixels

    # Wrtie n the image
    image = cv2.putText(image, 'Distance from Camera in CM :', org, font,
                        1, color, 2, cv2.LINE_AA)

    image = cv2.putText(image, str(dist), (110, 50), font,
                        fontScale, color, 1, cv2.LINE_AA)

    return image

def pixelDistance(x1,y1,x2,y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist


# Extract Frames
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)


# basic constants for opencv Functs
kernel = np.ones((3, 3), 'uint8')
font = cv2.FONT_HERSHEY_SIMPLEX
org = (0, 20)
fontScale = 0.6
color = (0, 0, 255)
thickness = 2


cv2.namedWindow('Object Dist Measure ', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Object Dist Measure ', 700, 600)


# loop to capture video frames
while True:
    ret, img = cap.read()

    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


    # predefined mask for green colour detection
    lower = np.array([20, 103, 102])
    upper = np.array([43, 239, 250])
    mask = cv2.inRange(hsv_img, lower, upper)

    cv2.imshow("mask", mask)

    # Remove Extra garbage from image
    d_img = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=5)

    # find the histogram
    cont, hei = cv2.findContours(
        d_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cont = sorted(cont, key=cv2.contourArea, reverse=True)

    boxes = []
    rects = []
    contours = []

    for cnt in cont:
        # check for contour area
        if (cv2.contourArea(cnt) > 200 and cv2.contourArea(cnt) < 306000):

            # Draw a rectangle on the contour
            rect = cv2.minAreaRect(cnt)
            box = cv2.boxPoints(rect)
            
            box = np.int0(box)
            rects.append(rect)
            boxes.append(box)
            #cv2.drawContours(img, [cnt], -1, (255, 0, 0), 3)

            #img = get_dist(rect, img)
            
    img = cv2.putText(img, str(len(boxes)), org, font, 1, color, 2, cv2.LINE_AA)
    fwidth = img.shape[1]
    fheight = img.shape[0]
    print("width: " + str(fwidth) + " height: " + str(fheight))
    img = cv2.circle(img, (int(fwidth/2), int(fheight/2)), 5, color, 2)

    for rect in rects:
        box = cv2.boxPoints(rect)
        
        box = np.int0(box)

        area = cv2.contourArea(box)

        cv2.drawContours(img, [box], -1, (255, 0, 0), 3)
        #print(rect)
        #print(box)
        #print(area)
        img = cv2.putText(img, str(area), (box[1][0], box[1][1]), font, 1, color, 2, 1)
        img = cv2.line(img, (box[1][0], box[1][1]), (int(fwidth/2), int(fheight/2)), color, 2) 

        distance = pixelDistance(box[1][0], box[1][1], int(fwidth/2), int(fheight/2))
        img = cv2.putText(img, str(distance), (box[1][0], box[1][1] + 40), font, 1, color, 2, 2)


    
    # for box in boxes:
    #     cv2.drawContours(img, [box], -1, (255, 0, 0), 3)
    #     #cv2.drawContours(img, boxes, -1, (255, 0, 0), 3)
    #     #print(box)
    #     img = cv2.putText(img, str(len(boxes)), (box[1][1], box[1][1]), font, 1, color, 2, cv2.LINE_AA)

    cv2.imshow('Object Dist Measure ', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
