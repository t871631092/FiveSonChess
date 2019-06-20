#Do not delete this file.
#ML Development Environment Checking

from __future__ import absolute_import, division, print_function, unicode_literals
from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np
import tensorflow as tf

def run():
    a = np.eye(15)
    print(a)

def TensorFlow_HelloWorld():
    sess =tf.Session()
    hello = tf.constant('HelloTensorFlow!')
    print(sess.run(hello))


run()
TensorFlow_HelloWorld()
