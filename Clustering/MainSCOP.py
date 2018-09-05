
import UtilitiesSCOP as scop
import UtilitiesCommon as util
import ClusterKMeans as km
import ClusterAgglomerative as agg
import ClusterAffinityProp as afp
import ClusterDBSCAN as dbs

scop_results = 'C:/ShareSSD/scop/clustering_results/'
scop_tables = 'C:/ShareSSD/scop/data_tables/'

structures = ['d1a00d_.ent','d2dysn_.ent','d4qvqv_.ent']
measures = ['RMSD','GDT-HA','GDT-TS','TM-score','MaxSub']

context = 'scop'

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

        measure_data,values1,values2,labels = util.readDataTable(scop_tables, structure, measure1, measure2)

        km.kmeansCustom(context, structure, measure1, measure2, values1, values2, measure_data, labels, scop_results)
        agg.aggloCustom(context, structure, measure1, measure2, values1, values2, measure_data, labels, scop_results)

        current_combo += 1

    current_combo = 0
    current_structure += 1   