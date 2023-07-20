from PIL import Image
import os

def create_gif(seq_name, images, gif_filename, duration=100):
    # 'images' is a list of image file paths in the order you want them to appear in the GIF
    # 'gif_filename' is the output file name for the GIF
    # 'duration' is the duration (in milliseconds) between frames

    frames = []
    for image_path in images:
        img = Image.open(os.path.join(seq_name,image_path))
        frames.append(img)

    # Save the frames as a GIF
    frames[0].save(gif_filename,
                   format='GIF',
                   append_images=frames[1:],
                   save_all=True,
                   duration=duration,
                   loop=0)

if __name__ == "__main__":
    # Example usage:
    modal = 'rgb'
    seq_name = '/mnt_2/Datasets/MS2/sync_data/_2021-08-06-16-19-00/thr_normalized/img_left'
    if modal == 'rgb':
        seq_name = seq_name.replace('thr_normalized', 'rgb')
        output_gif = 'output_rain_rgb.gif'    
    else: output_gif = 'output_rain_thr.gif'
    image_paths =[]
    for i in range(80):
        i+=510
        image_paths.append(f'{i:06}.png')
    create_gif(seq_name, image_paths, output_gif)