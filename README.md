# Caffe Recognition
SE 491 Project used to explore the world of learning, neural nets, and image processing through the Caffe deep learning toolkit.


## Pre-requisites and setup Instructions
  * Where applicable, please use Python version 2.7.12 and OpenCV 2.4
  * [Caffe version 1.0](http://caffe.berkeleyvision.org/installation.html)
  * [Ubuntu Guide](https://github.com/BVLC/caffe/wiki/Ubuntu-16.04-or-15.10-Installation-Guide)
  * Share images of aircraft and other objects [here](https://drive.google.com/drive/folders/0B_qq4rfPzIJ5eWkzUEFLMXVOY0U?usp=sharing)


## Training

### Caffe Training Documentation
  * [Training on ImageNet](http://caffe.berkeleyvision.org/gathered/examples/imagenet.html)
  * Alternatively, see pre-trained models in [Model Zoo](https://github.com/BVLC/caffe/wiki/Model-Zoo)

### Instructions
  1. (from **input**) `python image_manipulator.py <inDir> train` (where `inDir` is one of `planes`, `helicopters`, etc. (the class)
  2. Edit [create_lmdb.py](code/create_lmdb.py) to reflect how to map from filename to class (if you used image_manipulator.py, then this will be the directory name)
  3. (from **code**) `python create_lmdb.py`
  4. (from **root**)
     * `$CAFFE_DIR/compute_image_mean.bin -backend=lmdb input/train_lmdb input/mean.binaryproto`
  5. Edit reported mean-values and paths in [caffenet_train_val_1.prototxt](caffe_models/caffe_model_1/caffenet_train_val_1.prototxt)
  6. Change paths, step-sizes,max_iterations, and GPU-acceleration in [solver_1.prototxt](caffe_models/caffe_model_1/solver_1.prototxt).(For a rough start, consider step size as 10% of your total items in training directory)
  7. After defining model and solver, we can train using
     * `$CAFFE_DIR/build/tools/caffe train --solver caffe_models/caffe_model_1/solver_1.prototxt 2>&1 | tee caffe_models/caffe_model_1/model_1_train.log`
  8. Finally, you can plot the learning curve like this:
     * `python code/plot_learning_curve.py caffe_models/caffe_model_1/model_1_train.log caffe_models/caffe_model_1/caffe_model_1_learning_curve.png`

## Predicting
  1. Update `num_output` in [caffenet_deploy_1.prototxt](caffe_models/caffe_model_1/caffenet_deploy_1.prototxt) to desired number of classes
  2. Update paths in [make_predictions_1.py](code/make_predictions_1.py) & run `python code/make_predictions_1.py`