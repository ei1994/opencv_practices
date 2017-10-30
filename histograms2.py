'''
直方图均衡化，灰色图像和彩色图像
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('images/33.jpg')
grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#直方图均衡化
equ = cv2.equalizeHist(grey)
res = np.hstack((grey,equ)) #stacking images side-by-side

# create a CLAHE object (Arguments are optional).
# 分块局部均衡化
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
res1 = clahe.apply(grey)
'''
• channels=[0,1] 因为我们需要同时处理 H 和 S 两个通道。
• bins=[180,256]H 通道为 180,S 通道为 256。
• range=[0,180,0,256]H 的取值范围在 0 到 180,S 的取值范围
在 0 到 256。
'''
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

#plt.plot(hist)
plt.imshow(hist,interpolation = 'nearest')
plt.xlim([0,256])
plt.show()


#cv2.imshow('hsv.jpg',hsv)
#cv2.imshow('res.jpg',res)
#cv2.imshow('res1.jpg',res1)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(0)
cv2.waitKey(0)
cv2.waitKey(0)
cv2.waitKey(0)
