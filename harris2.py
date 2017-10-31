import cv2
import numpy as np
import matplotlib.pylab as plt
import scipy.misc as misc

'''
使用 Shi-Tomasi 方法获取图像中 N 个最好的角点
'''
img = cv2.imread('images/33.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
#25指的是找到25个角点；0.01是指：角点的质量水平,0
#到1之间；10指的是最短欧氏距离
corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
# 返回的结果是 [[ 311., 250.]] 两层括号的数组。
corners = np.int0(corners)
for i in corners:
  x,y = i.ravel()
  cv2.circle(img,(x,y),3,255,-1)
#plt.imshow(img),plt.show()

cv2.imshow('subpixel5.png',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
