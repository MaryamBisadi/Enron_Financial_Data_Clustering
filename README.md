# Enron_Financial_Data_Clustering
Objective of this project is to cluster Enron financial data to find persons of interest. Which is performed based on just two financial features; Salary and Exercised Stock Options.
Affinity Propagation and KMean clustering have been deployed on financial data.

k-means is a popular clustering algorithm that assign each data point to one of K cluster based on the feature similarity.
Choosing a good initial value for the number of clusters (k) can be problematic as k can be anything between 1 and the number of data instances.

Affinity Propagation is an algorithm that cluster data and find the number of clusters simultaneously. it creates clusters by sending messages between pairs of samples until convergence. The algorithm exchanges messages between pairs of data points until a set of exemplars emerges, with each exemplar corresponding to a cluster. 
“preference” is an input parameter for this algorithm that influance the number of clusters. if "preference" is not specified as an argument, it will be set to the medium of the input similarities.

The following plots show these two clustering tecnique results for same number of cluster.
