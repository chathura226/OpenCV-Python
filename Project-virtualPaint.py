# virtual paint using webcam
import cv2
import numpy as np

# webcam
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(2)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 50)

# myColors got from colorPicker in resources folder
# for each color h_min,h_max,s_min,s_max,v_min,v_max each defined
# im writing the values in the order : h_min,s_min,v_min,h_max,s_max,v_max
greenPen = [76,70,165,88,187,247]
bluePen = [92,116,142,105,198,245]
orangePen = [108,57,255,179,181,255]
myColors = [greenPen, bluePen, orangePen]
# defining RGB colors for above three respectively (green,blue,orange)
mycolorValues = [[0, 255, 0], [255, 0, 0], [51, 153, 255]]

# drawing
myPoints = []  # [x,y,colorIndex]


# find colors
def findColor(img, myColors, mycolorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    count = 0
    newPoints = []
    for color in myColors:
        # creating mask
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        cv2.circle(imgResult, (x, y), 10, mycolorValues[count], cv2.FILLED)
        if x != 0 and y != 0:
            newPoints.append([x, y, count])
        count += 1
        # cv2.imshow(str(color[0]),mask)
    return newPoints


def getContours(img):
    # retrieving extreme outer contours and get all countours without approximations
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        # getting area of each
        area = cv2.contourArea(cnt)
        # drawing the contours
        # -1 is for index.  index=-1 => drawing on the image
        # drawing on imgContour with blue color by line with thickness 3
        # below if statement is so that it wont detect any noise and draw only true shapes
        if area > 500:
            # cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            # getting perimeter (True - for closed shapes)
            perimeter = cv2.arcLength(cnt, True)
            # print(perimeter)
            # getting corner points of each shape
            approx = cv2.approxPolyDP(cnt, 0.02 * perimeter, True)

            # creating object corners to make a bounding box around detected object
            x, y, w, h = cv2.boundingRect(approx)
    return x + w // 2, y


# to Draw according to prev and new points
def drawOnCanvas(myPoints, mycolorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, mycolorValues[point[2]], cv2.FILLED)


while True:
    # read() will return whether read successfully and the image
    success, img = cap.read()
    img=np.fliplr(img)
    imgResult = img.copy()
    newPoints = findColor(img, myColors, mycolorValues)
    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)

    if len(myPoints) != 0:
        drawOnCanvas(myPoints, mycolorValues)
    # print(myPoints)

    cv2.imshow("Result", imgResult)
    # adding a delay and look for keypress 'q' for breaking loop if user want to stop,
    # otherwise it will stop automatically after playing whole video
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
