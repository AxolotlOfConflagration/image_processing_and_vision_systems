import cv2

img = cv2.imread('put.png', 0)
cv2.imshow("img", img)

_, threshold = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
adapt_thresh_1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
adapt_thresh_2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
_, adapt_thresh_3 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow('normal threshold', threshold)
cv2.imshow('adaptive thresh mean', adapt_thresh_1)
cv2.imshow('adaptive thresh gaussian', adapt_thresh_2)
cv2.imshow('normal and otsu', adapt_thresh_3)

key = cv2.waitKey(0)
