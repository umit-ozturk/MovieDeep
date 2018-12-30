import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error as MSE
from filmAdvice.system.constant import *


DATASET_RATINGS_FILE = "filmAdvice/system/try_ratings.csv"


def recomender_engine():
    ratings = pd.read_csv(DATASET_RATINGS_FILE, sep=",", engine='python')
    ratings_pivot = pd.pivot_table(ratings[['userId', 'movieId', 'rating']], values='rating',
                                   index='userId', columns='movieId').fillna(0)
    x_train, x_test = train_test_split(ratings_pivot, train_size=0.8)
    hidden_1_layer_vals = {'weights': tf.Variable(tf.random_normal([n_nodes_inpl+1, n_nodes_hl1]))}
    output_layer_vals = {'weights': tf.Variable(tf.random_normal([n_nodes_hl1+1, n_nodes_outl]))}
    input_layer = tf.placeholder('float', [None, 1260])
    input_layer_const = tf.fill([tf.shape(input_layer)[0], 1], 1.0)
    input_layer_concat = tf.concat([input_layer, input_layer_const], 1)
    layer_1 = tf.nn.sigmoid(tf.matmul(input_layer_concat, hidden_1_layer_vals['weights']))
    layer1_const = tf.fill([tf.shape(layer_1)[0], 1], 1.0)
    layer_concat = tf.concat([layer_1, layer1_const], 1)
    output_layer = tf.matmul(layer_concat, output_layer_vals['weights'])
    output_true = tf.placeholder('float', [None, 1260])
    meansq = tf.reduce_mean(tf.square(output_layer - output_true))
    learn_rate = 0.1
    optimizer = tf.train.AdagradOptimizer(learn_rate).minimize(meansq)
    init, sess = init_tensor_sess()
    sess.run(init)
    tot_users = x_train.shape[0]
    for epoch in range(hm_epochs):
        epoch_loss = 0  # initializing error as 0
        for i in range(int(tot_users / batch_size)):
            epoch_x = x_train[i * batch_size: (i + 1) * batch_size]
            _, c = sess.run([optimizer, meansq], feed_dict={input_layer: epoch_x, output_true: epoch_x})
            epoch_loss += c
        output_train = sess.run(output_layer, feed_dict={input_layer: x_train})
        output_test = sess.run(output_layer, feed_dict={input_layer: x_test})

        print('MSE train', MSE(output_train, x_train), 'MSE test', MSE(output_test, x_test))
        print('Epoch', epoch, '/', hm_epochs, 'loss:', epoch_loss)
    return x_train, x_test, input_layer, output_layer


def init_tensor_sess():
    init = tf.global_variables_initializer()
    sess = tf.Session()
    sess.run(init)
    sess = tf.Session()
    return init, sess


def take_predict(x_train):
    x_train, x_test, input_layer, output_layer = recomender_engine()
    init, sess = init_tensor_sess()
    sample_user = x_test.iloc[11, :]
    print(sample_user)
    sample_user_pred = sess.run(output_layer, feed_dict={input_layer: [sample_user]})
    print(sample_user_pred)
