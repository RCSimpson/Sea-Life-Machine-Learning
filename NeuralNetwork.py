import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
from tensorflow import keras
import datetime
from tensorflow.keras import layers

class Network(keras.Model):
    def __init__(self, hyp_params, **kwargs):
        super(Network, self).__init__(**kwargs)

        """
        :param hyp_params:
            hyp_params has the following keys:
                activation:
                number_of_layers:
                number_of_classes:
                middle_neurons:
                end_neurons:
                optimizer:
                loss:
                metric:
        :param kwargs:
        """

        self.activation = hyp_params['activation']
        self.number_of_layers = hyp_params['number_of_layers']
        self.number_of_classes = hyp_params['number_of_classes']
        self.middle_neurons = hyp_params['middle_neurons']
        self.end_neurons = hyp_params['end_neurons']
        self.optimizer = hyp_params['optimizer']
        self.loss = hyp_params['loss']
        self.metric = hyp_params['metric']

    def __call__(self,training_data,validation_data):
        """
        :return: compile the model using the parameters provided above by the hyper parameter dictionary.
        """
        train_ds = training_data
        val_ds = validation_data

        model = tf.keras.Sequential()
        model.add(layers.experimental.preprocessing.Rescaling(1. / 255))

        for __ in range(self.number_of_layers):
            model.add(layers.Conv2D(self.middle_neurons, 3, activation=self.activation))
            model.add(layers.MaxPooling2D())

        model.add(layers.Flatten())
        model.add(layers.Dense(self.end_neurons, activation=self.activation))
        model.add(layers.Dense(self.number_of_classes))

        model.compile(optimizer=self.optimizer, loss=self.loss, metrics=self.metric)
        history = model.fit(train_ds, validation_data=val_ds, epochs=20)

        return history