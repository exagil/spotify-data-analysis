import os.path
import pandas as pd

def get_my_path():
    return os.path.abspath(os.path.dirname(__file__))

def get_data_df():
    my_path = get_my_path()
    data_path = os.path.join(my_path, "./assets/data.csv")
    return pd.read_csv(data_path)

def get_genre_df():
    my_path = get_my_path()
    genre_path = os.path.join(my_path, "./assets/spotify_data_by_genres.csv")
    return pd.read_csv(genre_path)
