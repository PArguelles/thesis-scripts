import os 
from sklearn import metrics
from collections import OrderedDict

def readTargetSummary(model):

    path_to_file = "C:/ShareSSD/casp/summaries/"

    gdt_ts = []
    gdt_ha = []
    rmsd = []
    tmscore = []
    models = []

    with open(path_to_file+model+'.txt','r') as fp:
        line = fp.readline() #skip first line
        line = fp.readline()
        while line: 
            if not str(line).isspace():
                models.append(str(line).split()[1])
                gdt_ts.append(float(str(line).split()[3]))
                gdt_ha.append(float(str(line).split()[10]))
                rmsd.append(float(str(line).split()[14]))
                tmscore.append(float(str(line).split()[45]))
         
            line = fp.readline()

    return models, gdt_ha, gdt_ts, rmsd, tmscore


 
