import cv2
from pylab import rcParams
rcParams['figure.figsize'] = 8, 4

path = ''
img = cv2.imread(path)

color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()
