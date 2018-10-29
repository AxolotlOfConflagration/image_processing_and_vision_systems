import cv2

img = cv2.imread('img.png', cv2.IMREAD_COLOR)
b, g, r = cv2.split(img)
key = ord('a')
while key != ord('q'):
   cv2.imshow('blue', b)
   cv2.imshow('red', r)
   cv2.imshow('green', g)
   key = cv2.waitKey(30)
cv2.destroyAllWindows()