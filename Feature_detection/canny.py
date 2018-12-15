import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = plt.imread('mars_rocks.jpg',0)
edges = cv.Canny(img,100,200)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
cv.imwrite('canny_mars_rocks.jpg',edges)
