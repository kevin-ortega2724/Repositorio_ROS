import os
import cv2
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
import pandas as pd
import skimage.io as io
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam

Input (224x224x3)
Conv2D (7x7, 64, strides=2, padding='same')
BatchNormalization
Activation (ReLU)
MaxPooling2D (3x3, strides=2, padding='same')

Residual Block 1:
Conv2D (1x1, 64, strides=1, padding='valid')
BatchNormalization
Activation (ReLU)
Conv2D (3x3, 64, strides=1, padding='same')
BatchNormalization
Activation (ReLU)
Conv2D (1x1, 256, strides=1, padding='valid')
BatchNormalization
Add (skip connection)
Activation (ReLU)

Residual Block 2:
Conv2D (1x1, 128, strides=2, padding='valid')
BatchNormalization
Activation (ReLU)
Conv2D (3x3, 128, strides=1, padding='same')
BatchNormalization
Activation (ReLU)
Conv2D (1x1, 512, strides=1, padding='valid')
BatchNormalization
Projection Shortcut (1x1, 512, strides=2, padding='valid')
Add (skip connection)
Activation (ReLU)

Residual Block 3:
Conv2D (1x1, 128, strides=1, padding='valid')
BatchNormalization
Activation (ReLU)
Conv2D (3x3, 128, strides=1, padding='same')
BatchNormalization
Activation (ReLU)
Conv2D (1x1, 512, strides=1, padding='valid')
BatchNormalization
Add (skip connection)
Activation (ReLU)

Residual Block 4:
Conv2D (1x1, 256, strides=2, padding='valid')
BatchNormalization
Activation (ReLU)
Conv2D (3x3, 256, strides=1, padding='same')
BatchNormalization
Activation (ReLU)
Conv2D (1x1, 1024, strides=1, padding='valid')
BatchNormalization
Projection Shortcut (1x1, 1024, strides=2, padding='valid')
Add (skip connection)
Activation (ReLU)

Residual Block 5:
Conv2D (1x1, 256, strides=1, padding='valid')
BatchNormalization
Activation (ReLU)
Conv2D (3x3, 256, strides=1, padding='same')
BatchNormalization
Activation (ReLU)
Conv2D (1x1, 1024, strides=1, padding='valid')
BatchNormalization
Add (skip connection)
Activation (ReLU)

Residual Block 6:
Conv2D (1x1, 256, strides=1, padding='valid')
BatchNormalization
Activation (ReLU)
Conv2D (3x3, 256, strides=1, padding='same')
BatchNormalization
Activation (ReLU)
Conv2D (1x1, 1024, strides=1, padding='valid')
BatchNormalization
Add (skip connection)
Activation (ReLU)

Residual Block 7:
Conv2D (1x1, 256, strides=1, padding='valid')
BatchNormalization
Activation (ReLU)
Conv2D (3x3, 256, strides=1, padding='same')
BatchNormalization
Activation (ReLU)
Conv2D (1x1, 1024, strides=1, padding='valid')
BatchNormalization
Add (skip connection)
Activation (ReLU)

Residual Block 8:
Conv2D (1x1, 512, strides=2, padding='valid')
BatchNormalization
Activation (ReLU)
Conv2D (3x3, 512, strides=1, padding='same')
BatchNormalization
Activation (ReLU)
Conv2D (1x1, 2048, strides=1, padding='valid')
BatchNormalization
Projection Shortcut (1x1, 2048, strides=2, padding='valid')
Add (skip connection)
Activation (ReLU)

Residual Block 9:
Conv2D (1x1, 512, strides=1, padding='valid')
BatchNormalization
Activation (ReLU)
Conv2D (3x3, 512, strides=1, padding='same')
BatchNormalization
Activation (ReLU)
Conv2D (1x1, 2048, strides=1, padding='valid')
BatchNormalization
Add (skip connection)
Activation (ReLU)

Residual Block 10:
Conv2D (1x1, 512, strides=1, padding='valid')
BatchNormalization
Activation (ReLU)
Conv2D (3x3, 512, strides=1, padding='same')
BatchNormalization
Activation (ReLU)
Conv2D (1x1, 2048, strides=1, padding='valid')
BatchNormalization
Add (skip connection)
Activation (ReLU)

AveragePooling2D (7x7, strides=1, padding='valid')
Flatten
Dense (1000, activation='softmax')