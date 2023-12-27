# basic functions when using openCV

import cv2
import numpy as np

img = cv2.imread("resources/lena.png")

# converting to greyscale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# adding blur
# ksize - size of the kernel or filter that is applied to the image.
# It's a tuple specifying the width and height of the kernel.
# (both ksize values must be odd numbers - for well defined center pixel)
# sigmaX - how much the values around each pixel contribute to the blur calculation
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)

# edge detector ( in here, Canny edge detector)
# my note - higher threshold values => low number of edges
imgCanny = cv2.Canny(img, 150, 200)

# matrix of 5x5 filled with 1
kernel = np.ones((5, 5), np.uint8)

# some edges don't get detected because of a gap or not joint , it doenst get detected as a proper line
# for that we can increase thickness of edge by using dialation
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)

# opposite of dialation - erode (to make thinner edge)
imageErode = cv2.erode(imgDilation, kernel, iterations=1)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dilated Image", imgDilation)
cv2.imshow("Eroded Image", imageErode)
cv2.waitKey(0)
