# project - document scanner

import cv2
import numpy as np
from UtilityFunctions import stackImages

#########################
widthImg = 640
heightImg = 480
#########################


cap = cv2.VideoCapture(2)
cap.set(3, widthImg)
cap.set(4, heightImg)


def preProcessing(img):
    imgGrayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGrayscale, (5, 5), 1)
    imgCanny = cv2.Canny(imgBlur, 200, 200)
    # somtime edges are very thin, so we make them thicker using dialate function
    # and little bit thinner again by using erode function.
    # In here we use 2 iterations of dialation and 1 pass of erode
    kernel = np.ones((5, 5))
    imgDialated = cv2.dilate(imgCanny, kernel, iterations=2)
    imgThreshold = cv2.erode(imgDialated, kernel, iterations=1)

    return imgThreshold


# findinfg contours
def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    biggest = np.array([])
    maxArea = 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 5000:
            # cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            perimeter = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * perimeter, True)
            print(len(approx))
            if area > maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area

    cv2.drawContours(imgContour, biggest, -1, (255, 0, 0), 20)  # coloring 4 corner points of biggestcontour
    return biggest


# reordering points before send to warp
def reorder(mypoints):
    # shape of biggest is (4,1,0) . 1 is redundant, we are reshaping to remove it in below
    mypoints = mypoints.reshape((4, 2))

    myPointsNew = np.zeros((4, 1, 2), np.int32)
    add=mypoints.sum(1)  #taking sum of x+y for each point

    #reordering
    myPointsNew[0]=mypoints[np.argmin(add)]  #smallest sum is origin
    myPointsNew[3]=mypoints[np.argmax(add)]  #biggest sum is diaganally opposite point

    diff=np.diff(mypoints,axis=1)  #taking difference betwewen x and y
    myPointsNew[1]=mypoints[np.argmin(diff)]
    myPointsNew[2]=mypoints[np.argmax(diff)]

    return myPointsNew

# getting bird eye view
def getWarp(img, biggest):
    biggest=reorder(biggest)
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgOutput = cv2.warpPerspective(img, matrix, (widthImg, heightImg))

    #smooting corner edges - croping to remove edges
    imgCropped=imgOutput[20:imgOutput.shape[0]-20,20:imgOutput.shape[1]-20]
    imgCropped=cv2.resize(imgCropped,(widthImg,heightImg))
    return imgCropped


while True:
    success, img = cap.read()
    cv2.resize(img, (widthImg, heightImg))
    imgContour = img.copy()

    imgThreshold = preProcessing(img)
    biggest = getContours(imgThreshold)  # getting biggest contour points
    if biggest.size!=0:
        warpedImg = getWarp(img, biggest)
        imgArr=([img,imgThreshold],[imgContour,warpedImg])
    else:
        imgArr=([img,imgThreshold],[img,img])


    stackedImage=stackImages(0.8, imgArr)
    cv2.imshow('Result', stackedImage)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
