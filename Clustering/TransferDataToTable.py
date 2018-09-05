
import UtilitiesCommon as util
import UtilitiesCASP as casp

# CASP
structures = ['T0859','T0860','T0861','T0862','T0863','T0864','T0865','T0866','T0867']
measures = ['RMSD','GDT-HA','GDT-TS','TM-score']

combinations = util.generateMeasureCombinations(measures) 

current_combo = 0
current_structure = 0

path = 'C:/ShareSSD/casp/data_tables/table_'

for structure in structures:
    models, gdt_ha, gdt_ts, rmsd, tmscore = casp.readTargetSummary(structure)
    values = {'GDT-HA': gdt_ha, 'GDT-TS' : gdt_ts, 'RMSD' : rmsd, 'TM-score' : tmscore}
    
    while current_combo < len(combinations):
        parsed = combinations[current_combo].split(' ')
        measure1 = parsed[0]
        measure2 = parsed[1]

        to_write = list(zip(models,values[measure1],values[measure2]))

        with open(path+structure+'_'+measure1+'_'+measure2,'w') as file:
            for value in to_write:
                line = str(value).replace(',','').replace("'",'').replace("(",'').replace(")",'')
                file.write(line+'\n')

        current_combo += 1

    current_combo = 0
    current_structure += 1       