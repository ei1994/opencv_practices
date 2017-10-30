import cv2
import numpy as np
import matplotlib.pylab as plt
import scipy.misc as misc

'''

'''
img = cv2.imread('images/11.jpg')
ret,thresh = cv2.threshold(cv2.cvtColor(img,cv2.COLOR_BGR2GRAY),127,255,0)
_,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)#得到轮廓信息
cnt = contours[1]#取第一条轮廓
M = cv2.moments(cnt)#计算第一条轮廓的各阶矩,字典形式

imgnew = cv2.drawContours(img, contours, -1, (0,255,0), 3)#把所有轮廓画出来
#print (M)
#这两行是计算中心点坐标
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

#计算轮廓所包含的面积
area = cv2.contourArea(cnt)

#计算轮廓的周长
# 第二参数可以用来指定对象的形状是闭合的(True),还是打开的(一条曲线)。
perimeter = cv2.arcLength(cnt,False)


#轮廓的近似,近似到另外一种由更少点组成的轮廓形状
epsilon = 0.02*perimeter
approx = cv2.approxPolyDP(cnt,epsilon,True)
imgnew1 = cv2.drawContours(img, approx, -1, (0,0,255), 3)

cv2.imshow('result1.jpg', imgnew)    
cv2.imshow('result2.jpg', imgnew1)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
