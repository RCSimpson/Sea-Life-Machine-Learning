# Sea-Life-Machine-Learning

<!-- TABLE OF CONTENTS -->
# Table of Contents

## About The Project
 In this project I collect images from the interest of varied sea-life using a web-scrapper that interacts with bing images to save all images it comes across given a certain search query. I then sorted cleaned and homogenized those images so that a neural network could be easily trained by passing images through and allowing the neural network to look for commonalities between images of a certain type. 

## Data Collection and Cleaning
I do not claim copyright over any of these images. These images are for education purposes only.

I have implemented scraper.py to collect these images in accordance with specific search terms. We want to collect images which provide clear views of the creaters, preferably with some degree of contrast. These images are then breifly reviewed to ensure they are of the species we are looking for. Each image is then processed by the data_homogenizer.py to ensure that each image is of size 100x100 pixels. This gives us a standard size to pass through to our intial layer.

<p>
<img src = "https://github.com/RCSimpson/Sea-Life-Machine-Learning/blob/master/images/0.jpg" width = "200" height = "200" >
<img src = "https://github.com/RCSimpson/Sea-Life-Machine-Learning/blob/master/images/1.jpg" width = "200" height = "200" >
<img src = "https://github.com/RCSimpson/Sea-Life-Machine-Learning/blob/master/images/2.jpg" width = "200" height = "200" >
<img src = "https://github.com/RCSimpson/Sea-Life-Machine-Learning/blob/master/images/7.jpg" width = "200" height = "200" >
</p>


## The Machine
