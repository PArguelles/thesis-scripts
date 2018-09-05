import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

#scop

img = mpimg.imread('D:/Dados/plots/plot_T0859_GDT-HA_GDT-TS_km_5.png')

fig = plt.figure(figsize=(45, 25))

fig.subplots_adjust(left=0.03, right=0.97, hspace=1, wspace=1)

a=fig.add_subplot(3,5,1)
a.set_axis_off()
imgplot = plt.imshow(img,aspect='equal')

a=fig.add_subplot(3,5,2)
a.set_axis_off()
imgplot = plt.imshow(img,aspect='equal')

a=fig.add_subplot(3,5,3)
a.set_axis_off()
imgplot = plt.imshow(img,aspect='equal')

a=fig.add_subplot(3,5,4)
a.set_axis_off()
imgplot = plt.imshow(img,aspect='equal')

a=fig.add_subplot(3,5,5)
a.set_axis_off()
imgplot = plt.imshow(img,aspect='equal')

a=fig.add_subplot(3,5,6)
a.set_axis_off()
imgplot = plt.imshow(img,aspect='equal')

a=fig.add_subplot(3,5,7)
a.set_axis_off()
imgplot = plt.imshow(img,aspect='equal')

a=fig.add_subplot(3,5,8)
a.set_axis_off()
imgplot = plt.imshow(img,aspect='equal')

a=fig.add_subplot(3,5,9)
a.set_axis_off()
imgplot = plt.imshow(img,aspect='equal')

a=fig.add_subplot(3,5,10)
a.set_axis_off()
imgplot = plt.imshow(img,aspect='equal')

a=fig.add_subplot(3,5,11)
a.set_axis_off()
imgplot = plt.imshow(img,aspect='equal')

a=fig.add_subplot(3,5,12)
a.set_axis_off()
imgplot = plt.imshow(img,aspect='equal')

a=fig.add_subplot(3,5,13)
a.set_axis_off()
imgplot = plt.imshow(img,aspect='equal')

a=fig.add_subplot(3,5,14)
a.set_axis_off()
imgplot = plt.imshow(img,aspect='equal')

a=fig.add_subplot(3,5,15)
a.set_axis_off()
imgplot = plt.imshow(img,aspect='equal')

fig.tight_layout()
plt.tight_layout()
plt.show()