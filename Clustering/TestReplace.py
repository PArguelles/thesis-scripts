import os

path = 'C:/ShareSSD/scop/maxcluster_summaries/'

indexes = [11,23]
char = '$'

for filename in os.listdir(path):
    copy = filename
    for index in indexes:
        copy = copy[:index] + char + copy[index + 1:]

    os.rename(path+filename, path+copy)