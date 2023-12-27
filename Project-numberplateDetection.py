# numberplate detection using webcams
import numpy as np
import cv2

##########################
framewidth = 640
frameheight = 480
# importing cascade for plate detectipn
numberplateCascade = cv2.CascadeClassifier('resources/haarcascades/haarcascade_russian_plate_number.xml')
minArea = 500
color = (255, 0, 255)
count = 0
############################
cap = cv2.VideoCapture(2)
cap.set(3, framewidth)
cap.set(4, frameheight)
cap.set(10, 50)
while True:
    success, img = cap.read()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plates = numberplateCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in plates:
        area = w * h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img, "Number Plate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)

            imgRoi = img[y:y + h, x:x + w]  # croppping to save the plate
            cv2.imshow("Number Plate", imgRoi)

    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("ScannedPlates/NoPlate_" + str(count) + ".jpg", imgRoi)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"Scan saved!",(150,265),cv2.FONT_HERSHEY_DUPLEX,2,(0,0,255),2)
        cv2.imshow("Result", img)
        cv2.waitKey(500)
        count += 1
