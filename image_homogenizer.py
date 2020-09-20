import cv2
import os


def load_images_from_folder(folder):
    images = []

    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images

def homogenize_image_set(image_set,a,b):

    export_directory = os.path.dirname(os.path.realpath(__file__)) + "/resized_output/"
    if (os.path.exists(export_directory) == False):
        os.mkdir(export_directory)
    t=0

    for image in image_set:
        old_image = image
        new_image = cv2.resize(old_image, (a, b))
        new_file_name = export_directory + str(t) + '.jpg'
        cv2.imwrite(new_file_name, new_image)
        print(new_file_name)
        t+=1

def main():
    folder = 'scraper_output'
    image_set = load_images_from_folder(folder)
    a=100
    b=100
    homogenize_image_set(image_set, a, b)


if __name__ == '__main__':
    main()