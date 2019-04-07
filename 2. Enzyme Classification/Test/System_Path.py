from os.path import *
Path = 'D:\\Dataset\\Test\\Test.jpg'

a = exists(Path)

from PIL import Image
img = Image.open(Path)
print(img)

import cv2 as cv
img = cv.imread(Path, cv.IMREAD_COLOR)
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()
