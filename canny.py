import cv2
import numpy as np
import matplotlib.pylab as plt
import scipy.misc as misc

'''
这个函数的第一个参数是输入图像。第二和第三
个分别是 minVal 和 maxVal。第三个参数设置用来计算图像梯度的 Sobel
卷积核的大小,默认值为 3。最后一个参数是 L2gradient,它可以用来设定
求梯度大小的方程。如果设为 True,就会使用我们上面提到过的方程,否则
使用方程:Edge − Gradient (G) = |G 2 x | + |G 2 y | 代替,默认值为 False。
'''
img = cv2.imread('images/32.jpg',0)

edges = cv2.Canny(img,150,200)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()
