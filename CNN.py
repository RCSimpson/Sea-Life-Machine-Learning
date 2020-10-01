import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
import datetime
import matplotlib.pyplot as plt
import NeuralNetwork as NN
import data_preprocessing as dp


folder = 'resized_output'
batch_size = 10
img_height = 100
img_width = 100

hyp_params = dict()
hyp_params['activation'] = 'relu'
hyp_params['number_of_layers'] = 4
hyp_params['number_of_classes'] = 4
hyp_params['middle_neurons'] = 10
hyp_params['end_neurons'] = 128
hyp_params['optimizer'] = 'adam'
hyp_params['loss'] = tf.losses.SparseCategoricalCrossentropy(from_logits=True)
hyp_params['metric'] = 'accuracy'

train_ds = dp.preprocess_training(img_height, img_width, batch_size, folder)
val_ds = dp.preprocess_testing(img_height, img_width, batch_size, folder)

network = NN.Network(hyp_params)
history = network(train_ds, val_ds)

log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

plt.figure(figsize=(10,5))
plt.title('History')

plt.subplot(121)
plt.plot(history.history['loss'])
plt.ylabel('Loss')
plt.xlabel('Epoch')

plt.subplot(122)
plt.plot(history.history['accuracy'])
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.show()