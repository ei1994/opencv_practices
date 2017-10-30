import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('images/33.jpg',0)
f = np.fft.fft2(img)  #傅里叶变换得到频谱，一般来说，低频分量模值最大
fshift = np.fft.fftshift(f)#平移频谱到图像中央
# 将频谱转换成db
magnitude_spectrum = 20*np.log(np.abs(fshift))
plt.subplot(321),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(322),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])


rows, cols = img.shape
crow,ccol = rows//2 , cols//2
#设计一个高通滤波器对应0, 低频对应1
fshift[crow-30:crow+30, ccol-30:ccol+30] = 0
#平移逆变换
f_ishift = np.fft.ifftshift(fshift)
#傅里叶反变换
img_back = np.fft.ifft2(f_ishift)
# 取绝对值
img_back = np.abs(img_back)
plt.subplot(323),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(324),plt.imshow(img_back, cmap = 'gray')
plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
plt.subplot(325),plt.imshow(img_back)
plt.title('Result in JET'), plt.xticks([]), plt.yticks([])
plt.show()

# fft in cv2
dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()
