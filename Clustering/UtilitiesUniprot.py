import os

uniprot_path = 'D:/Dados/uniprot/pdb_chain_uniprot.tsv'

with open(uniprot_path) as fp:
    line = fp.readline()
    while line:
        parsed = str(line).strip().split('\t')
        print(parsed[2])
        line = fp.readline()