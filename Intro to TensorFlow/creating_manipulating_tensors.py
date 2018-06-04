import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


with tf.Graph().as_default():
    primes = tf.constant([2,3,5,7,11,13], dtype=tf.int32)

    ones = tf.ones([6], dtype=tf.int32)

    sum = tf.add(primes, ones, name='my_sum')

    with tf.Session() as sess:
        print(sum.eval())

