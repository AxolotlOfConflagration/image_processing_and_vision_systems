import cv2

def nothing_(x):
   pass
img = cv2.imread('put.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.namedWindow('image')


cv2.createTrackbar("Type", 'image',0,5,nothing_)
cv2.createTrackbar("Number 1", 'image', 0,255, nothing_)
cv2.createTrackbar("Number 2", 'image', 0, 255, nothing_)


while(1):

   k = cv2.waitKey(1) & 0xFF
   if k == 27:
       break


   i_1 = cv2.getTrackbarPos('Number 1', 'image')
   i_2 =  cv2.getTrackbarPos('Number 2', 'image')
   t = cv2.getTrackbarPos("Type", 'image')
   if t == 0:
       img2 = img

   if t == 1:
       ret, thresh1 = cv2.threshold(img, i_1, i_2, cv2.THRESH_BINARY)
       img2 = thresh1
   if t == 2:
       ret, thresh2 = cv2.threshold(img, i_1, i_2,cv2.THRESH_BINARY_INV)
       img2 = thresh2
   if t == 3:
       ret, thresh3 = cv2.threshold(img, i_1, i_2, cv2.THRESH_TRUNC)
       img2= thresh3
   if t == 4:
       ret, thresh4 = cv2.threshold(img, i_1, i_2,cv2.THRESH_TOZERO)

       img2 = thresh4
   if t == 5:
       ret, thresh5 = cv2.threshold(img, i_1, i_2,cv2.THRESH_TOZERO_INV)
       img2= thresh5
   cv2.imshow('image', img2)



cv2.waitKey(0)
cv2.destroyAllWindows()
