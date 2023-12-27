# detecting shapes
import cv2
import numpy as np
from UtilityFunctions import stackImages


def getContours(img):
    # retrieving extreme outer contours and get all countours without approximations
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        # getting area of each
        area = cv2.contourArea(cnt)
        print(area)
        # drawing the contours
        # -1 is for index.  index=-1 => drawing on the image
        # drawing on imgContour with blue color by line with thickness 3
        # below if statement is so that it wont detect any noise and draw only true shapes
        if area > 500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            # getting perimeter (True - for closed shapes)
            perimeter = cv2.arcLength(cnt, True)
            # print(perimeter)
            # getting corner points of each shape
            approx = cv2.approxPolyDP(cnt, 0.02 * perimeter, True)
            print(len(approx))  # printing length (count) of corners

            # creating object corners to make a bounding box around detected object
            objCorners = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            # categorizing
            if objCorners == 3:
                ObjectType = "Triangle"
            elif objCorners == 4:
                aspectRatio=w/float(h)
                if aspectRatio >0.95 and aspectRatio <1.05:
                    ObjectType = "Square"
                else:
                    ObjectType = "Rectangle"
            elif objCorners > 4:
                ObjectType = "Circle"
            else:
                ObjectType = "None"

            # drawing the bounding box
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(imgContour, ObjectType, (x + (w // 2) - 10, y + (h // 2) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        (0, 0, 0), 2)


path = 'resources/shapes.png'
img = cv2.imread(path)
imgContour = img.copy()

# preprocessing
# converting to grayscale and finding corner points by finding edges
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)

getContours(imgCanny)

# cv2.imshow('Original', img)
# cv2.imshow('Gray', imgGray)
# cv2.imshow('Blur', imgBlur)

imgBlank = np.zeros_like(img)
stackedImages = stackImages(0.5, ([img, imgGray, imgBlur], [imgCanny, imgContour, imgBlank]))
cv2.imshow('Stacked Images', stackedImages)
cv2.waitKey(0)
