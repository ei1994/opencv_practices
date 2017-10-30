import cv2
import numpy as np
'''
反向投影，根据颜色直方图和模板检测图像中像素值，
实现图像分割、背景与图像分离
'''
roi = cv2.imread('images/roi.jpg')
hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
target = cv2.imread('images/apple.jpg')
hsvt = cv2.cvtColor(target,cv2.COLOR_BGR2HSV)
# calculating object histogram
roihist = cv2.calcHist([hsv],[0, 1], None, [180, 256], [0, 180, 0, 256] )
# normalize histogram and apply backprojection
# 归一化:原始图像,结果图像,映射到结果图像中的最小值,最大值,归一化类型
#cv2.NORM_MINMAX 对数组的所有值进行转化,使它们线性映射到最小值和最大值之间
# 归一化之后的直方图便于显示,归一化之后就成了 0 到 255 之间的数了。
cv2.normalize(roihist,roihist,0,255,cv2.NORM_MINMAX)
dst = cv2.calcBackProject([hsvt],[0,1],roihist,[0,180,0,256],1)
# Now convolute with circular disc
# 此处卷积可以把分散的点连在一起
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))  #生成的卷积核
dst=cv2.filter2D(dst,-1,disc)
# threshold and binary AND
ret,thresh = cv2.threshold(dst,10,255,0)
# 别忘了是三通道图像,因此这里使用 merge 变成 3 通道
thresh = cv2.merge((thresh,thresh,thresh))
# 按位操作
res = cv2.bitwise_and(target,thresh)
res = np.hstack((target,thresh,res))
#cv2.imwrite('res.jpg',res)
# 显示图像
cv2.imshow('res.jpg',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(0)
cv2.waitKey(0)
cv2.waitKey(0)
cv2.waitKey(0)
