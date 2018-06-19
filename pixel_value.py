import cv2

img_c = cv2.imread('flaming.jpeg', cv2.IMREAD_COLOR)
img_g = cv2.imread('flaming.jpeg', cv2.IMREAD_GRAYSCALE)
pixel_c = img_c[220,270]
pixel_g = img_g[220,270]
print('Pixel color', pixel_c)
print('Shape color img ', img_c.shape)
print('Pixel grey', pixel_g)
print('Shape grey img ', img_g.shape)
