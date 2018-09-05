import os 

pdb_files = 'D:/Dados/clusco/build/src/data/'
protein_list = 'D:/Dados/clusco/build/src/protein_list'
         
with open(protein_list,'w') as fp:
    for filename in os.listdir(pdb_files):
        print(filename)
        fp.write('./data/'+filename+'\n')