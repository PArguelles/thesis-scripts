import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import time as time
from sklearn.cluster import DBSCAN
import UtilitiesCommon as util

def dbscanCustom(context, structure, measure1, measure2, values1, values2, data, true_labels, path_res):

    algorithm = 'dbs'

    path = path_res

    tmp = list(zip(values1, values2))        
    X = np.array(tmp)

    try:      
        par1 = 0.6 
        par2 = 20
        db = DBSCAN(eps=par1, min_samples=par2).fit(X)
        core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
        core_samples_mask[db.core_sample_indices_] = True
        labels = db.labels_
                
        unique_labels = set(labels)
        colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unique_labels))]
        for k, col in zip(unique_labels, colors):
                if k == -1:
                        col = [0, 0, 0, 1]

                class_member_mask = (labels == k)

                xy = X[class_member_mask & core_samples_mask]
                plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col), markeredgecolor='k', markersize=14)

                xy = X[class_member_mask & ~core_samples_mask]
                plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col), markeredgecolor='k', markersize=5)

                n = str(par1)+'_'+str(par2)

                if 'cath' in context or 'scop' in context:
                        ce = util.clusterEvaluation(X,labels,true_labels)  
                        util.saveResultsToFile(structure, algorithm, n, data, measure1, measure2, ce, path)
                elif 'casp' in context:
                        ce = util.clusterEvaluationNoLabels(X,labels)
                        util.saveResultsToFileNoLabels(structure, algorithm, n, measure1, measure2, ce, path)

                util.saveImage(plt, path+structure+'/', 'plot_'+structure+'_'+measure1+'_'+measure2+'_'+algorithm+'_'+str(n))
    except Exception:
        pass 