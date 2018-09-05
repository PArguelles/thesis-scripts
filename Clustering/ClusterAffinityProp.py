import matplotlib.pyplot as plt
import numpy as np
import time as time
from sklearn.cluster import AffinityPropagation
from itertools import cycle
import UtilitiesCommon as util

def afpCustom(context, structure, measure1, measure2, values1, values2, data, true_labels, path_res):

    algorithm = 'afp'

    path = path_res

    tmp = list(zip(values1, values2))        
    X = np.array(tmp)

    damping = 0.95
    preference = -200
    af = AffinityPropagation(damping=.95,preference=-200).fit(X)
    cluster_centers_indices = af.cluster_centers_indices_
    labels = af.labels_
    n_clusters_ = len(cluster_centers_indices)

    print("AFP: "+str(damping)+' '+str(preference))

    try:
        colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
        for k, col in zip(range(n_clusters_), colors):
            class_members = labels == k
            cluster_center = X[cluster_centers_indices[k]]
            plt.plot(X[class_members, 0], X[class_members, 1], col + '.')
            plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
                    markeredgecolor='k', markersize=5)
            #for x in X[class_members]:
                #plt.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], col)

        plt.xlabel(measure1)
        plt.ylabel(measure2)

        n = str(damping)+'_'+str(preference)
        if 'cath' in context or 'scop' in context:
            ce = util.clusterEvaluation(X,labels,true_labels)  
            util.saveResultsToFile(structure, algorithm, n, data, measure1, measure2, ce, path)
        elif 'casp' in context:
            ce = util.clusterEvaluationNoLabels(X,labels)
            util.saveResultsToFileNoLabels(structure, algorithm, n, measure1, measure2, ce, path)

        util.saveImage(plt, path+structure+'/', 'plot_'+structure+'_'+measure1+'_'+measure2+'_'+algorithm+'_'+str(n))
    except Exception:
        pass 
