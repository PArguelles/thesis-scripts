import matplotlib.pyplot as plt
import numpy as np
import time as time
from sklearn.cluster import KMeans
import UtilitiesCommon as util

def kmeansCustom(context, structure, measure1, measure2, values1, values2, data, true_labels, path_res):

    algorithm = 'km'
    
    path = path_res

    tmp = list(zip(values1, values2))        
    X = np.array(tmp)

    if 'cath' in context or 'scop' in context:
        n_ = util.getClassificationsNumber(true_labels)
    else:
        n_ = None

    for n in (3,5,n_):
        try:
            print("K-Means: "+str(n))
            kmeans = KMeans(n_clusters=n_)
            kmeans.fit(X)

            centroids = kmeans.cluster_centers_
            labels = kmeans.labels_
     
            colors = ["r.","g.","b.","y.","c.","m.","r.","g.","b.","y."]

            plt.xlabel(measure1)
            plt.ylabel(measure2)

            for i in range(len(X)):
                plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 10)

            plt.scatter(centroids[:,0], centroids[:,[1]], marker = "x", s=25, linewidths=5, zorder=10)

            if 'cath' in context or 'scop' in context:
                ce = util.clusterEvaluation(X,labels,true_labels)  
                util.saveResultsToFile(structure, algorithm, n, data, measure1, measure2, ce, path)
            elif 'casp' in context:
                ce = util.clusterEvaluationNoLabels(X,labels)
                util.saveResultsToFileNoLabels(structure, algorithm, n, measure1, measure2, ce, path)

            util.saveImage(plt, path+structure+'/', 'plot_'+structure+'_'+measure1+'_'+measure2+'_'+algorithm+'_'+str(n))         
        except Exception:
            pass    

