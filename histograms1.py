import cv2
import numpy as np
import matplotlib.pyplot as plt

'''
cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
1. images: 原图像(图像格式为 uint8 或 float32)。当传入函数时应该
用中括号 [] 括起来,例如:[img]。
2. channels: 同样需要用中括号括起来,它会告诉函数我们要统计那幅图
像的直方图。如果输入图像是灰度图,它的值就是 [0];如果是彩色图像
的话,传入的参数可以是 [0],[1],[2] 它们分别对应着通道 B,G,R。
3. mask: 掩模图像。要统计整幅图像的直方图就把它设为 None。但是如
果你想统计图像某一部分的直方图的话,你就需要制作一个掩模图像,并
使用它。
(后边有例子)
4. histSize:BIN 的数目。也应该用中括号括起来,例如:[256]。
5. ranges: 像素值范围,通常为 [0,256]
'''

img = cv2.imread('images/33.jpg',0)
hist = cv2.calcHist([img],[0],None,[256],[0,256])
'''
 can instead of calcHist() function
 OpenCV function is more faster than (around 40X) than np.histogram().
 So stick with OpenCV function.
 '''
#hist,bins = np.histogram(img.ravel(),256,[0,256])

plt.plot(hist,'r')
plt.xlim([0,256])
plt.show()

# 直接使用plt绘制直方图
#plt.hist(img.ravel(),256,[0,256])
#plt.show()

# 使用掩模
# create a mask
# create a mask image with white color
# on the region you want to find histogram and black otherwise.
mask = np.zeros(img.shape[:2], np.uint8)
mask[100:300, 100:400] = 255
masked_img = cv2.bitwise_and(img,img,mask = mask)

# Calculate histogram with mask and without mask
# Check third argument for mask
hist_full = cv2.calcHist([img],[0],None,[256],[0,256])
hist_mask = cv2.calcHist([img],[0],mask,[256],[0,256])

plt.subplot(221), plt.imshow(img, 'gray')
plt.subplot(222), plt.imshow(mask,'gray')
plt.subplot(223), plt.imshow(masked_img, 'gray')
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
plt.xlim([0,256])
plt.show()
