## Steps for preprocessing
#1) load in the data

#Note: at first this will be meter reading only with numbers, not dials. 

# Dataset does not need the 'reader detection', just need to resize images for classification


import os
import sys
import argparse
import torch 
from torch.utils.data import Dataset #note, not the actual dataset, a torch package
from PIL import Image

import torchvision.transforms as T
import pandas as pd



#Note to self; batching is not required for this project


#cropper

#crop image and save it

#collect tasks

