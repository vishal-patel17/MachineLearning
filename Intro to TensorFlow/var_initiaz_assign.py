import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Creating variables
with tf.Graph().as_default():
    v = tf.Variable([5])
    w = tf.Variable(tf.random_normal([1], mean = 1.0, stddev = 0.35))

    with tf.Session() as sess:
        # try:
        #     v.eval()
        # except tf.errors.FailedPreconditionError as e:
        #     print('Caught exception: ', e)
        initializer = tf.global_variables_initializer()
        sess.run(initializer)
        print('v: ', v.eval(), '\n w: ', w.eval())
        assign_v = tf.assign(v, [7])
        sess.run(assign_v) # rus without this statement also!
        print('New value of v: ', assign_v.eval())
