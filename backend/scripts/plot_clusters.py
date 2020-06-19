import pandas as pd
import numpy as np
import os.path
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def plot_clusters():
    my_path = os.path.abspath(os.path.dirname(__file__))
    data_path = os.path.join(my_path, "./../assets/data.csv")
    data_df = pd.read_csv(data_path)
    cluster_features = ['liveness', 'loudness', 'tempo', 'valence', 'acousticness', 'danceability', 'instrumentalness',
                        'energy', 'speechiness']
    df_cluster = data_df[cluster_features]
    scaler = StandardScaler()
    X_std = scaler.fit_transform(np.array(df_cluster))

    k = 2
    km = KMeans(n_clusters=k, init='k-means++', random_state=123)
    km = km.fit(X_std)
    km_cluster = km.fit_predict(X_std)

    cluster_map = pd.DataFrame()
    cluster_map['data_index'] = df_cluster.index.values
    cluster_map['cluster'] = km.labels_

    pca = PCA(n_components=2)
    principalComponents = pca.fit_transform(df_cluster)
    principalDf = pd.DataFrame(data=principalComponents
                               , columns=['principal component 1', 'principal component 2'])

    plt.scatter(principalDf['principal component 1'], principalDf['principal component 2'], s=100, c=km_cluster)
    plt.title("Scatter Plot")
    plt.savefig('clusters.png')

plot_clusters()
