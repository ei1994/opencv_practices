import cv2
import numpy as np
import matplotlib.pylab as plt
import scipy.misc as misc

'''
。 OpenCV 为我们提供了函数 cv2.cornerSubPix(),
它可以提供亚像素级别的角点检测。下面是一个例子。首先我们要找到 Harris
角点,然后将角点的重心传给这个函数进行修正。Harris 角点用红色像素标
出,绿色像素是修正后的像素。在使用这个函数是我们要定义一个迭代停止条
件。当迭代次数达到或者精度条件满足后迭代就会停止。我们同样需要定义进
行角点搜索的邻域大小。
'''
img = cv2.imread('images/33.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
# 输入图像必须是 float32 ,最后一个参数在 0.04 到 0.05 之间
dst = cv2.cornerHarris(gray,2,3,0.04)
#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)

## Threshold for an optimal value, it may vary depending on the image.
#img[dst>0.1*dst.max()]=[0,0,255]
#cv2.imshow('dst',img)


ret, dst = cv2.threshold(dst,0.01*dst.max(),255,0)
dst = np.uint8(dst)
# find centroids
#connectedComponentsWithStats(InputArray image, OutputArray labels, OutputArray stats,
#OutputArray centroids, int connectivity=8, int ltype=CV_32S)
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
# define the criteria to stop and refine the corners
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
#Python: cv2.cornerSubPix(image, corners, winSize, zeroZone, criteria)
#zeroZone – Half of the size of the dead region in the middle of the search zone
#over which the summation in the formula below is not done. It is used sometimes
# to avoid possible singularities of the autocorrelation matrix. The value of (-1,-1)
# indicates that there is no such a size.
# 返回值由角点坐标组成的一个数组(而非图像)
corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)
# Now draw them
res = np.hstack((centroids,corners))
#np.int0 可以用来省略小数点后面的数字(非四五入)。
res = np.int0(res)
img[res[:,1],res[:,0]]=[0,0,255]
img[res[:,3],res[:,2]] = [0,255,0]

cv2.imshow('subpixel5.png',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
