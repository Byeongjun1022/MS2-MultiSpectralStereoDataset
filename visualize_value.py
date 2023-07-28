
# import cv2
# import os

# # Function to handle mouse events
# def mouse_callback(event, x, y, flags, param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         # Get the pixel value at the cursor location
#         pixel_value = param[y, x]
#         print("Pixel Value at Cursor Location:", pixel_value)

# # Read the image file

# seq_name = '/mnt_2/Datasets/MS2/sync_data/_2021-08-06-11-37-46/thr/img_left'
# seq_name_rgb = '/mnt_2/Datasets/MS2/sync_data/_2021-08-06-11-37-46/rgb/img_left'
# index = 3
# thr_img_pth = os.path.join(seq_name, f'{index:06}.png')
# rgb_img_pth = os.path.join(seq_name_rgb, f'{index:06}.png')

# img_thr = cv2.imread(thr_img_pth)
# img_rgb = cv2.imread(rgb_img_pth)

# # Create a window to display the image
# cv2.namedWindow("Image")
# cv2.imshow("Image", img_rgb)
# cv2.imshow("Image_2", img_thr)

# # Set the mouse callback function
# cv2.setMouseCallback("Image", mouse_callback,img_rgb)
# cv2.setMouseCallback("Image_2", mouse_callback,img_thr)

# # Wait for the user to close the window
# cv2.waitKey(0)

# # Destroy the window and close the program
# cv2.destroyAllWindows()

#--------------------------------------------------------------------------------------
# # click하면 해당 좌표에서의 값이 나오는 코드 (matplotlib 사용)
import matplotlib.pyplot as plt
from utils.utils import visualize_disp_as_numpy, visualize_depth_as_numpy, Raw2Celsius, load_as_float_img, load_as_float_depth
import numpy as np
import os
from thr_2_jpg import normalize_zeroone, get_hist_range_and_normalize

class ClickVisual:
    def __init__(self, fig, img):
        self.fig = fig
        self.cid = self.fig.figure.canvas.mpl_connect('button_press_event', self.onclick)
        self.img = img
    
    # Function to handle mouse events
    def onclick(self, event):
        if event.button == 1:  # Check for left button click
            # Get the pixel value at the click location
            x = int(event.xdata)
            y = int(event.ydata)
            pixel_value = self.img[y, x]
            print("Pixel Value at Click Location:", pixel_value)

def visualize_value_image(img_pth, index, normalize=False):
    img_pth = os.path.join(img_pth,f'{index:06}.png')
    img = load_as_float_img(img_pth)

    if normalize:
        img = get_hist_range_and_normalize(img)
        img = normalize_zeroone(img)
        img*= 255

    fig, ax = plt.subplots()
    ax.imshow(np.uint8(img))
    cv = ClickVisual(fig, img)
    # Show the plot
    plt.show()

    # Disconnect the event handler
    fig.canvas.mpl_disconnect(cv.cid)

def visualize_multiple_value():
    # Read the image file
    seq_name = '/mnt_2/Datasets/MS2/sync_data/_2021-08-06-10-59-33/thr/img_left'
    seq_name_rgb = seq_name.replace('thr', 'rgb')
    depth_thr = seq_name.replace('sync_data','proj_depth')[:-8]+'depth_filtered'
    depth_rgb = depth_thr.replace('thr', 'rgb')
    index = 155
    thr_img_pth = os.path.join(seq_name, f'{index:06}.png')
    rgb_img_pth = os.path.join(seq_name_rgb, f'{index:06}.png')
    thr_depth_pth = os.path.join(depth_thr, f'{index:06}.png')
    rgb_depth_pth = os.path.join(depth_rgb, f'{index:06}.png')


    thr_img = load_as_float_img(thr_img_pth)
    thr_img = Raw2Celsius(thr_img)
    rgb_img = load_as_float_img(rgb_img_pth)

    thr_depth = load_as_float_depth(thr_depth_pth)/256
    rgb_depth = load_as_float_depth(rgb_depth_pth)/256

    # Display the image using matplotlib
    fig, ax = plt.subplots()
    ax.imshow(np.uint8(rgb_img))

    # Set the mouse click event handler
    # cid = fig.canvas.mpl_connect('button_press_event', onclick)
    cv = ClickVisual(fig, rgb_img)

    fig_2, ax_2 = plt.subplots()
    ax_2.imshow(np.uint8(thr_img))
    cv_2 = ClickVisual(fig_2, thr_img)

    fig_3, ax_3 = plt.subplots()
    ax_3.imshow(np.uint8(thr_depth))
    cv_3 = ClickVisual(fig_3, thr_depth)

    fig_4, ax_4 = plt.subplots()
    ax_4.imshow(np.uint8(rgb_depth))
    cv_4 = ClickVisual(fig_4, rgb_depth)

    # Show the plot
    plt.show()

    # Disconnect the event handler
    fig.canvas.mpl_disconnect(cv.cid)

if __name__ == "__main__":
    img_pth = '/mnt_2/Datasets/MS2/sync_data/_2021-08-13-21-36-10/thr_normalized/img_left'
    img_pth = '/mnt_2/Datasets/MS2/sync_data/_2021-08-06-16-19-00/thr/img_left'
    visualize_value_image(img_pth, 400, normalize=True)