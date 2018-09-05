import numpy as np
from scipy import ndimage as ndi
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import matplotlib.image as mpimg
from skimage import data
from skimage import color
from skimage.util import view_as_blocks


# get astronaut from skimage.data in grayscale
l = color.rgb2gray(data.astronaut())

# size of blocks
block_shape = (4, 4)

# see astronaut as a matrix of blocks (of shape block_shape)
view = view_as_blocks(l, block_shape)

# collapse the last two dimensions in one
flatten_view = view.reshape(view.shape[0], view.shape[1], -1)

# resampling the image by taking either the `mean`,
# the `max` or the `median` value of each blocks.
mean_view = np.mean(flatten_view, axis=2)
max_view = np.max(flatten_view, axis=2)
median_view = np.median(flatten_view, axis=2)

# display resampled images
fig, axes = plt.subplots(3, 5, figsize=(20, 20), sharex=True, sharey=True)
ax = axes.ravel()

l_resized = ndi.zoom(l, 2, order=3)

img = mpimg.imread('C:/ShareSSD/tests/plot_T0859_GDT-HA_GDT-TS_km_3.png')

i = 0
while i < 15:
    ax[i].imshow(img, interpolation='nearest', cmap=cm.Greys_r)
    i += 1


for a in ax:
    a.set_axis_off()

fig.tight_layout()
plt.show()