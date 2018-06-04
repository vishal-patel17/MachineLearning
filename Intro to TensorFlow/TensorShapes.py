import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

with tf.Graph().as_default():
    scalar = tf.zeros([])
    vector = tf.zeros([3])
    matrix = tf.zeros([3, 5])

    with tf.Session() as sess:
        # print('Scalar has shape: ', scalar.get_shape, ' and value: ', scalar.eval())
        # print('Vector has shape: ', vector.get_shape, ' and value: ', vector.eval())
        # print('Matrix has shape: ', matrix.get_shape, ' and value: ', matrix.eval())
        pass
# Multiplying matrix:

with tf.Graph().as_default():
    x = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype = tf.int32)
    y = tf.constant([[1, 2], [3, 4], [5, 6]], dtype = tf.int32)
    mul = tf.matmul(x, y, name = 'matrix_mul')
    with tf.Session() as sess:
        print('Matrix multiplication: \n', mul.eval())


# Tensor Reshaping

with tf.Graph().as_default():
    orgMatrix = tf.constant([[1, 2], [3, 4], [5, 6], [7, 8], [9, 0], [2, 1], [3, 2], [4, 3]])
    reshaped_matrix = tf.reshape(orgMatrix, [4, 4]) # multiplication should result into 16.

    # Exercise one:
    a = tf.constant([5, 3, 2, 7, 1, 4])
    b = tf.constant([4, 6, 3])
    reshape_a = tf.reshape(a, [2, 3])
    reshape_b = tf.reshape(b, [3, 1])
    axb = tf.matmul(reshape_a, reshape_b)

    with tf.Session() as  sess:
        # print('Reshaped Matrix: \n', reshaped_matrix.eval())
        print('axb: \n', axb.eval())
