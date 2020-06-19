import pandas as pd
import numpy as np
import os.path
from collections import Counter
from ast import literal_eval
import base64
from io import BytesIO
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def calculate_k():
    my_path = os.path.abspath(os.path.dirname(__file__))
    data_path = os.path.join(my_path, "./../assets/data.csv")
    data_df = pd.read_csv(data_path)
    cluster_features = ['liveness', 'loudness', 'tempo', 'valence', 'acousticness', 'danceability', 'instrumentalness', 'energy', 'speechiness']
    df_cluster = data_df[cluster_features]
    scaler = StandardScaler()
    X_std = scaler.fit_transform(np.array(df_cluster))

    ss_dist = []
    K = range(1, 11)
    for k in K:
        km = KMeans(n_clusters=k, init='k-means++', random_state=123)
        km = km.fit(X_std)
        ss_dist.append(km.inertia_)
    plt.plot(K, ss_dist, 'bx-')
    plt.xlabel('k')
    plt.ylabel('Sum of squared distances')
    plt.title('Elbow Method For Optimal k')
    plt.savefig('elbow.png')

calculate_k()
