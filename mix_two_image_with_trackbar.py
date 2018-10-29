import cv2 

def nothing1(x):
   pass

img = cv2.imread('qr.jpg')
img1 = cv2.resize(img, dsize=(313, 313), interpolation=cv2.INTER_LANCZOS4)
img2 = cv2.imread('logo.png')

cv2.namedWindow('image')

cv2.createTrackbar("alpha", 'image', 0, 10, nothing1)
cv2.createTrackbar("betha", 'image', 0, 10, nothing1)

while (1):

   k = cv2.waitKey(1) & 0xFF
   if k == 27:
       break

   a = cv2.getTrackbarPos("alpha", 'image')
   b = cv2.getTrackbarPos("betha", 'image')
   dst = cv2.addWeighted(img1, a/10, img2, b/10, 0)
   cv2.imshow('image', dst)


cv2.waitKey(0)
cv2.destroyAllWindows()