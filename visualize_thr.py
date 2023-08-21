#%%
import matplotlib.pyplot as plt
import os
from utils.utils import visualize_disp_as_numpy, visualize_depth_as_numpy, Raw2Celsius, load_as_float_img
import numpy as np
import cv2 as cv
from thr_2_jpg import normalize_zeroone, get_hist_range_and_normalize

def plt_multi(cnt, *args):
    for i in range(cnt):
        plt.subplot(cnt, 1, i+1)
        plt.imshow(args[i])

def main(index):
    # seq_name = '/mnt_2/Datasets/MS2/sync_data/_2021-08-06-16-19-00/thr/img_left'
    seq_name = '/mnt_2/Datasets/MS2/sync_data/_2021-08-13-22-03-03/thr/img_left'
    seq_name_rgb = seq_name.replace('thr', 'rgb')
    index = int(index)
    thr_img_pth = os.path.join(seq_name, f'{index:06}.png')
    rgb_img_pth = os.path.join(seq_name_rgb, f'{index:06}.png')

    thr_img = load_as_float_img(thr_img_pth)
    thr_img = get_hist_range_and_normalize(thr_img)
    thr_img = normalize_zeroone(thr_img)
    edges = cv.Canny(np.uint8(np.squeeze(thr_img, 2)*255), 0, 0 )
    plt.subplot(2,1,1)
    plt.imshow(thr_img)
    plt.subplot(2,1,2)
    plt.imshow(edges, cmap='gray')

    # plt_multi(2, (thr_img, edges))

    # thr_img = Raw2Celsius(thr_img)
    # rgb_img = load_as_float_img(rgb_img_pth)
    # rgb_resized = cv.resize(rgb_img,(640,256))
    # min = np.min(thr_img)
    # thr_img = thr_img-min
    # max = np.max(thr_img)
    # thr_img/= max
     
    # edges = cv.Canny(np.squeeze(np.uint8(thr_img), 2)*255 ,5,12)
    # edges_rgb = cv.Canny(np.uint8(rgb_img)*255 ,300,400)

    # plt.subplot(2,2,1)
    # plt.imshow(thr_img)
    # plt.subplot(2,2,2)
    # plt.imshow(edges, cmap='gray')
    # plt.subplot(2,2,3)
    # plt.imshow(np.uint8(rgb_img))
    # plt.subplot(2,2,4)
    # plt.imshow(edges_rgb)

    # plt.hist(np.ravel(thr_img*255), 256, [0,256])

    # plt.subplot(3,1,1)
    # plt.imshow(thr_img)
    # plt.subplot(3,1,2)
    # plt.imshow(np.uint8(rgb_resized))
    # plt.subplot(3,1,3)
    # plt.imshow(np.uint8(rgb_img))
    # plt.imshow(thr_img)


if __name__ == "__main__":
    main(1600)

# %%
