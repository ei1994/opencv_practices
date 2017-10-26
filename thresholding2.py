import cv2
import numpy as np
import matplotlib.pylab as plt
import scipy.misc as misc

'''
Adaptive Method - It decides how thresholding value is calculated.

    cv2.ADAPTIVE_THRESH_MEAN_C : threshold value is the mean of neighbourhood area.
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C : threshold value is the weighted sum of neighbourhood values
                                where weights are a gaussian window.

Block Size - It decides the size of neighbourhood area.

C - It is just a constant which is subtracted from the mean or weighted mean calculated.
'''
img = cv2.imread('images/32.jpg',0)
# 中值滤波，卷积核是奇数
img = cv2.medianBlur(img,5)
# 高斯滤波，求加权平均值，必须是奇数
blur = cv2.GaussianBlur(img,(5,5),0)
# 指定卷积核滤波,平均滤波器
kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)
#dst = cv2.blur(img,(5,5))   # 平均滤波
'''
双边滤波在同时使用空间高斯权重和灰度值相似性高斯权重。空间高斯函
数确保只有邻近区域的像素对中心点有影响,灰度值相似性高斯函数确保只有
与中心像素灰度值相近的才会被用来做模糊运算。所以这种方法会确保边界不
会被模糊掉,因为边界处的灰度值变化比较大。
'''
#邻域直径,两个 75 分别是空间高斯函数标准差,灰度值相似性高斯函数标准差
bila = cv2.bilateralFilter(img,9,75,75)

ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#11 为 Block size, 2 为 C 值
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                            cv2.THRESH_BINARY,11,2)
titles = ['Original Image', 'Global Thresholding (v = 127)',
          'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]

for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

