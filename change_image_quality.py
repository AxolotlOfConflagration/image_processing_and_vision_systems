import cv2

alfa = 1.5
beta = -40.0
img = cv2.imread("1.jpg")
cv2.imshow("Old image", img)

img = img.astype('int32')
img_new = alfa * img + beta
img_new = np.clip(img_new, 0, 255)
img_new = img_new.astype('uint8')

cv2.imshow("New img", img_new)
key = cv2.waitKey(0)
