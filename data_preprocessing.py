import tensorflow as tf



def preprocess_training(img_height, img_width, batch_size, folder):
    train_ds = tf.keras.preprocessing.image_dataset_from_directory(folder, labels='inferred', label_mode='int',
                                                                   class_names=None,
                                                                   color_mode='rgb', batch_size=batch_size,
                                                                   image_size=(img_height, img_width), shuffle=True,
                                                                   seed=123,
                                                                   validation_split=0.2, subset='training',
                                                                   interpolation='bilinear', follow_links=False
                                                                   )
    return train_ds


def preprocess_testing(img_height, img_width, batch_size, folder):
    val_ds = tf.keras.preprocessing.image_dataset_from_directory(folder, labels='inferred', label_mode='int',
                                                                 class_names=None,
                                                                 color_mode='rgb', batch_size=batch_size,
                                                                 image_size=(img_height, img_width), shuffle=True,
                                                                 seed=123,
                                                                 validation_split=0.2, subset='training',
                                                                 interpolation='bilinear', follow_links=False)
    return val_ds
