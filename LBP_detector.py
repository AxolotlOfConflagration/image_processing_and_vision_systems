import cv2
from skimage.feature import local_binary_pattern
img = cv2.imread('2.jpeg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
radius = 1
n_points = 4 * radius

lbp = local_binary_pattern(img_gray, n_points, radius, 'default')
cv2.imshow('new', lbp)
key = cv2.waitKey(0)