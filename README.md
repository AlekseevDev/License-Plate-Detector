# Photo license plate detector 🕵🏻

![python](https://img.shields.io/badge/4.6.0-opencv-green?logo=opencv&logoColor=white)
![python](https://img.shields.io/badge/3.9.x-python-blue?logo=python&logoColor=white)

## Overview

Viola-Jones method using rectangular primitives. To search for an object in a digital image, a trained classifier is used, presented in xml format. The classifier is formed on Haar primitives. Based on this basis, a cascade of classifiers is built that decides whether an object is recognized in the image or not. More details can be read [here](https://docs.opencv.org/3.4/dc/d88/tutorial_traincascade.html).

## Quick Start

After cloning the repository, go to the project folder.\
Before you start, make sure you have the correct version of python installed by typing the command in the terminal

`python3 --version`

Next, install the necessary libraries by typing the following command

`pip3 install -r requirements.txt`

And finally, let's run our script on test images

`python3 main.py`

After success, we should have a folder **result_images** in the same directory in which our processed images are located.
\
\
\
_Be sure to try to study the code and change it to understand how it all works._\
🌟 *Do not spare the stars if it helped you or became useful for you! Thank you.*
