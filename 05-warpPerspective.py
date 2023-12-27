#try to warp and get birdeye perspective

import cv2
import numpy as np

img=cv2.imread('resources/cards.jpg')

# definign 4 coner points cordinates
pts1=np.float32([[111,219],[287,188],[154,482],[352,440]])

#defining new image points corresponding to above 4 points
width,height=250,350
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix=cv2.getPerspectiveTransform(pts1,pts2)
imgOutput=cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image",img)
cv2.imshow("Warp Image",imgOutput)
cv2.waitKey(0)