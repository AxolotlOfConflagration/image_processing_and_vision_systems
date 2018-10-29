import matplotlib.pyplot as plt
from skimage.feature import hog
from skimage import data
from skimage import color
from skimage import exposure

img = color.rgb2gray(data.astronaut())

_, hog_image = hog(img, orientations=8, pixels_per_cell=(16, 16),cells_per_block=(1, 1), visualise=True)


fig, (ax1, ax2) = plt.subplots(1, 2)
#fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4), sharex=True, sharey=True)

fig.suptitle('Descriptor HoG')

ax1.axis('off')
ax1.imshow(img, cmap=plt.cm.gray)
ax1.set_title('Women Input')

#Rescale histogram for better display
hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 10))

ax2.axis('off')
ax2.imshow(hog_image_rescaled, cmap=plt.cm.gray)
ax2.set_adjustable('box-forced')
ax2.set_title('Historam of Oriented Gradzients')

plt.show()