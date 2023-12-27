# detecting face through webcam
import cv2
import numpy as np

# importing cascade for face detectipn
faceCascade = cv2.CascadeClassifier('resources/haarcascades/haarcascade_frontalface_default.xml')


# to use webcam , type '0' instead of video path or 1 if have more than 1 webcams
cap = cv2.VideoCapture(0)
# defining
#  width => prop_id=3
# height = > prop_id = 4
# brightness = > prop_id = 10
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 50)
while True:
    # read() will return whether read successfully and the image
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # finding faces using cascade
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('Original', img)
    # cv2.imshow("Video", img)
    # adding a delay and look for keypress 'q' for breaking loop if user want to stop,
    # otherwise it will stop automatically after playing whole video
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
