import numpy as np
import cv2
import os

def load_images_from_folder(folder):

    """
    :param folder: Specify the directory which contains folders of sorted images. Folder name will specify label.
    :return: returns collection of images set in gray-scale
    """

    images = []
    t=0
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename), 0)
        if img is not None:
            images.append(img)
    return images

def Data_Generator(storage_directory):
    folders = os.listdir(storage_directory)
    labels = folders
    label_array = np.array([])
    image_array = np.array([])
    t = 0

    for folder in folders:
        files = os.listdir(storage_directory + '/' + folder)
        number_of_files = len(files)
        array = np.ones(number_of_files)*t
        label_array = np.append(label_array, array)
        t=+1
        x_array = load_images_from_folder(storage_directory + '/' + folder)
        image_array = np.append(image_array, x_array)
    data_set_y = label_array
    row = data_set_y.shape[0]

    col = np.int(image_array.shape[0]/row)
    data_set_x = image_array.reshape((row,col))


    return data_set_x, data_set_y, labels
