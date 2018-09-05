import numpy as np
import matplotlib.pyplot as plt
import os
import UtilitiesCommon as util

# ##################
# CATH
# ##################
#structures = ['1c4zA02','1xfjA00','2asfA00','2evvA00','2vxzA01','3bfmA01','3bpkA01','3hisA02','4kp1A01']
#path_to_results = "D:/Dados/cath/clustering_results/"
#path_to_tables = "D:/Dados/cath/dompdb_tmscore_table/table_"

# ##################
# CASP
# ##################
#structures = ['T0859','T0860','T0861','T0862','T0863','T0864','T0865','T0866','T0867']

path_to_results = "D:/Dados/casp12/clustering_results/"
path_to_tables = "D:/Dados/casp12/tmscore_table/table_"

# append cluster evaluation to the end of the file

algorithm_list = ['fcm_2','fcm_4']

models = []
values1 = []
values2 = []
labels = []

for algorithm in algorithm_list:
    for folder in os.listdir(path_to_results):
        current_folder = path_to_results+folder
        for filename in os.listdir(current_folder):

            # ################################################
            # Go through each file that contains fcm or snn results    
            if "plot" not in filename and algorithm in filename:
                print(filename)
                parsed = str(filename).split("_")
                structure = parsed[0]
                measure1 = parsed[1]
                measure2 = parsed[2]

                # open corresponding table and load data
                with open(path_to_tables+structure+'_'+measure1+'_'+measure2) as fp:
                    line = fp.readline()
                    while line: 
                        data = str(line).strip().split(' ')
                        models.append(data[0])
                        values1.append(data[1])
                        values2.append(data[2])
                        line = fp.readline()

                if 'snn' in algorithm:
                    # read clustering labels for snn files
                    with open(path_to_results+structure+'/'+filename,'r') as cr:
                        line = cr.readline()
                        while line: 
                            if "$cluster" in line:
                                line = cr.readline()
                                while not str(line).isspace():
                                    values = str(line).rstrip().split()
                                    for v in values:
                                        if '[' not in str(v):
                                            labels.append(int(v))
                                    line = cr.readline()
                            line = cr.readline()

                elif 'fcm' in algorithm:
                    # read clustering labels for fcm files
                    with open(path_to_results+structure+'/'+filename,'r') as cr:        
                        line = cr.readline()
                        while line: 
                            if "$cluster" in line:
                                line = cr.readline() #skip one
                                line = cr.readline()
                                while not str(line).isspace() and '$csize' not in line:
                                    values = str(line).rstrip().split()
                                    print(values)
                                    for v in values:
                                        labels.append(int(v))
                                    line = cr.readline()
                                    line = cr.readline()
                            line = cr.readline()

                tmp = list(zip(values1, values2))        
                X = np.array(tmp)
                X = np.array(X).astype(np.float)
                ce = util.clusterEvaluationNoLabels(X,labels)

                with open(path_to_results+structure+'/'+filename, "a") as ap:
                    ap.write('\n')
                    ap.write('# Cluster evaluation: \n')
                    ap.write('Calinksi-Harabaz: %0.3f \n' % ce[0])
                    ap.write('Silhouette coefficient: %0.3f \n' % ce[1])

            # Clear lists
            models = []
            values1 = []
            values2 = []
            labels = []




      
              
