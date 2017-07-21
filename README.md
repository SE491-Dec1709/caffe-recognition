# Caffe Recognition
SE 491 Project used to explore the world of learning, neural nets, and image processing through the Caffe deep learning toolkit.


## Setup Instructions
  * Where applicable, please use Python v2.7.12 and OpenCV 2.4 
  * [Official](http://caffe.berkeleyvision.org/installation.html) 
  * [Ubuntu Guide](https://github.com/BVLC/caffe/wiki/Ubuntu-16.04-or-15.10-Installation-Guide)

## Training Instructions
  * [Training on ImageNet](http://caffe.berkeleyvision.org/gathered/examples/imagenet.html)
  * Alternatively, see pre-trained models in [Model Zoo](https://github.com/BVLC/caffe/wiki/Model-Zoo)

## Preprocessing
  1. `cd input/`
  2. `cd input && python image_manipulator.py <inDir> train` (where `inDir` is one of `planes`, `helicopters`, etc. (the class)
  3. ``