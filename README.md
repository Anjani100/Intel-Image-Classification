# Intel-Image-Classification
A classifier model to classify images of buildings, forest, glacier, mountain, sea and street.

## Setup
The following packages are used in this entire project:
* Python (Version: 3.6.9) - You can install python from the following [link](https://www.python.org/downloads/).
* Numpy - To install numpy, just fire up a command prompt/terminal and type the following text: *pip install numpy*
* OpenCV - pip install opencv-python
* Scikit-learn - pip install scikit-learn
* Tensorflow - We're going to use the GPU version of Tensorflow. Installation Link: [Sentdex](https://pythonprogramming.net/how-to-cuda-gpu-tensorflow-deep-learning-tutorial/)

## The Plan

* Firstly, I am going to build up a Neural Network from scratch and observe our model's performance. For this, I have built a 2-layer neural network and an L-layer neural network separately.

## Dataset

The dataset can be found at the following [link](https://www.kaggle.com/puneet6060/intel-image-classification). You can find the entire description of the dataset there.

## Training the Neural Network

### Preprocessing

The first step in any machine learning problem is to preprocess the data and make it ML-ready. The preprocessing steps are as follows:
* Grab the images from the directory (in which you have stored them) and convert them to array using OpenCV.
