import cv2

i = 0
while 0xFF != ord('q'):
   img = cv2.imread(name, cv2.IMREAD_COLOR)
   cv2.imshow('1', img)
   if  cv2.waitKey(1) & 0xFF == ord('n'):
       if i < 3 :
           cv2.destroyAllWindows()
           i= i+1
       else:
           cv2.destroyAllWindows()
           i = 0
cv2.destroyAllWindows()
