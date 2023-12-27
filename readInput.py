# reading images,videos and web cams

import cv2

print("Package imported successfully!")

# reading images
"""
img = cv2.imread("resources/lena.png")
cv2.imshow("Output", img)
# to wait without auto closing the image use waitKey()
# 0 - infinite delay, other value means that number of miliseconds
cv2.waitKey(1000)
"""

# reading videos
"""
cap = cv2.VideoCapture("resources/testVideo.mp4")
while True:
    # read() will return whether read successfully and the image
    success, img = cap.read()
    cv2.imshow("Video", img)
    # adding a delay and look for keypress 'q' for breaking loop if user want to stop, otherwise it will stop automatically after playing whole video
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
"""

# reading from webcam

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
    cv2.imshow("Video", img)
    # adding a delay and look for keypress 'q' for breaking loop if user want to stop, otherwise it will stop automatically after playing whole video
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
