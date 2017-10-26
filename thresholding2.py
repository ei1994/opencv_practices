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
# 中值滤波
img = cv2.medianBlur(img,5)
# 高斯滤波
blur = cv2.GaussianBlur(img,(5,5),0)
# 指定卷积核滤波
kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)

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

