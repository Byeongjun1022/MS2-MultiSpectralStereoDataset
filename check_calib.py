import numpy as np
import math
import os

data_root = '/mnt_2/Datasets/MS2/sync_data'
dir_list = os.listdir(data_root)

for i in range(len(dir_list)):
    if os.path.isdir(os.path.join(data_root, dir_list[i])):
        calib = np.load(os.path.join(data_root, dir_list[i],'calib.npy'), allow_pickle=True)
    
    for k, v in calib.item().items():    
        if 'K_thrL' in k:
            print(f'{k}:\n {v}')

# for k, v in calib.item().items():
#     if 'nir2rgb' in k or 'nir2thr' in k or 'rgbL' in k:
#         print(f'{k}:\n {v}')
