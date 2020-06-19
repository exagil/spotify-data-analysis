from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import pandas as pd
import numpy as np
from collections import Counter
from ast import literal_eval
import base64
from io import BytesIO
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from utils import get_data_df, get_genre_df



# declare constants
HOST = '0.0.0.0'
PORT = 5000

# initialize flask application
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# get_trending_genres_by_year
@app.route('/')
@cross_origin()
def get_trending_genres_by_year():
    data_df = get_data_df()
    genre_data_df = get_genre_df()
    # add genre to data randomly
    data_df["genre"] = np.random.choice(genre_data_df['genres'], size=len(data_df))
    # create result dict which has top trending genres for each year
    trending_genres_by_year = dict()

    # group the data by year and aggregate over genres to get list
    df_grouped = data_df.groupby('year').agg({'genre': list})
    for year in df_grouped.index:
        genre_list = df_grouped.loc[year]['genre']
        counts = dict()
        for i in genre_list:
            counts[i] = counts.get(i, 0) + 1
        max_value = max(counts.values())
        trending_genres = [k for k, v in counts.items() if v == max_value]
        trending_genres_by_year[year] = trending_genres
    return jsonify(trending_genres_by_year)

# get_ten_most_popular_artists_of_2020
@app.route('/popular-artists-2020')
@cross_origin()
def get_ten_most_popular_artists_of_2020():
    data_df = get_data_df()
    data_df = data_df.loc[data_df['year'] == 2020]
    data_df['artists'] = data_df['artists'].apply(literal_eval)
    artists = {}
    artist_song_count = {}
    for index, row in data_df.iterrows():
        for artist in row['artists']:
            if artist in artists:
                artists[artist] += row['popularity']
                artist_song_count[artist] += 1
            else:
                artists[artist] = row['popularity']
                artist_song_count[artist] = 1
    for key, value in artist_song_count.items():
        if value != 1:
            artists[key] = artists[key]/value
    {k: v for k, v in sorted(artists.items(), key=lambda item: item[1])}
    top_artists = Counter(artists).most_common(10)
    return jsonify(list(map(lambda x: x[0], top_artists)))

# get_avg_duration_of_popular_songs_of_2020
@app.route('/popular-songs-duration-2020')
@cross_origin()
def get_avg_duration_of_popular_songs_of_2020():
    data_df = get_data_df()
    result_df = data_df.loc[data_df['year'] == 2020].sort_values(by='popularity', ascending = False).head(10)
    return jsonify({"avg_duration" : (int)(result_df['duration_ms'].mean()/1000)})

# analysis endpoint
@app.route('/api/analysis', methods=['GET'])
def analysis():
    response_obj = {}
    elbow_image = open('./assets/elbow.png', 'rb')  # open binary file in read mode
    elbow_image_read = elbow_image.read()
    response_obj['elbow_fig'] = base64.encodebytes(elbow_image_read).decode("ascii")
    cluster_image = open('./assets/clusters.png', 'rb')  # open binary file in read mode
    clusters_image_read = cluster_image.read()
    response_obj['fig'] = base64.encodebytes(clusters_image_read).decode("ascii")
    return jsonify(response_obj)


if __name__ == '__main__':
    app.run(host=HOST,
            debug=True,
            port=PORT)
