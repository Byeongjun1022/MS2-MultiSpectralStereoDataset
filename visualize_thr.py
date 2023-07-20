#%%
import matplotlib.pyplot as plt
import os
from utils.utils import visualize_disp_as_numpy, visualize_depth_as_numpy, Raw2Celsius, load_as_float_img
import numpy as np
import cv2 as cv

def main():
    seq_name = '/mnt_2/Datasets/MS2/sync_data/_2021-08-06-16-19-00/thr/img_left'
    seq_name_rgb = '/mnt_2/Datasets/MS2/sync_data/_2021-08-06-16-19-00/rgb/img_left'
    index = 3352
    thr_img_pth = os.path.join(seq_name, f'{index:06}.png')
    rgb_img_pth = os.path.join(seq_name_rgb, f'{index:06}.png')

    thr_img = load_as_float_img(thr_img_pth)
    thr_img = Raw2Celsius(thr_img)
    rgb_img = load_as_float_img(rgb_img_pth)
    rgb_resized = cv.resize(rgb_img,(640,256))
    # min = np.min(thr_img)
    # thr_img = thr_img-min
    # max = np.max(thr_img)
    # thr_img/= max
    #  
    edges = cv.Canny(np.squeeze(np.uint8(thr_img), 2)*255 ,5,12)
    edges_rgb = cv.Canny(np.uint8(rgb_img)*255 ,300,400)

    # plt.subplot(2,2,1)
    # plt.imshow(thr_img)
    # plt.subplot(2,2,2)
    # plt.imshow(edges, cmap='gray')
    # plt.subplot(2,2,3)
    # plt.imshow(np.uint8(rgb_img))
    # plt.subplot(2,2,4)
    # plt.imshow(edges_rgb)

    # plt.hist(np.ravel(thr_img*255), 256, [0,256])

    plt.subplot(3,1,1)
    plt.imshow(thr_img)
    plt.subplot(3,1,2)
    plt.imshow(np.uint8(rgb_resized))
    plt.subplot(3,1,3)
    plt.imshow(np.uint8(rgb_img))


if __name__ == "__main__":
    main()

# %%
