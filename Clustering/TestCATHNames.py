import UtilitiesCommon as util
import UtilitiesCATH as cath
import os

names = cath.readChainFiles('asd')

dic = {}

for filename in os.listdir('C:/ShareSSD/cath/dompdb/'):
    print(filename)
    dic[filename] = '0'

count = 0
for a in names.keys():
    if a in dic.keys():
        print(dic[a])
        count += 1

print(count)