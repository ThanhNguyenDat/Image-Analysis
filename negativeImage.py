import cv2

def Negative(imageIn):
    Height, Weight = imageIn.shape
    for x in range(0, Height):
        for y in range(0, Weight):
            r = imageIn[x, y]
            s = L - 1 - r
            imageOut[x, y] = s
    return imageOut
  
  path = ''
  img = cv2.imread(path)
  roi = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  roi = Negative(roi)
  cv2.imshow("Negative", roi)
  cv2.waitKey(0)
  
