import numpy as np
import math
import os

data_root = '/mnt_2/Datasets/MS2/sync_data'
dir_list = [i for i in os.listdir(data_root) if os.path.isdir(os.path.join(data_root, i))]

store_calib_txt = False
for i in range(len(dir_list)):
    if os.path.isdir(os.path.join(data_root, dir_list[i])):
        calib = np.load(os.path.join(data_root, dir_list[i],'calib.npy'), allow_pickle=True)

    if store_calib_txt == True:    
        with open('calib.txt','w') as f:
            for k, v in calib.item().items():
                f.write(f'{k}:\n {v}\n')
        break
    for k, v in calib.item().items():    
        if 'K_thrL' in k:
            K = v.copy()
            K[0, :] /= 640
            K[1, :] /= 256
            print(K)
            break
            # print(f'{k}:\n {v}')

# for k, v in calib.item().items():
#     if 'nir2rgb' in k or 'nir2thr' in k or 'rgbL' in k:
#         print(f'{k}:\n {v}')
