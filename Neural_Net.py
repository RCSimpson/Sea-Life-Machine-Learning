import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
import datetime
from tensorflow.keras import layers
import matplotlib.pyplot as plt
import Image_Set as imgset
from tensorflow import keras

folder = 'resized_output'
batch_size = 10
img_height = 100
img_width = 100

train_ds = tf.keras.preprocessing.image_dataset_from_directory( folder, labels='inferred', label_mode='int', class_names=None,
                        color_mode='rgb', batch_size=batch_size, image_size=(img_height, img_width), shuffle=True, seed=123,
                        validation_split=0.2, subset= 'training', interpolation='bilinear', follow_links=False
                        )

val_ds = tf.keras.preprocessing.image_dataset_from_directory(folder, labels='inferred', label_mode='int', class_names=None,
                        color_mode='rgb', batch_size=batch_size, image_size=(img_height, img_width), shuffle=True, seed=123,
                        validation_split=0.2, subset= 'training', interpolation='bilinear', follow_links=False
                        )

class_names = train_ds.class_names
print(class_names)
num_classes = len(class_names)

model = tf.keras.Sequential([
  layers.experimental.preprocessing.Rescaling(1./255),
  layers.Conv2D(10, 3, activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(10, 3, activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(10, 3, activation='relu'),
  layers.MaxPooling2D(),
  layers.Flatten(),
  layers.Dense(128, activation='relu'),
  layers.Dense(num_classes)
])

model.compile(optimizer='adam', loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True), metrics=['accuracy'])

log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)
#['accuracy', 'loss', 'val_accuracy', 'val_loss']

history = model.fit(train_ds, validation_data=val_ds, epochs=20)
plt.figure(figsize=(10,5))
plt.subplot(121)
plt.plot(history.history['loss'])
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.subplot(122)
plt.plot(history.history['accuracy'])
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.show()