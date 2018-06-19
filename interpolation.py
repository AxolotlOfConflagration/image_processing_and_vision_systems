import cv2

img = cv2.imread('1.jpg')
cv2.imshow('img', img)

img_scale_nearset = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_NEAREST)
img_scale_linear = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
img_scale_cubic = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
img_scale_lanczos4 = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LANCZOS4)

cv2.imshow('Nearset scaled image ', img_scale_nearset)
cv2.imshow('Linear scaled image ', img_scale_linear)
cv2.imshow('Cubic scaled image ', img_scale_cubic)
cv2.imshow('Lanczos4 scaled image ', img_scale_lanczos4)

key = cv2.waitKey(0)
