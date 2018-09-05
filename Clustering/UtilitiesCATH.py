import os
import numpy as np
import datetime
from sklearn import metrics
import itertools 
from collections import OrderedDict

# read file with cath classifications and returns result as a dictionary
def readCATHNames(input_structure):
    print('Fetching random sample')
    cath_names_path = "D:/Dados/cath/cath-classification-data/cath-names.txt"
    id_map = {}

    with open(cath_names_path) as fp:
        line = fp.readline()
        while line:
            if '#' not in line:
                id_map[str(line).split()[1]] = str(line).split()[0]
            line = fp.readline()   

    return(id_map)
    
def readChainFiles(input_structure):
    print('Fetching random sample')
    cath_names_path = "D:/Dados/cath/cath-classification-data/cath-chain-list.txt"
    id_map = {}
    names = set()

    with open(cath_names_path) as fp:
        line = fp.readline()
        while line:
            if '#' not in line:
                id_map[str(line).split()[0]] = str(line).split()[1]
                names.add(str(line).split()[0])
                print(line)
            line = fp.readline()   

    print(len(names))
    return(id_map)

# intersects the keys of both maps in order to extract entries which have
# a CATH classification    
def intersectCATHKeys(cath_names, measure_data):
    data = {}
    for pdb_id in cath_names.keys():
        if pdb_id in measure_data.keys():
            data[pdb_id] = []
            data[pdb_id].append(pdb_id)
            data[pdb_id].append(cath_names[pdb_id])
            data[pdb_id].append(measure_data[pdb_id][0])
            data[pdb_id].append(measure_data[pdb_id][1])
            data[pdb_id].append(cath_names[pdb_id][0][0])

    return data        

# splits the intersected dictionary into lists
def splitCATHTuples(data):
    pdb = []
    cath = []
    measure1 = []
    measure2 = []
    true_labels = []

    for pdb_id in data.keys():
        pdb.append(data[pdb_id][0])
        cath.append(data[pdb_id][1])
        measure1.append(data[pdb_id][2])
        measure2.append(data[pdb_id][3])
        true_labels.append(str(data[pdb_id][1].split('.')[3]))   

    return pdb, cath, measure1, measure2, true_labels    

