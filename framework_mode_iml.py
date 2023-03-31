from tensorflow.keras import layers
from tensorflow import keras

import matplotlib.pyplot as plt
import tensorflow_addons as tfa
import tensorflow as tf
import numpy as np


learning_rate = 0.001
weight_decay = 0.0001
batch_size = 128
num_epochs = 10

PATH_1='/' #denosing model path 
PATH_2='/' #Data path

def load_data(PATH_2):

    #Load classification data from path _2 
    x_train, y_train, x_test, y_test=[], [], [], []

    return (x_train, y_train), (x_test, y_test)

def denoising(data):

    #loading model from the path_1
    model=tf.load_model(PATH_1)

    return model.preidict(data)

def prepare_data(data):


    #1.Normalization
    #2.Resizing
    #3.data Augmentaion
    data_aumentation=tf.keras.sequential(
        #augmentation operations
    name="data_augmentation",
    )

    return denoising(data)


def get_model():
    
    #defining model architeruers
    model = tf.keras.sequentail([
        #deifine model operations
    ])

    return model

def train():

    data=load_data(PATH_2)

    prepared_data=prepare_data(data)

    model=get_model()


    model.compile(optimizer='adam',
              loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
              metrics=['accuracy'] ) # all the metrics proposed will be passed 

    model_history=model.fit()

    #saving model checkpoints
    model.save_weights('Checkpoints/')

    loss=model_history.history['loss']
    val_loss=model_history.history['val_loss']
    
def evaluate(model, test_data):

    #predictions on test_data
    #plotting confusion matrix
    #plotting other importent results
    return 


if __name__=='main':
    train()


