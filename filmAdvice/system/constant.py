SYSTEM_APP_PATH = '/filmAdvice/system/'
DATASET_LINKS_FILE = 'links.csv'
DATASET_MOVIES_FILE = 'movies.csv'
DATASET_RATINGS_FILE = 'ratings.csv'
DATASET_TMP_RATINGS_FILE = 'try_ratings.csv'
DATASET_TAGS_FILE = 'tags.csv'

batch_size = 100
hm_epochs = 50
learn_rate = 0.1

TENSOR_CONST = (
    (batch_size, 100),
    (hm_epochs, 100),
    (learn_rate, 1260),
)
