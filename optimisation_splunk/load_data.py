
from tensorflow.examples.tutorials.mnist import input_data

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.datasets import fetch_mldata

from sklearn import datasets
from neupy import environment

import pandas as pd
import numpy as np

import sys


def load_data(path_to_file):

    environment.reproducible()

    if path_to_file == "MNIST":

        mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

        def TRAIN_SIZE(num):
            print ('Total Training Images in Dataset = ' + str(mnist.train.images.shape))
            print ('--------------------------------------------------')
            x_train = mnist.train.images[:num,:]
            print ('x_train Examples Loaded = ' + str(x_train.shape))
            y_train = mnist.train.labels[:num,:]
            print ('y_train Examples Loaded = ' + str(y_train.shape))
            print('')
            return x_train, y_train

        def TEST_SIZE(num):
            print ('Total Test Examples in Dataset = ' + str(mnist.test.images.shape))
            print ('--------------------------------------------------')
            x_test = mnist.test.images[:num,:]
            print ('x_test Examples Loaded = ' + str(x_test.shape))
            y_test = mnist.test.labels[:num,:]
            print ('y_test Examples Loaded = ' + str(y_test.shape))
            return x_test, y_test


        x_train, y_train = TRAIN_SIZE(55000)
        x_test, y_test = TEST_SIZE(55000)

        return x_train, x_test, y_train, y_test
    
    # take str args, if none load default trial set
    if path_to_file == None:

        print("Loading sklearn dataset")
        dataset = datasets.load_digits()
        n_samples = dataset.target.size
        n_dimensionality = dataset.data.shape[1]  # gives input dimensions

        n_classes = []
        for counter in dataset.target:
            if counter not in n_classes:
                n_classes.append(counter)
        n_classes = max(n_classes) + 1  # gives output dimensions

        # One-hot encoder
        target = np.zeros((n_samples, n_classes))
        target[np.arange(n_samples), dataset.target] = 1

        x_train, x_test, y_train, y_test = train_test_split(
            dataset.data, target, train_size=0.5)

    # import data form custom file
    if path_to_file == "./input_data/r.csv":
        print "Reading file: ", path_to_file
        dataset = pd.read_csv(path_to_file)
        data, target_raw = dataset.iloc[:, :-1], dataset.iloc[:, -1]
        n_samples = dataset.shape[0]
        n_dimensionality = data.shape[1]
        print "File dimensions: ", n_samples, n_dimensionality

        # integer encode
        label_encoder = LabelEncoder()
        integer_encoded = label_encoder.fit_transform(target_raw)
        # binary encode
        onehot_encoder = OneHotEncoder(sparse=False)
        integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
        target = onehot_encoder.fit_transform(integer_encoded)

        n_classes = target.shape[1]

        x_train, x_test, y_train, y_test = train_test_split(
            data, target, train_size=0.7)
    
    return x_train, x_test, y_train, y_test

# if __name__ == '__main__':
    # load_data( str(sys.argv[1]) )
