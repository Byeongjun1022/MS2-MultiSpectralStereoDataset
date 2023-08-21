import os
folder_pth = '/mnt_2/Datasets/MS2/sync_data/_2021-08-06-11-37-46/gps_imu/data'

static_list = []

for i in range(len(os.listdir(folder_pth))):
    input_file = os.path.join(folder_pth, f'{i:06}.txt')
    with open(input_file,'r') as file_in:
        lines = file_in.readlines()
        vel_x = float(lines[7].strip())
        vel_y = float(lines[8].strip())
        vel_z = float(lines[9].strip())

        vel = (vel_x**2 + vel_y**2 + vel_z**2)**(0.5)

        if vel < 1:
            static_list.append(i)

output_file = 'static.txt'

with open(output_file,'w') as file_out:
    for i in range(len(static_list)):
        file_out.write(f'{static_list[i]}\n')
