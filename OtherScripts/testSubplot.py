import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import os

def loadImages():

    plots = []

    path = 'C:/ShareSSD/tests/'
    for filename in os.listdir(path):
        if 'plot_' in filename:
            print(filename)
            plots.append(mpimg.imread(path+filename))

    return plots

def createSubplot(plots):
    fig = plt.figure(figsize=(20, 10))

    i = 1

    #casp 
    #scop 3,5
    while i < len(plots):
        a=fig.add_subplot(3,3,i)
        a.set_axis_off()
        plt.imshow(plots[i-1],aspect='equal')
        i += 1

    fig.tight_layout()
    plt.tight_layout()
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=-0.7, hspace=-0.02)
    plt.show()

createSubplot(loadImages())


            

