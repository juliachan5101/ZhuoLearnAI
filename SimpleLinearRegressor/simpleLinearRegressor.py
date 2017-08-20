import numpy as np

# A simple linear regressor
# AX + b = Y
# Assume sample size of X and Y is m,
# each obs has n numeric features,
# each obs has a numeric y value to predict
class SimpleLinearRegressor(object):
    def __int__(self):
        raise Exception('not implemented')
        #Your code here

    # x is numpy array with shape: (m * n)
    # y is numpy array with shape: (m * 1)
    # is_interception determines whether regress with b
    # Train model
    def fit(self, x, y, is_interception = True):
        raise Exception('not implemented')
        #Your code here

    # x is numpy array with shape: (m * n)
    # return numpy array y with shape (m * 1)
    def predict(self, x):
        raise Exception('not implemented')
        #Your code here


    # Return numpy array with shape (1 * n) which represents A
    def __str__(self):
        raise Exception('not implemented')
        #Your code here







