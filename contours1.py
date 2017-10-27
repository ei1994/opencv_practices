import cv2
import numpy as np
import matplotlib.pylab as plt
import scipy.misc as misc

'''
函数 cv2.findContours() 有三个参数,第一个是输入图像,第二个是
轮廓检索模式,第三个是轮廓近似方法。返回值有三个,第一个是图像,第二个
是轮廓,第三个是(轮廓的)层析结构。轮廓(第二个返回值)是一个 Python
列表,其中存储这图像中的所有轮廓。每一个轮廓都是一个 Numpy 数组,包
含对象边界点(x,y)的坐标。
函数 cv2.drawContours() 可以被用来绘制轮廓。它可以根据你提供
的边界点绘制任何形状。它的第一个参数是原始图像,第二个参数是轮廓,一
个 Python 列表。第三个参数是轮廓的索引(在绘制独立轮廓是很有用,当设
置为 -1 时绘制所有轮廓)。接下来的参数是轮廓的颜色和厚度等
'''
img = cv2.imread('images/33.jpg',0)
#ret,th = cv2.threshold(img,127,255,0)
ret,th = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#image = th
image, contours, hierarchy = cv2.findContours(th,
                                cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# draw all the contours
img = cv2.drawContours(img, contours, -1, (0,255,0), 3)
# draw an individual contour
cnt = contours[4]
img1 = cv2.drawContours(img, [cnt], 0, (0,255,0),3)

cv2.imshow('result1.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
