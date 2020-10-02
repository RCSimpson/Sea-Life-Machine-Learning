# Sea Life Machine Learning

<!-- TABLE OF CONTENTS -->
# Table of Contents

## About The Project
 In this project I collect images from the interest of varied sea-life using a web-scrapper that interacts with bing images to save all images it comes across given a certain search query. I then sorted cleaned and homogenized those images so that a neural network could be easily trained by passing images through and allowing the neural network to look for commonalities between images of a certain type. 

## Data Collection and Cleaning
I do not claim copyright over any of these images. These images are for educational purposes only.

I have implemented scraper.py to collect these images in accordance with specific search terms. We want to collect images which provide clear views of the creaters, preferably with some degree of contrast. These images are then breifly reviewed to ensure they are of the species we are looking for. Each image is then processed by the data_homogenizer.py to ensure that each image is of size 100x100 pixels. This gives us a standard size to pass through to our intial layer.

<p>
<img src = "https://github.com/RCSimpson/Sea-Life-Machine-Learning/blob/master/images/0.jpg" width = "200" height = "200" >
<img src = "https://github.com/RCSimpson/Sea-Life-Machine-Learning/blob/master/images/1.jpg" width = "200" height = "200" >
<img src = "https://github.com/RCSimpson/Sea-Life-Machine-Learning/blob/master/images/2.jpg" width = "200" height = "200" >
<img src = "https://github.com/RCSimpson/Sea-Life-Machine-Learning/blob/master/images/7.jpg" width = "200" height = "200" >
</p>


## The Machine

The machine is a simple convolutional neural network. The first layer is a preprocessing layer that scales all RBG inputs to values between zero and one. This ensure that the machin is able to learn more effeciently- values will not 'blow up'. The hyper parameter dictionary then allows the user to specify how many hidden layers one wants to use in addition to the number of neurons and the activation function.


When running the machine I used the following dictionary:

* hyp_params = dict()

* hyp_params['activation'] = 'relu'

* hyp_params['number_of_layers'] = 4

* hyp_params['number_of_classes'] = 4

* hyp_params['middle_neurons'] = 10

* hyp_params['end_neurons'] = 128

* hyp_params['optimizer'] = 'adam'

* hyp_params['loss'] = tf.losses.SparseCategoricalCrossentropy(from_logits=True)

* hyp_params['metric'] = 'accuracy'

* hyp_params['epochs'] =  20

A great number of epochs aren't necessary. Certain parameter choices are obvious given the fact we are training a neural network to classify and make predictions about images so we choose sparse categorical crossentropy as the lost function.

<img src = "https://github.com/RCSimpson/Sea-Life-Machine-Learning/blob/master/images/summary.JPG" >
