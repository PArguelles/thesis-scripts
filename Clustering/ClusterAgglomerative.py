import matplotlib.pyplot as plt
import numpy as np
import os
from sklearn.cluster import AgglomerativeClustering
from sklearn.neighbors import kneighbors_graph
import UtilitiesCommon as util

def aggloCustom(context, structure, measure1, measure2, values1, values2, data, true_labels, path_res):

    algorithm = 'agg'

    path = path_res

    tmp = list(zip(values1, values2))        
    X = np.array(tmp)

    if 'cath' in context or 'scop' in context:
        n_ = util.getClassificationsNumber(true_labels)
    else:
        n_ = None

    knn_graph = kneighbors_graph(X, 30, include_self=False)

    for connectivity in (None, knn_graph):
        for n_clusters in (3,5,n_):
            for linkage in ['average','complete','ward']:
                try:
                    print("Agglomerative: "+linkage+' '+str(n_clusters))
                    plt.xlabel(measure1)
                    plt.ylabel(measure2)

                    model = AgglomerativeClustering(linkage=linkage,connectivity=connectivity,n_clusters=n_clusters)
                    model.fit(X)

                    plt.scatter(X[:, 0], X[:, 1], c=model.labels_,cmap='jet',s=10)

                    n = linkage+'_'+str(n_clusters)

                    if 'cath' in context or 'scop' in context:
                        ce = util.clusterEvaluation(X,model.labels_,true_labels)  
                        util.saveResultsToFile(structure, algorithm, n, data, measure1, measure2, ce, path)
                    elif 'casp' in context:
                        ce = util.clusterEvaluationNoLabels(X,model.labels_)
                        util.saveResultsToFileNoLabels(structure, algorithm, n, measure1, measure2, ce, path)

                    util.saveImage(plt, path+structure+'/', 'plot_'+structure+'_'+measure1+'_'+measure2+'_'+algorithm+'_'+str(n))
                except Exception:
                    pass 
