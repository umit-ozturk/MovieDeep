import csv
from filmAdvice.settings import APP_MAIN_CURRENT_PATH
from filmAdvice.system.constant import *
from filmAdvice.system.load_data import LoadDataSets
import numpy as np
import warnings
import pandas as pd


def find_imdb_link_for_movie_id(movie_id):
    with open(APP_MAIN_CURRENT_PATH + SYSTEM_APP_PATH + DATASET_LINKS_FILE, encoding='utf-8') as f:
        reader = csv.DictReader([line.replace(',', '\t') for line in f],
                                fieldnames='movieId,imdbId,tmdbId'.split(','), delimiter='\t')
    for row in reader:
        if row["movieId"] == movie_id:  # imdb_link = "https://www.imdb.com/title/tt" + str(imdb_id) + "/"
            imdb_id = 'tt' + str(row['imdbId'])
            return imdb_id
    return None


def get_movie_table():
    movie_df = pd.read_csv(APP_MAIN_CURRENT_PATH + SYSTEM_APP_PATH + DATASET_MOVIES_FILE,
                           index_col='movieId').drop(['genres'], axis=1)
    print("Debug1")
    return movie_df.head()  # head is just now


def get_user_rating():
    print("Debug2")
    warnings.simplefilter(action='ignore', category=FutureWarning)
    names = ['user_id', 'item_id', 'rating', 'timestamp']
    user_rating_df = pd.read_csv(APP_MAIN_CURRENT_PATH + SYSTEM_APP_PATH + DATASET_RATINGS_FILE, sep=',',
                                 names=names, low_memory=False, header=None)
    user_rating_df = user_rating_df.head(10)
    print(user_rating_df)
    # user_rating_df_2 = user_rating_df.stack()
    n_users = user_rating_df.user_id.unique().shape[0]
    n_items = user_rating_df.item_id.unique().shape[0]
    # user_rating_df_2.columns = user_rating_df_2.columns.droplevel(0)
    # user_rating_df_2.reset_index()
    #user_rating_df_2 = pd.pivot(user_rating_df, values='rating', columns=['userId'])
    print("Debug3")
    return n_users, n_items  # head is just now


def concat_frames(frames=[]):  # Frames Must be List
    print("Debug4")
    result = pd.concat(frames)
    print("Debug5")
    return result

print(get_user_rating())
#print(concat_frames([get_movie_table(), get_user_rating()]))

