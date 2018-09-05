import os
import numpy as np
import datetime
from sklearn import metrics
import itertools 
import random
from collections import OrderedDict

def readMeasureData(measure1, measure2, structure, path_to_tables):
    print("Reading data: "+measure1+" "+measure2+" for "+structure)
    path = path_to_tables

    measure1_values = []
    measure2_values = []
    structures = []

    for filename in os.listdir(path):
        if structure in filename:
            structure2 = filename.split('$')[1]
            structures.append(structure2)
            with open(path+filename) as fp: 
                    line = fp.readline()
                    while line:
                        #isolar numa funçao
                        if measure1 in line:
                            v1 = float(str(line).split(' ')[1])
                            #print(v1)
                            measure1_values.append(v1)
                        if measure2 in line:  
                            v2 = float(str(line).split(' ')[1])
                            #print(v2)
                            measure2_values.append(v2)
                        line = fp.readline()

    dic = {}

    values = zip(measure1_values,measure2_values)
    #structures = str(structures).replace('.ent','')
    dic = dict(itertools.zip_longest(structures, values))

    #usar funcao
    dic = removeNoneValues(dic)    

    return dic, measure1_values, measure2_values

def readDataTable(path_to_tables, structure, measure1, measure2):
    path = path_to_tables+'table_'+structure+'_'+measure1+'_'+measure2
    print('Reading table data...')
    print(path)

    measure1_values = []
    measure2_values = []
    labels = []
    structures = []

    with open(path) as fp:
        line = fp.readline()
        while line:
            parsed = str(line).strip().split(' ')
            structures.append(parsed[0])
            measure1_values.append(float(parsed[1]))
            measure2_values.append(float(parsed[2]))
            labels.append(int(parsed[3]))
            line = fp.readline()

    dic = {}
    values = zip(measure1_values,measure2_values)
    dic = dict(itertools.zip_longest(structures, values))
    dic = removeNoneValues(dic)
 
    return dic, measure1_values, measure2_values, labels

def removeNoneValues(dic):
    dic = {k:v for k,v in dic.items() if v is not None}
    return dic

def getRandomElements(dic, n):
    dic2 = {}

    i = 0
    while i < n:
        key, value = random.choice(list(dic.items()))
        dic2[key] = value
        i += 1

    dic2 = {k:v for k,v in dic2.items() if v is not None}
    return dic2

def generateMeasureCombinations(measures):
    measures_copy = measures
    visited = []
    combinations = set()

    x = 0
    y = 0
    while x < len(measures):
        while y < len(measures_copy):
            if measures_copy[y] not in visited:
                line = measures[x]+' '+measures_copy[y]
                combinations.add(line)
            y += 1 
        visited.append(measures[x])      
        x += 1         
        y = 0
    
    combinations = list(combinations)
    return combinations

def getClassificationsNumber(true_labels):
    unique_labels = set(true_labels)
    return len(unique_labels)

def saveResultsToFile(structure, algorithm, parameters, data, measure1, measure2, metrics, path_res):
    print('Saving results...')
    data2 = OrderedDict(sorted(data.items(), key=lambda x: x[0]))

    path = path_res+'/'+structure+'/'
    if not os.path.exists(path):
        os.makedirs(path)

    with open(path+structure+'_'+measure1+'_'+measure2+'_'+algorithm+'_'+str(parameters), 'w') as file:
        file.write('# ####################################################\n')
        file.write('Structure: '+structure+'\n')
        file.write('\n')
        file.write('# ####################################################\n')
        file.write('Algorithm: '+algorithm+'\n')
        file.write('\n')
        file.write('# ####################################################\n')
        file.write('Parameters: '+str(parameters).replace('_',' ')+'\n')
        file.write('\n')
        file.write('# ####################################################\n')
        file.write('Measures: '+measure1+' '+measure2+'\n')
        file.write('\n')
        file.write('# ####################################################\n')
        file.write('# Cluster evaluation: \n')
        file.write('Homogeneity: %0.3f \n' % metrics[0])
        file.write('Completeness: %0.3f \n' % metrics[1])
        file.write('V-measure: %0.3f \n' % metrics[2])
        file.write('Adjusted Rand Index: %0.3f \n' % metrics[3])
        file.write('Adjusted Mutual Information: %0.3f \n' % metrics[4])
        file.write('Silhouette coefficient: %0.3f \n' % metrics[5])
        file.write('Calinksi-Harabaz: %0.3f \n' % metrics[6])
        file.write('\n')
        file.write('# ####################################################\n')
        file.write('# pdb | cath | '+measure1+' | '+measure2+' | label\n')
        for value in data2.values():
            file.write('{}\n'.format(value))

def saveResultsToFileNoLabels(structure, algorithm, parameters, measure1, measure2, metrics, path_res):
    print('Saving results...')

    path = path_res+'/'+structure+'/'
    if not os.path.exists(path):
        os.makedirs(path)

    with open(path+structure+'_'+measure1+'_'+measure2+'_'+algorithm+'_'+str(parameters), 'w') as file:
        file.write('# ####################################################\n')
        file.write('Structure: '+structure+'\n')
        file.write('\n')
        file.write('# ####################################################\n')
        file.write('Algorithm: '+algorithm+'\n')
        file.write('\n')
        file.write('# ####################################################\n')
        file.write('Parameters: '+str(parameters).replace('_',' ')+'\n')
        file.write('\n')
        file.write('# ####################################################\n')
        file.write('Measures: '+measure1+' '+measure2+'\n')
        file.write('\n')
        file.write('# ####################################################\n')
        file.write('# Cluster evaluation: \n')
        file.write('Calinksi-Harabaz: %0.3f \n' % metrics[0])
        file.write('Silhouette coefficient: %0.3f \n' % metrics[1])
        file.write('\n')

def clusterEvaluation(X, labels, labels_true):
    values = []
    values.append(metrics.homogeneity_score(labels_true, labels))
    values.append(metrics.completeness_score(labels_true, labels))
    values.append(metrics.v_measure_score(labels_true, labels))
    values.append(metrics.adjusted_rand_score(labels_true, labels))
    values.append(metrics.adjusted_mutual_info_score(labels_true, labels))
    values.append(metrics.silhouette_score(X, labels, metric='sqeuclidean'))
    values.append(metrics.calinski_harabaz_score(X, labels))
    return values

def clusterEvaluationNoLabels(X, labels):
    values = []
    values.append(metrics.calinski_harabaz_score(X, labels))
    values.append(metrics.silhouette_score(X, labels, metric='sqeuclidean'))
    return values

def saveImage(plt, path, name):
    plt.savefig(path+name+'.png',format='png',bbox_inches='tight',dpi = 200)
    plt.cla() # Clear axis
    plt.clf() # Clear figure
    plt.close() # Close figure window