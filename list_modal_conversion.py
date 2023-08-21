
input_file_list = [ 'train_thr_rm.txt', 'val_thr_rm.txt', #'test_day_thr_rm.txt',
                   'test_night_thr_rm.txt', 'test_rainy_thr_rm.txt']
for input_file in input_file_list:
    # input_file = 'test_day_thr_rm.txt'
    output_file = input_file.replace('thr', 'rgb')

    with open(input_file, 'r') as file_in, open(output_file,'w') as file_out:
        for line in file_in:
            img_pth = line.split()[0].replace('thr','rgb')
            gt_pth = line.split()[1].replace('thr','rgb')
            modified_line = f'{img_pth} {gt_pth}'
            file_out.write(modified_line + '\n')