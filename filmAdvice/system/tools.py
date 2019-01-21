from filmAdvice.settings import APP_MAIN_CURRENT_PATH
from filmAdvice.profile.models import UserProfile
from filmAdvice.movie.models import Movie, Recommend
from filmAdvice.system.constant import *
import pandas as pd
import warnings
import csv


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
    return movie_df.head()


def get_user_rating():
    warnings.simplefilter(action='ignore', category=FutureWarning)
    names = ['user_id', 'item_id', 'rating', 'timestamp']
    user_rating_df = pd.read_csv(APP_MAIN_CURRENT_PATH + SYSTEM_APP_PATH + DATASET_RATINGS_FILE, sep=',',
                                 names=names, low_memory=False, header=None)
    user_rating_df = user_rating_df.head(10)
    n_users = user_rating_df.user_id.unique().shape[0]
    n_items = user_rating_df.item_id.unique().shape[0]
    return n_users, n_items  # head is just now


def concat_frames(frames=[]):
    result = pd.concat(frames)
    return result


def save_recommendations(predictions, user_id):
    for prediction in predictions:
        rec_movie = Movie.objects.filter(movie_id=prediction).first()
        user = UserProfile.objects.filter(id=user_id)
        print(user)
        recommend = Recommend(user=user, movie=rec_movie)
        recommend.save()
