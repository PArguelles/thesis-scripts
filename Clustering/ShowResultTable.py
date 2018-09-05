import numpy as np
import matplotlib.pyplot as plt
import os
import re
import UtilitiesCommon as util

# ####################################################################
# SETUP VARIABLES
#path_to_results = "D:/Dados/cath/clustering_results/"
#structures = ['1c4zA02','1xfjA00','2asfA00','2evvA00','2vxzA01','3bpkA01','3hisA02','4kp1A01']
#
path_to_results = "D:/Dados/cath/clustering_results/"
structure = '3bpkA01'
algorithm = "km"
parameters = "5"
standard = "RMSD_RMSD"
# ####################################################################

data = []

labels = [] 
values = []

counter = 0
reference_value = 0

for folder in os.listdir(path_to_results):
    if structure in folder:
        path_to_results = path_to_results+folder+'/'
        for filename in os.listdir(path_to_results):
            if 'plot_' not in filename and algorithm in filename:
                if parameters in filename:
                    parsed = filename.split('_')
                    measure1 = parsed[1]
                    measure2 = parsed[2]
                    #label = measure1+' '+measure2+' '+algorithm
                    label = measure1+' '+measure2+' '+' '.join(parsed[3:])
                    labels.append(label)
                    with open(path_to_results+filename,'r') as fp:
                        line = fp.readline()
                        while line:
                            if 'Cluster evaluation' in line:
                                i = 0
                                #usar is space
                                while i < 7:
                                    line = fp.readline()
                                    num = [float(s) for s in re.findall(r'-?\d+\.?\d*', line)]
                                    values.append(num[0])
                                    i += 1
                                    print(line)   
                            line = fp.readline()
                        data.append(values)
                        values = []
                    if standard in filename:
                        reference_value = counter
                    else: counter += 1
         
print(reference_value)

columns = ('Homogeneity', 'Completeness', 'V-measure', 'ARI', 'AMI', 'Silhouette', 'Calinski-Harabasz')
rows = labels

plt.axis('off')

# Add a table at the bottom of the axes
the_table = plt.table(cellText=data,
                      rowLabels=rows,
                      rowColours=None,
                      colLabels=columns,
                      cellLoc='center',
                      loc='center')

ref = reference_value+1

#Color matrix
for i,j in the_table._cells:
    print(str(the_table._cells[(i, j)]._text.get_text()))
    if i > 0 and j > -1:
        if i == ref:
            the_table._cells[(i, j)]._text.set_color('blue')
        else:    
            if float(the_table._cells[(i, j)]._text.get_text()) > float(the_table._cells[(ref, j)]._text.get_text()):
                the_table._cells[(i, j)]._text.set_color('green')
            if float(the_table._cells[(i, j)]._text.get_text()) == float(the_table._cells[(ref, j)]._text.get_text()):
                the_table._cells[(i, j)]._text.set_color('black')
            if float(the_table._cells[(i, j)]._text.get_text()) < float(the_table._cells[(ref, j)]._text.get_text()):
                the_table._cells[(i, j)]._text.set_color('red')


#plt.title('Algorithm performance: '+algorithm+' '+parameters)
plt.savefig('D:/Dados/matrix.png', format='png', bbox_inches="tight", dpi=300)
#plt.show()
#util.saveImage(plt, path_to_results, 'matrix_'+structure)
