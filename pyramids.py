import cv2
import numpy as np
import matplotlib.pylab as plt
import scipy.misc as misc

'''
实现上述效果的步骤如下:
1. 读入两幅图像,苹果和句子
2. 构建苹果和橘子的高斯金字塔(6 层)
3. 根据高斯金字塔计算拉普拉斯金字塔
4. 在拉普拉斯的每一层进行图像融合(苹果的左边与橘子的右边融合)
5. 根据融合后的图像金字塔重建原始图像。
'''
A = cv2.imread('images/apple.jpg')
B = cv2.imread('images/orange.jpg')

# 分开进行计算
def separately(A, B):
        
    # generate Gaussian pyramid for A
    G = A.copy()
    gpA = [G]
    for i in range(6):
        G = cv2.pyrDown(G)
        gpA.append(G)
    # generate Gaussian pyramid for B
    G = B.copy()
    gpB = [G]
    for i in range(6):
        G = cv2.pyrDown(G)
        gpB.append(G)
    # generate Laplacian Pyramid for A
    lpA = [gpA[6]]
    for i in range(6,0,-1):
        GE = cv2.pyrUp(gpA[i])
        L = cv2.subtract(gpA[i-1],GE)
        lpA.append(L)
    # generate Laplacian Pyramid for B
    lpB = [gpB[6]]
    for i in range(6,0,-1):
        GE = cv2.pyrUp(gpB[i])
        L = cv2.subtract(gpB[i-1],GE)
        lpB.append(L)
    # Now add left and right halves of images in each level
    #numpy.hstack(tup)
    #Take a sequence of arrays and stack them horizontally
    #to make a single array.
    LS = []
    for la,lb in zip(lpA,lpB):
        rows,cols,dpt = la.shape
        ls = np.hstack((la[:,0:int(cols/2)], lb[:,int(cols/2):]))
        LS.append(ls)
    # now reconstruct
    ls_ = LS[0]
    for i in range(1,7):
        ls_ = cv2.pyrUp(ls_)
        ls_ = cv2.add(ls_, LS[i])
    # image with direct connecting each half
    real = np.hstack((A[:,:int(cols/2)],B[:,int(cols/2):]))
    #cv2.imwrite('Pyramid_blending2.jpg',ls_)
    #cv2.imwrite('Direct_blending.jpg',real)
    
    return real, ls_

def improve(imgA, imgB):
    gA=[imgA]
    lpA=[]
    gB=[imgB]
    lpB=[]
    DEPTH=6
    for i in range(DEPTH):
      tempA1 = cv2.pyrDown(gA[i])
      tempB1 = cv2.pyrDown(gB[i])
      
      gA.append(tempA1)
      gB.append(tempB1)
      
      lA = cv2.subtract(gA[i] ,cv2.pyrUp(tempA1))
      lB = cv2.subtract(gB[i] ,cv2.pyrUp(tempB1))
      
      lpA.append(lA)
      lpB.append(lB)
    lpA.append(gA[-1])
    lpB.append(gB[-1])
    
    lpAB = []#将拉布拉斯金字塔的每一层拼接起来
    for la,lb in zip(lpA,lpB):
      rows,cols,dpt = la.shape
      ls = np.hstack((la[:,0:cols//2], lb[:,cols//2:]))
      lpAB.append(ls)
      
    tempA2 =lpAB[-1]
    for i in range(DEPTH,0,-1):
      tempA2 = cv2.pyrUp(tempA2)
      tempA2 = cv2.add(tempA2,lpAB[i-1])
      
    return tempA2


if __name__ == '__main__':
    real = improve(A, B)

    cv2.imshow('result.jpg', real)
#    cv2.imshow('result1.jpg', ls_)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    cv2.waitKey(1)
    cv2.waitKey(1)
    cv2.waitKey(1)
