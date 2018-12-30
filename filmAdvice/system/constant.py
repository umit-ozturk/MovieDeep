SYSTEM_APP_PATH = '/filmAdvice/system/'
DATASET_LINKS_FILE = 'links.csv'
DATASET_MOVIES_FILE = 'movies.csv'
DATASET_RATINGS_FILE = 'ratings.csv'
DATASET_TAGS_FILE = 'tags.csv'

n_nodes_inpl = 1260
n_nodes_hl1 = 100
n_nodes_outl = 1260

NODES_CONST = (
    (n_nodes_inpl, 1260),
    (n_nodes_hl1, 100),
    (n_nodes_outl, 1260),
)

batch_size = 100
hm_epochs = 50

TENSOR_CONST = (
    (n_nodes_inpl, 1260),
    (n_nodes_hl1, 100),
    (n_nodes_outl, 1260),
)
