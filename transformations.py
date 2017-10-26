import cv2
import numpy as np
import matplotlib.pylab as plt
import scipy.misc as misc

img = cv2.imread('images/33.jpg')
rows, cols = img.shape[:2]

def weighted():
    # the two images must be same size
    img1 = cv2.imread('images/31.jpg')
    img2 = cv2.imread('images/32.jpg')
    dst = cv2.addWeighted(img1,0.3,img2,0.7,0)
    return dst

def scaling(img):
    '''
    cv2.INTER_AREA for shrinking and cv2.INTER_CUBIC (slow) & cv2.INTER_LINEAR for zooming.
    By default, interpolation method used is cv2.INTER_LINEAR for all resizing purposes. 
    '''
#    res = cv2.resize(img,(2*h,2*w),interpolation=cv2.INTER_CUBIC)
    res = cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
    return res

def translation(img):
    # moving (100,50),
    # Remember width = number of columns, and height = number of rows
    M = np.float32([[1,0,100],[0,1,50]])
    dst = cv2.warpAffine(img,M,(rows,cols))
    return dst

def rotation(img):
#    center,angle,scaling, 长方形旋转后会有损失
#    M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
#    dst = cv2.warpAffine(img,M,(cols,rows))
    # 这种方法针对长方形图像，旋转之后不会有遮挡
    M = np.float32([[0,1,0],[-1,0,cols]])
    dst = cv2.warpAffine(img,M,(rows,cols))
    return dst

def affine(img):
    pts1 = np.float32([[50,50],[200,50],[50,200]])
    pts2 = np.float32([[10,100],[200,50],[100,250]])
    M = cv2.getAffineTransform(pts1,pts2)       #2*2
    dst = cv2.warpAffine(img,M,(cols,rows))
    return dst
    
def perspective(img):
    pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
    pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
    M = cv2.getPerspectiveTransform(pts1,pts2)  #3*3
    dst = cv2.warpPerspective(img,M,(cols,rows))
    return dst,M


if __name__ == '__main__':
    dst,M = perspective(img)


    cv2.imshow('result.jpg', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    cv2.waitKey(1)
    cv2.waitKey(1)
    cv2.waitKey(1)
