import operator
import SCOPUtilities as scop

#x = {1:'b', 2:'a',3:'c',5:'v',4:'d'}

measure1 = 'RMSD'
measure2 = 'MaxSub'

x,_,_ = scop.readMeasureData(measure1,measure2,'3o88')

if 'RMSD' in measure1:
    sorted_x = sorted(x.items(), key=operator.itemgetter(1))
    print('rmsd')
else:
    sorted_x = sorted(x.items(), key=operator.itemgetter(1),reverse=True)

print(sorted_x)

with open('D:/Dados/dict.txt', 'w') as file:
    for value in sorted_x:
        file.write('{}\n'.format(value))