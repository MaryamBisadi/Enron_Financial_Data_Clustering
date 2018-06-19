# Enron_Financial_Data_Clustering
Objective of this project is to cluster Enron financial data to find persons of interest. Which is performed based on just two financial features; Salary and Exercised Stock Options.
Affinity Propagation and KMean clustering have been deployed on financial data.

k-means is a popular clustering algorithm that assign each data point to one of K cluster based on the feature similarity.
Choosing a good initial value for the number of clusters (k) can be problematic as k can be anything between 1 and the number of data instances.

Affinity Propagation is an algorithm that cluster data and find the number of clusters simultaneously. it creates clusters by sending messages between pairs of samples until convergence. The algorithm exchanges messages between pairs of data points until a set of exemplars emerges, with each exemplar corresponding to a cluster. 
“preference” is an input parameter for this algorithm that influance the number of clusters. if "preference" is not specified as an argument, it will be set to the medium of the input similarities.

The following plots show these two clustering tecnique results for same number of cluster.

 ### Affinity Propagation with preference = -1.5
![affinintypropagation_2](https://user-images.githubusercontent.com/39537957/41582641-0afb7926-7357-11e8-8dc4-b461e5b631cd.png)
### KMean Clustering with K = 2
![kmean_2](https://user-images.githubusercontent.com/39537957/41582660-136924f0-7357-11e8-9b2c-6bfa9fbb515c.png)

### Affinity Propagation with preference = -1.3
![affinintypropagation_3](https://user-images.githubusercontent.com/39537957/41582642-0b1bcb9a-7357-11e8-9a5c-7126d7051a42.png)
### KMean Clustering with K = 3
![kmean_3](https://user-images.githubusercontent.com/39537957/41582661-1388af5a-7357-11e8-85e3-2256102240ef.png)

### Affinity Propagation with no preference set as input parameter
![affinintypropagation_14](https://user-images.githubusercontent.com/39537957/41582643-0b3dd44c-7357-11e8-825a-3081446aaf94.png)
### KMean Clustering with K = 14
![kmean_14](https://user-images.githubusercontent.com/39537957/41582662-13a2430c-7357-11e8-9ee3-514c0a7957fb.png)
