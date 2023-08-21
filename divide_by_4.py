def write_to_multiple_of_4(input_file, output_file):
    with open(input_file, 'r') as input_file_handle:
        lines = input_file_handle.readlines()

    with open(output_file, 'w') as output_file_handle:
        for i, line in enumerate(lines, 1):
            if i % 4 == 0:
                output_file_handle.write(line)

# Example usage:
if __name__ == "__main__":
    input_file_name = "splits_bj/val_rgb_clear_with_gt.txt"
    output_file_name = "splits_bj/val_rgb_clear_with_gt_4.txt"
    write_to_multiple_of_4(input_file_name, output_file_name)