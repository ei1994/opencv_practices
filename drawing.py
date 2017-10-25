import cv2
import numpy as np

# creat a black image
img = np.zeros((512,512,3), np.uint8)

# draw a diagonal blue line with thickness of 5 px
cv2.line(img, (0,0),(511,511),(255,0,0),5)

# draw a rectangle
cv2.rectangle(img, (384,0),(510,128),(0,255,0),3)

# draw a circle, -1:fill the circle
cv2.circle(img, (447,63),63,(0,0,255),-1)

# draw a ellipse
cv2.ellipse(img,(256,256),(100,50),0,0,180,(255,0,255),-1)

#draw a polygon
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
# if the third argument is Flase, you will get a polylines joining all the points, not a closed shape.
cv2.polylines(img,[pts],True,(0,255,255))

# add text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'opencv',(10,500),font,4,(255,255,255),7,cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
