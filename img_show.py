import cv2
import matplotlib.pyplot as plt

img = cv2.imread('images/1.jpg',0) 

# 1. direct to show
cv2.imshow('result.jpg',img)
cv2.imwrite('result.jpg',img)
cv2.waitKey(0)  # wait for any keyboard event
cv2.destroyAllWindows() 
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)

## 2. creat a window to show
#cv2.namedWindow('image',cv2.WINDOW_NORMAL)
#cv2.imshow('image', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

## 3.plt to show
#plt.imshow(img,cmap='gray')
#plt.xticks([]), plt.yticks([])
##plt.show()
