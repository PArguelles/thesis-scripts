import os
import numpy as np
import datetime
from sklearn import metrics
import itertools 
import random
from collections import OrderedDict
import UtilitiesCommon as util

# read file with classifications and returns result as a dictionary
def readSCOPNames(input_structure):
    print('Fetching random sample')
    scop_names_path = "D:/Dados/scop/scope/dir.cla.scope.2.07-stable.txt"
    id_map = {}

    input_structure = input_structure.replace('.ent','')

    with open(scop_names_path) as fp:
        line = fp.readline()
        while line:
            #class, fold, superfamiliy, family
            pdb_id = str(line).strip().split('\t')[0]+'.ent'
            superfamily = str(line).strip().split("\t")[3].split('.')[2]

            #make sure the input structure information is in the final dictionary
            if input_structure in pdb_id:
                key = pdb_id
                value = superfamily

            id_map[pdb_id] = superfamily
            line = fp.readline()   

    #id_map = util.getRandomElements(id_map, 10000)
    id_map[key] = value

    return(id_map)

# intersects the keys of both maps in order to extract entries which have
# a classification    
def intersectSCOPKeys(scop_names, measure_data):

    measure_data = util.removeNoneValues(measure_data)
    scop_names = util.removeNoneValues(scop_names)

    data = {}
    for pdb_id in scop_names.keys():
        if pdb_id in measure_data.keys():
            data[pdb_id] = []
            data[pdb_id].append(pdb_id)
            data[pdb_id].append(scop_names[pdb_id])
            data[pdb_id].append(measure_data[pdb_id][0])
            data[pdb_id].append(measure_data[pdb_id][1])
      
    return data        

def splitSCOPTuples(data):
    pdb = []
    measure1 = []
    measure2 = []
    true_labels = []

    print(data)

    for pdb_id in data.keys():
        pdb.append(data[pdb_id][0])
        measure1.append(data[pdb_id][2])
        measure2.append(data[pdb_id][3])
        true_labels.append(data[pdb_id][1])   
        
    return pdb, measure1, measure2, true_labels    

