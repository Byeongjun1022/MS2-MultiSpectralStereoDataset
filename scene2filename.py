import os
modality = 'thr'
input_file = 'MS2dataset/test_rainy_list.txt'
sort = input_file.split('/')[1][:-8]
output_file = sort+ modality +'_rm.txt'  # Replace 'file_names.txt' with the desired output file name

extreme_scene = ['_2021-08-06-17-44-55', '_2021-08-13-21-18-04', '_2021-08-06-16-19-00','_2021-08-13-21-36-10',\
                '_2021-08-06-16-45-28' ,'_2021-08-13-22-03-03','_2021-08-06-17-10-27','_2021-08-13-22-27-31',\
                '_2021-08-06-16-59-13','_2021-08-06-17-21-04','_2021-08-13-22-36-41', '_2021-08-13-21-58-13']

def check_velocity(input_file, threshold):
    with open(input_file,'r') as file_in:
        lines = file_in.readlines()
        vel_x = float(lines[7].strip())
        vel_y = float(lines[8].strip())
        vel_z = float(lines[9].strip())

        vel = (vel_x**2 + vel_y**2 + vel_z**2)**(0.5)

        return vel > threshold

with open(input_file, 'r') as file_in, open(output_file, 'w') as file_out:
    for line in file_in:
        if '_2021-08-13-15-42-41' not in line:
        # if not any(keyword in line for keyword in extreme_scene) and '_2021-08-13-15-42-41' not in line:
            folder_path = os.path.join('sync_data',line.rstrip('\n'), modality+'/img_left')
            file_names = os.listdir(os.path.join('/mnt_2/Datasets/MS2/',folder_path))

            for name in file_names:
                scene_name = folder_path.split('/')[1]
                gps_pth = os.path.join('/mnt_2/Datasets/MS2/sync_data', scene_name, 'gps_imu/data', name.replace('png', 'txt'))
                if check_velocity(gps_pth, 1):
                    img_path = os.path.join(folder_path, name)
                    gt_path = img_path.replace('sync_data','proj_depth').replace('img_left', 'depth_filtered')
                    modified_name = f"{img_path} {gt_path}"
                    file_out.write(modified_name + '\n')

