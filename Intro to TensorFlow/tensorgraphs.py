import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

g = tf.Graph()

x = tf.constant(8, name = 'x_const')
y = tf.constant(5, name = 'y_const')
# exercise:
z = tf.constant(4, name = 'z_const')
my_sum = tf.add(x, y,  name = 'x_y_sum')

# my_sum = tf.add(x+y, z,  name = 'x_y_z_sum')

my_new_sum = tf.add(my_sum, z)
with tf.Session() as sess:
    print(my_sum.eval())
    print(my_new_sum.eval())

