from numpy import vstack,array
from numpy.random import rand
#from scipy.cluster.vq import whiten
import scipy.cluster.vq as vec

# data generation with three features
data = vstack((rand(100,3) + array([.5,.5,.5]),rand(100,3)))

# whitening of data
data = vec.whiten(data)

# computing K-Means with K = 3 (2 clusters)
centroids,_ = vec.kmeans(data,3)

# assign each sample to a cluster
clx,_ = vec.vq(data,centroids)
              
print(data)
print(centroids)
print (clx)
