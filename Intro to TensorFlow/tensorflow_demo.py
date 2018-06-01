# -*- coding: utf-8 -*-
"""
Created on Sun May 20 20:56:17 2018

@author: vp185104
"""

import tensorflow as tf

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

hello = tf.constant("Hello, World!")
sess = tf.Session()
print(sess.run(hello))

i = tf.constant(5)
j = tf.constant(5)

print(sess.run(i + j))

a = tf.Variable([0])
# print(a)
a.assign([1])
print("Value of a: ", a)

with tf.Session() as sess:
    initializer = tf.global_variables_initializer
    print(a.eval())
