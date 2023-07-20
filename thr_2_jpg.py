import os
import argparse
import numpy as np
import PIL.Image as pil
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.cm as cm
from utils.utils import visualize_disp_as_numpy, visualize_depth_as_numpy, Raw2Celsius, load_as_float_img

def parse_args():
    parser=argparse.ArgumentParser()
    parser.add_argument('--thr_png_pth', type=str,
                        help='path to thermal_image',
                        default='/mnt_2/Datasets/MS2/sync_data/_2021-08-06-16-19-00/thr/img_left')


    return parser.parse_args()

def save_numpy_as_image(numpy_array, image_path):
    # Normalize the numpy array to values between 0 and 255
    normalized_array = (numpy_array * 255).astype(np.uint8)

    if numpy_array.ndim == 3:
        normalized_array = np.squeeze(normalized_array, 2)
    
    # Create an Image object from the numpy array
    image = pil.fromarray(normalized_array, mode='L')

    # Save the image to the specified path
    image.save(image_path)

def normalize_zeroone(numpy_array):
    min = np.min(numpy_array)
    numpy_array = numpy_array-min
    max = np.max(numpy_array)
    numpy_array/= max
    
    return numpy_array

def get_hist_range_and_normalize(npy, bottom=0.01, top=0.99):
    # npy = np.squeeze(npy,2)
    im_sort = np.sort(np.squeeze(npy,2).reshape(-1))
    tmax = im_sort[round(len(im_sort)*0.99)-1]
    tmin = im_sort[round(len(im_sort)*0.01)]

    npy[npy<tmin] = tmin
    npy[npy>tmax] = tmax

    npy = (npy-tmin)/(tmax-tmin)

    return npy


def npy_to_jpg_monodepth_2(args, normalize_follow_author = True):
    if normalize_follow_author:
        output_pth = args.thr_png_pth.replace('thr', 'thr_normalized')
    else:
        output_pth = args.thr_png_pth.replace('thr', 'thr_vis')

    if not os.path.exists(output_pth):
        print('Since output path does not exist, make output folder')
        os.makedirs(output_pth)
        # os.makedirs(os.path.join(output_pth, args.model_type))
    
    cnt = len(os.listdir(args.thr_png_pth))
    for index in range(cnt):
        thr_img_pth = os.path.join(args.thr_png_pth, f'{index:06}.png')
        thr_out_pth = os.path.join(output_pth, f'{index:06}.png')
        thr_img = load_as_float_img(thr_img_pth)

        if normalize_follow_author:
            thr_img = get_hist_range_and_normalize(thr_img)
        else:
            thr_img = Raw2Celsius(thr_img)
            thr_img = normalize_zeroone(thr_img)
        
        save_numpy_as_image(thr_img, thr_out_pth)



if __name__ == '__main__':
    args=parse_args()
    npy_to_jpg_monodepth_2(args)