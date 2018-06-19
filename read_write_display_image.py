import cv2

img_c = cv2.imread('flaming.jpeg', cv2.IMREAD_COLOR)
img_g = cv2.imread('flaming.jpeg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('flaming color', img_c)
cv2.imshow('flaming gray', img_g)
key = cv2.waitKey(0)
if key == 27:
   cv2.destroyAllWindows()
elif key == ord('s'):
   cv2.imwrite('flaming_gray.jpg', img_g)
   cv2.destroyAllWindows()
