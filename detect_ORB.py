import cv2
import matplotlib.pyplot as plt
img1 = cv2.imread('box.png', 0)
img2 = cv2.imread('box2.png', 0)

# initiate detector
orb = cv2.ORB_create()

# find the keypoints and descriptors with ORB
keyp1, des1 = orb.detectAndCompute(img1, None)
keyp2, des2 = orb.detectAndCompute(img2, None)

# create BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Match descriptors
matches = bf.match(des1, des2)

# Sort them in the order of theri distance
matches = sorted(matches, key=lambda x: x.distance)

# Draw first 20 matchers
img3 = cv2.drawMatches(img1, keyp1, img2, keyp2, matches[:20], flags=2, outImg=None)

plt.imshow(img3)
plt.show()