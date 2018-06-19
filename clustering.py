
import pickle
import numpy as np
import matplotlib.pyplot as plt
from feature_format import featureFormat, targetFeatureSplit

from sklearn.cluster import KMeans
from sklearn import preprocessing
from itertools import cycle
from sklearn.cluster import AffinityPropagation

def Draw(plt, f1_name="feature 1", f2_name="feature 2", name="image.png"):
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()


def KMeanClustering(scaled_finance_feature, features, f1_name="feature 1", f2_name="feature 2"):

    pred = KMeans(n_clusters=2, random_state=0).fit_predict(scaled_finance_feature)

    ### plot each cluster with a different color--add more colors if needed
    colors = ["#8d8a8b", "#f6afce", "#fbddea", "#154981", "#6f8ba9","#f97923","#f6d612","#9e3b7e"
        ,"#ff9900","#7d0234","#9cfdff","#d7b8ff","#c6ffc6","#d45440"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    Draw(plt, f1_name, f2_name, name="KMean.pdf")


def AffinityPropagationClustering(scaled_finance_feature, f1_name="feature 1", f2_name="feature 2"):

    # no preferences passed as arguments = the median of the input similarities -> number of cluster = 14
    # preference = -1.3 -> number of cluster = 3
    # preference = -1.5 -> number of cluster = 2
    af = AffinityPropagation(preference = -1.5).fit(scaled_finance_feature)
    cluster_center_indicator = af.cluster_centers_indices_
    labels = af.labels_
    n_clusters_ = len(cluster_center_indicator)
    print('Estimated number of clusters: %d' % n_clusters_)

    colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
    for k, col in zip(range(n_clusters_), colors):
        class_members = labels == k
        cluster_center = scaled_finance_feature[cluster_center_indicator[k]]
        plt.plot(scaled_finance_feature[class_members, 0], scaled_finance_feature[class_members, 1], col + '.')
        plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col, markeredgecolor='k', markersize=14)
        for x in scaled_finance_feature[class_members]:
            plt.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], col)

    Draw(plt, f1_name, f2_name, name="AffinintyPropagation.pdf")


### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("dataset.pkl", "r") )
### there's an outlier--remove it!
data_dict.pop("TOTAL", 0)

### the input features we want to use
### can be any key in the person-level dictionary (salary, director_fees, etc.)
feature_1 = "salary"
feature_2 = "exercised_stock_options"
poi  = "poi"
features_list = [poi, feature_1, feature_2]
data = featureFormat(data_dict, features_list )
poi, finance_features = targetFeatureSplit( data )

#scailing the features
finance_features_array = np.asarray(finance_features)
minmax_scaler = preprocessing.MinMaxScaler()
scaled_finance_feature = minmax_scaler.fit_transform(finance_features_array)


AffinityPropagationClustering(scaled_finance_feature, f1_name=feature_1, f2_name=feature_2)

KMeanClustering(scaled_finance_feature, scaled_finance_feature, f1_name=feature_1, f2_name=feature_2)


