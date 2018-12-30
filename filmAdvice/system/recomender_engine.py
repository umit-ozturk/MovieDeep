import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error as MSE


DATASET_RATINGS_FILE = "filmAdvice/system/try_ratings.csv"


def recomender_engine():
    ratings = pd.read_csv(DATASET_RATINGS_FILE, sep=",", engine='python')
    print(ratings.shape)
    ratings_pivot = pd.pivot_table(ratings[['userId', 'movieId', 'rating']], values='rating',
                                   index='userId', columns='movieId').fillna(0)
    print(ratings_pivot)
    x_train, x_test = train_test_split(ratings_pivot, train_size=0.8)
    print(x_train)
    n_nodes_inpl = 1260
    n_nodes_hl1 = 100
    n_nodes_outl = 1260
    hidden_1_layer_vals = {'weights': tf.Variable(tf.random_normal([n_nodes_inpl+1, n_nodes_hl1]))}
    output_layer_vals = {'weights': tf.Variable(tf.random_normal([n_nodes_hl1+1, n_nodes_outl]))}
    input_layer = tf.placeholder('float', [None, 1260])
    print(input_layer)
    input_layer_const = tf.fill([tf.shape(input_layer)[0], 1], 1.0)
    print(input_layer_const)
    input_layer_concat = tf.concat([input_layer, input_layer_const], 1)
    layer_1 = tf.nn.sigmoid(tf.matmul(input_layer_concat, hidden_1_layer_vals['weights']))
    layer1_const = tf.fill([tf.shape(layer_1)[0], 1], 1.0)
    layer_concat = tf.concat([layer_1, layer1_const], 1)
    output_layer = tf.matmul(layer_concat, output_layer_vals['weights'])
    output_true = tf.placeholder('float', [None, 1260])
    meansq = tf.reduce_mean(tf.square(output_layer - output_true))
    learn_rate = 0.1
    optimizer = tf.train.AdagradOptimizer(learn_rate).minimize(meansq)
    init = tf.global_variables_initializer()
    sess = tf.Session()
    sess.run(init)
    batch_size = 100
    hm_epochs = 200
    tot_users = x_train.shape[0]
    print(tot_users)
    sess = tf.Session()
    sess.run(init)
    batch_size = 100
    hm_epochs = 50
    tot_users = x_train.shape[0]
    for epoch in range(hm_epochs):
        epoch_loss = 0  # initializing error as 0
        for i in range(int(tot_users / batch_size)):
            epoch_x = x_train[i * batch_size: (i + 1) * batch_size]
            _, c = sess.run([optimizer, meansq], feed_dict={input_layer: epoch_x, output_true: epoch_x})
            print("Debug4")
            epoch_loss += c
        output_train = sess.run(output_layer, feed_dict={input_layer: x_train})
        output_test = sess.run(output_layer, feed_dict={input_layer: x_test})

        print('MSE train', MSE(output_train, x_train), 'MSE test', MSE(output_test, x_test))
        print('Epoch', epoch, '/', hm_epochs, 'loss:', epoch_loss)
    sample_user = x_test.iloc[11, :]
    print(sample_user)
    sample_user_pred = sess.run(output_layer, feed_dict={input_layer: [sample_user]})
    print(sample_user_pred)
