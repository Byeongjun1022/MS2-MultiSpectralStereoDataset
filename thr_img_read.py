from PIL import Image
import os

import numpy as np

image_path = '/mnt_2/Datasets/MS2/'
file_name = 'splits_bj/train_thr_with_gt.txt'

with open(file_name, 'r') as f:
    file_names = f.readlines()

thr_img = Image.open(os.path.join(image_path, file_name[0]))