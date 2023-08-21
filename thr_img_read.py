from PIL import Image
import os

import numpy as np
import torch

image_path = '/mnt_2/Datasets/MS2/'
file_name = 'splits_bj/train_thr_with_gt.txt'

with open(file_name, 'r') as f:
    file_names = f.readlines()
data_min=5000
data_max=0
mean_list = []
std_list = []
for i in range(len(file_names)):
    thr_img = Image.open(os.path.join(image_path, file_names[i].split()[0]))
    img = np.array(thr_img, np.int32, copy=False)

    mean_list.append(np.mean(img))
    std_list.append(np.std(img))
    img_min = np.min(img)
    img_max = np.max(img)

    if data_min > img_min:
        data_min = img_min
    
    if data_max < img_max:
        data_max = img_max
    
    # if thr_img.mode == 'I':
    #     img = torch.from_numpy(np.array(thr_img, np.int32, copy=False))

print(np.mean(mean_list), np.mean(std_list))    
print(data_min, data_max) 
# print(thr_img.mode)