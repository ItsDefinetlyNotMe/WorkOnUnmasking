import os
import random
import argparse

def parse_command_line():
    parser = argparse.ArgumentParser(description="Get file name and number from command line arguments")
    parser.add_argument("-l", "--number", type=int, help="A number")
    parser.add_argument("-f", "--path", help="A file path")

    args = parser.parse_args()
    return args.number, args.path

def count_lines(filename):
        line_count = 0
        with open(filename, 'r') as file:
            for line in file:
                line_count += 1
        return line_count

def select_specific_lines(input_filename, line_numbers):
    texts_from_lines = []
    with open(input_filename, 'r') as input_file:
        for line_number, line in enumerate(input_file, 1):
            if line_number in line_numbers:
                texts_from_lines.append(line)
    return texts_from_lines


number, file_path = parse_command_line()
path = os.path.dirname(file_path)

file_base = file_path
file_truth = file_base[:-6] + '-truth.jsonl'
line_count = count_lines(file_truth)


samplesize = number

if samplesize > line_count:
    print("You requested more lines than there are in the file.")
else:
    random_lines = random.sample(range(1, line_count + 1), samplesize)
    random_lines.sort()

    lines_base = select_specific_lines(file_base, random_lines)
    lines_truth = select_specific_lines(file_truth, random_lines)

    # Create a new file and save the selected lines
    with open(os.path.join(path, 'Pan20-short.jsonl'), 'w') as new_file:
        for line_number in range(len(lines_base)):
            new_file.write(lines_base[line_number])

    with open(os.path.join(path, 'Pan20-short-truth.jsonl'), 'w') as new_file:
        for line_number in range(len(lines_truth)):
            new_file.write(lines_truth[line_number])