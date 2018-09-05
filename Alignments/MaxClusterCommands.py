import os

def listProcessing():
    lin_path_to_results = '/home/pedro/ShareWindows/scop/scop_maxcluster/'
    lin_path_to_structures = '/home/pedro/ShareWindows/scop/structures/'

    structures = ['d1a00d_.ent','d2dysn_.ent','d4qvqv_.ent']

    for structure in structures:
        with open('/home/pedro/ShareWindows/scop/'+structure+'_list','w') as fp:
            for filename in os.listdir(lin_path_to_structures):
                structure_path = '/home/pedro/ShareWindows/scop/'+filename
                fp.write(structure_path+'\n')

def singleAlignment():

    win_path_to_results = 'D:/Dados/scop/scop_maxcluster/'
    win_path_to_structures = 'D:/Dados/scop/structures/'

    lin_path_to_results = '/home/pedro/ShareWindows/scop/scop_maxcluster/'
    lin_path_to_structures = '/home/pedro/ShareWindows/scop/structures/'

    measure = 'gdt 2'

    structures = ['d1a00d_.ent','d2dysn_.ent','d4qvqv_.ent']

    for structure in structures:
        with open('D:/Dados/scop/'+structure+'_alignments','w') as fp:
            for filename in os.listdir(win_path_to_structures):
                cmd = './maxcluster64bit -e '+lin_path_to_structures+structure+' -p '+lin_path_to_structures+filename+' -'+measure+' > '+lin_path_to_results+structure+'_'+filename
                print(cmd)
                fp.write(cmd+'\n')

singleAlignment()
             
