# ways to draw shapes and texts on images

import cv2
import numpy as np

# matrix of 512x512 filled with zeros (zero=>black)
# 3 - for 3 channel (BGR) and 8 bit int for 256 values
img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)

# applying blue to whole image
wholeImage = np.copy(img)
wholeImage[:] = 255, 255, 0

# applying red to part of image
partImage = np.copy(img)
partImage[100:200, 100:200] = 0, 0, 255

# adding lines
# params - img,(x0,y0),(x1,y1),(B,G,R),thickness
cv2.line(img, (100, 200), (300, 300), (0, 0, 255), 3);
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3);

# adding rectangle
cv2.rectangle(img, (300, 400), (500, 100), (255, 0, 0),2)
#filled
cv2.rectangle(img, (0, 400), (200, 100), (255, 0, 0),cv2.FILLED)

#adding circle
cv2.circle(img,(100,100),100,(255,255,0),1)

#adding text
cv2.putText(img,"Test Text",(100,100),cv2.FONT_ITALIC,0.9,(255,255,255),1)

cv2.imshow("Image", img)
cv2.imshow("Whole Blue Image", wholeImage)
cv2.imshow("Part Red Image", partImage)

cv2.waitKey(0)
