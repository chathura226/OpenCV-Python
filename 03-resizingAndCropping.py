# resizing and cropping

"""
In openCV positive side of y axis is in opposite direction to conventional mathematics
X -axis is same. but positive y axis in towards downward instead of upward direction
"""
import cv2
import numpy as np

img = cv2.imread("resources/lambo.png")

# following will output the tupple (height,width,number of channels) n.channels-3 => BGR
print(img.shape)

# resizing
# secong parameter - tupple (width,height)
imgResized = cv2.resize(img, (300, 200))
print(imgResized.shape)

# cropping image
# from which array position to which position should be cropped
# hegiht (y direction) comes first
imgCropped = img[90:420, 65:520]

cv2.imshow("Image", img)
cv2.imshow("Resized Image", imgResized)
cv2.imshow("Cropped Image", imgCropped)
cv2.waitKey(0)
