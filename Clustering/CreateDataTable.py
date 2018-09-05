import UtilitiesCommon as util
import UtilitiesSCOP as scop
import UtilitiesCATH as cath

# SCOP
structures = ['d1a00d_.ent','d2dysn_.ent','d4qvqv_.ent']
measures = ['RMSD','GDT-HA','GDT-TS','TM-score','MaxSub']
path_to_tables = 'C:/ShareSSD/scop/data_tables/table$'
path_to_data = 'C:/ShareSSD/scop/maxcluster_summaries/'

# CATH
#structures = ['1c4zA02','2evvA00','3bpkA01']
#measures = ['RMSD','GDT-HA','GDT-TS','TM-score','MaxSub']
#path_to_tables = 'C:/ShareSSD/cath/data_tables/table_'
#path_to_data = 'C:/ShareSSD/cath/maxcluster_summaries/'

# CASP
#structures = ['T0859','T0860','T0861','T0862','T0863','T0864','T0865','T0866','T0867']
#measures = ['RMSD','GDT-HA','GDT-TS','TM-score']

combinations = util.generateMeasureCombinations(measures) 

current_combo = 0
current_structure = 0

while current_structure < len(structures):
    structure = structures[current_structure]
    sample = scop.readSCOPNames(structure)
    #sample = cath.readCATHNames(structure)
    while current_combo < len(combinations):
        parsed = combinations[current_combo].split(' ')
        measure1 = parsed[0]
        measure2 = parsed[1]

        measure_data,_,_ = util.readMeasureData(measure1,measure2,structure,path_to_data)

        data = scop.intersectSCOPKeys(sample,measure_data)
        #data = cath.intersectCATHKeys(sample,measure_data)
        
        with open(path_to_tables+structure+'$'+measure1+'$'+measure2,'w') as file:
            for key, value in sorted(data.items(), key=lambda x: x[1][2], reverse=True):
                line = str(key)+' '+str(value[2])+' '+str(value[3])
                file.write(line+'\n')

        current_combo += 1

    current_combo = 0
    current_structure += 1    