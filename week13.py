import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

# main function 
if __name__ == "__main__":

    cluster_total = 7
    Nexp = 200



    x = np.random.beta(0.5, 15, size = cluster_total)
    y = np.random.beta(0.3, 15, size = cluster_total)
    

    x_axis= []
    y_axis = []
    
    for i in range(cluster_total):

        mu = np.random.beta(0.5, 7)
        sig = np.random.beta(0.3, 3)
        x_axis = np.append(x_axis, x[i] + np.random.normal(mu, sig, Nexp))
        y_axis= np.append(y_axis, y[i] + np.random.normal(mu, sig, Nexp))
    

    plt.figure()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.scatter(x_axis, y_axis)

    plt.show()
    

    data = np.vstack((x_axis, y_axis)).T 
    kmeans = KMeans(n_clusters = cluster_total)
    kmeans.fit(data)
    
    #predictions from kmeans
    pred = kmeans.predict(data)
    frame = pd.DataFrame(data)
    frame['cluster'] = pred
    frame.columns = ['X', 'Y', 'cluster']
    
    #plotting cluster results
    plt.figure()
    plt.title("K-Means Clustering")
    plt.xlabel("X Values")
    plt.ylabel("Y Values")
    for k in range(cluster_total):
        data = frame[frame["cluster"]==k]
        plt.scatter(data["X"],data["Y"])
    plt.show()
