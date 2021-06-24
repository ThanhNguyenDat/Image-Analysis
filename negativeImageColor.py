import cv2
import numpy as np

def NegativeColor(imageIn, imageOut):
    M, N, P = imageIn.shape
    for x in range(0, M):
        for y in range(0, N):
            r = imageIn[x, y, 2]
            g = imageIn[x, y, 1]
            b = imageIn[x, y, 0]
            imageOut[x, y, 2] = L - 1 - r
            imageOut[x, y, 1] = L - 1 - g
            imageOut[x, y, 0] = L - 1 - b
    return
  
path = ''
imgin = cv2.imread(path , cv2.IMREAD_COLOR)
imgout = np.zeros(imgin.shape, np.uint8)
c3.NegativeColor(imageIn=imgin, imageOut=imgout)
cv2.imshow("Negative Image Color", imgout)
cv2.waitKey(0)
