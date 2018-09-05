import UtilitiesCATH as cath
import UtilitiesCommon as util
import ClusterKMeans as km
import ClusterAgglomerative as agg
import ClusterAffinityProp as afp
import ClusterDBSCAN as dbs

cath_results = 'C:/ShareSSD/cath/clustering_results/'
cath_tables = 'C:/ShareSSD/cath/data_tables/'

structures = ['1c4zA02','1xfjA00','2asfA00','2evvA00','2vxzA01','3bpkA01','3hisA02','4kp1A01']
measures = ['RMSD','GDT-HA','GDT-TS','TM-score','MaxSub']
context = 'cath'

combinations = util.generateMeasureCombinations(measures) 

current_combo = 0
current_structure = 0

while current_structure < len(structures):
    structure = structures[current_structure]
    while current_combo < len(combinations):
        parsed = combinations[current_combo].split(' ')
        measure1 = parsed[0]
        measure2 = parsed[1]

        print('Clustering '+measure1+' and '+measure2+' of '+structure)

        measure_data,values1,values2,labels = util.readDataTable(cath_tables, structure, measure1, measure2)

        km.kmeansCustom(context, structure, measure1, measure2, values1, values2, measure_data, labels, cath_results)
        agg.aggloCustom(context, structure, measure1, measure2, values1, values2, measure_data, labels, cath_results)
  
        current_combo += 1
        
    current_combo = 0
    current_structure += 1    
    