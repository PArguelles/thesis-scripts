import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img1 = mpimg.imread('D:/Dados/plots/plot_T0859_GDT-HA_GDT-TS_km_5.png')
img2 = mpimg.imread('D:/Dados/plots/plot_T0859_GDT-HA_TM-score_agg_average_10.png')
img3 = mpimg.imread('D:/Dados/plots/plot_T0859_GDT-HA_GDT-TS_km_5.png')
img4 = mpimg.imread('D:/Dados/plots/plot_T0859_GDT-HA_TM-score_agg_average_10.png')
img5 = mpimg.imread('D:/Dados/plots/plot_T0859_GDT-HA_GDT-TS_km_5.png')
img6 = mpimg.imread('D:/Dados/plots/plot_T0859_GDT-HA_TM-score_agg_average_10.png')

imgs = [img1,img2,img3,img4]

nrows = 5
ncols = 3

f, axarr = plt.subplots(nrows,ncols)

axarr[0,0].imshow(img1)
axarr[0,0].axis('off')

axarr[0,1].imshow(img2)
axarr[0,1].axis('off')

axarr[0,2].imshow(img3)
axarr[0,2].axis('off')

axarr[1,0].imshow(img4)
axarr[1,0].axis('off')

axarr[1,1].imshow(img1)
axarr[1,1].axis('off')

axarr[1,2].imshow(img1)
axarr[1,2].axis('off')

axarr[2,0].imshow(img1)
axarr[2,0].axis('off')

axarr[2,1].imshow(img1)
axarr[2,1].axis('off')

axarr[2,2].imshow(img1)
axarr[2,2].axis('off')

axarr[3,0].imshow(img1)
axarr[3,0].axis('off')

axarr[3,1].imshow(img1)
axarr[3,1].axis('off')

axarr[3,2].imshow(img1)
axarr[3,2].axis('off')

axarr[4,0].imshow(img1)
axarr[4,0].axis('off')

axarr[4,1].imshow(img1)
axarr[4,1].axis('off')

axarr[4,2].imshow(img1)
axarr[4,2].axis('off')


plt.subplots_adjust(bottom=0.1, right=0.8, top=0.9)

f.tight_layout()
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
plt.show()