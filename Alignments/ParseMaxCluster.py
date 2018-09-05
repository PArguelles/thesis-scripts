import os
import re

path = 'C:/ShareSSD/scop/maxcluster_filtered/'
path_to_summaries = 'C:/ShareSSD/scop/maxcluster_summaries/'

def startSummaries():

    #start with gdt_2 files

    for filename in os.listdir(path):
        print(filename)
        if 'gdt_2' in filename:

            with open(path+filename,'r') as fp:

                line = fp.readline()
                while line:
                    if 'RMSD' in line:
                        parsed = re.findall(r"[-+]?\d*\.\d+|\d+", line)
                        rmsd = parsed[5]
                        maxsub = parsed[3]
                        tmscore = parsed[6]

                    #gdt-ha
                    if 'GDT' in line:
                        for n in line.split():
                            try:                                   
                                gdt = float(n)
                            except ValueError:
                                pass

                    line = fp.readline()

            new_name = str(filename).replace('gdt_2','summary')

            with open(path_to_summaries+new_name,'w') as nf:
                nf.write('RMSD= '+rmsd+'\n')
                nf.write('MaxSub= '+maxsub+'\n')
                nf.write('TM-score= '+tmscore+'\n')
                nf.write('GDT-HA= '+str(gdt)+'\n')

    appendGDTTS()

def appendGDTTS():

    for filename in os.listdir(path):
        print(filename)
        if 'gdt_4' in filename:

            parsed = str(filename).split('_')

            structure1 = parsed[0]
            if '.ent' not in structure1:
                structure1 = structure1+'_.ent'
            structure2 = parsed[2]
            if '.ent' not in structure2:
                structure2 = structure2+'_.ent'

            print(structure1)
            print(structure2)

            with open(path+filename) as fp:
                line = fp.readline()
                while line:
                    if 'GDT' in line:
                        for n in line.split():
                            try:                                   
                                gdt = float(n)
                            except ValueError:
                                pass

                    line = fp.readline()

            summary_name = structure1+'_'+structure2+'_summary'

            with open(path_to_summaries+summary_name,'a') as nf:
                nf.write('GDT-TS= '+str(gdt)+'\n')

startSummaries()               

