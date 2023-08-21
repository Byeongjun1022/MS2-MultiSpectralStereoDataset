import os
modality = 'rgb'
input_file = 'MS2dataset/val_list.txt'
sort = input_file.split('/')[1][:-8]
output_file = sort+ modality +'_clear_with_gt.txt'  # Replace 'file_names.txt' with the desired output file name

extreme_scene = ['_2021-08-06-17-44-55', '_2021-08-13-21-18-04', '_2021-08-06-16-19-00','_2021-08-13-21-36-10',\
                '_2021-08-06-16-45-28' ,'_2021-08-13-22-03-03','_2021-08-06-17-10-27','_2021-08-13-22-27-31',\
                '_2021-08-06-16-59-13','_2021-08-06-17-21-04','_2021-08-13-22-36-41', '_2021-08-13-21-58-13']

with open(input_file, 'r') as file_in, open(output_file, 'w') as file_out:
    for line in file_in:
        if not any(keyword in line for keyword in extreme_scene) and '_2021-08-13-15-42-41' not in line:
            folder_path = os.path.join('sync_data',line.rstrip('\n'), modality+'/img_left')
            file_names = os.listdir(os.path.join('/mnt_2/Datasets/MS2/',folder_path))

            for name in file_names:
                img_path = os.path.join(folder_path, name)
                gt_path = img_path.replace('sync_data','proj_depth').replace('img_left', 'depth_filtered')
                modified_name = f"{img_path} {gt_path}"
                file_out.write(modified_name + '\n')

