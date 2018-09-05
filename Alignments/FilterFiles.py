import os
import shutil

# isolate files that contain valid MaxCluster results
def extractValidResults():
    path = 'C:/ShareSSD/scop/maxcluster_indep/'
    new_path = 'C:/ShareSSD/scop/maxcluster_filtered/'

    count = 0

    for filename in os.listdir(path):

        count+=1
        with open(path+filename,'r') as fp:
            line = fp.readline()
            while line:
                print(line)
                if 'RMSD' in line:
                    shutil.copy2(path+filename, new_path+filename)
                    break
                line = fp.readline()
        print(count)

def removeHighRMSDAlignments():
    path = 'C:/ShareSSD/scop/maxcluster_summaries/'
    new_path = 'C:/ShareSSD/scop/maxcluster_summaries_delete/'

    for filename in os.listdir(path):
        print(filename)
        with open(path+filename,'r') as fp:
            line = fp.readline()
            while line:
                if 'RMSD' in line:
                    value = str(line).split(' ')[1]
                    if float(value) > 9:
                        shutil.copy2(path+filename, new_path+filename)
                        break
                line = fp.readline()

removeHighRMSDAlignments()