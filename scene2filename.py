import os
modality = 'thr'
input_file = 'MS2dataset/test_rainy_list.txt'
sort = input_file.split('/')[1][:-8]
output_file = sort+ modality +'_with_gt.txt'  # Replace 'file_names.txt' with the desired output file name


with open(input_file, 'r') as file_in, open(output_file, 'w') as file_out:
    for line in file_in:
        if '_2021-08-13-15-42-41' not in line:
            folder_path = os.path.join('sync_data',line.rstrip('\n'), modality+'/img_left')
            file_names = os.listdir(os.path.join('/mnt_2/Datasets/MS2/',folder_path))

            for name in file_names:
                img_path = os.path.join(folder_path, name)
                gt_path = img_path.replace('sync_data','proj_depth').replace('img_left', 'depth_filtered')
                modified_name = f"{img_path} {gt_path}"
                file_out.write(modified_name + '\n')
