#!/usr/bin/env python3
import argparse
import json


def parse_file(file_path):
    """Read and parse JSON file."""
    with open(file_path) as file:
        return json.load(file)


def generate_diff(file1_path, file2_path, format_name='stylish'):
    """Generate diff between two files."""
    data1 = parse_file(file1_path)
    data2 = parse_file(file2_path)
    
    # Детальная информация о данных
    print("=== First File ===")
    for key, value in data1.items():
        print(f"  {key}: {value} (type: {type(value).__name__})")
    
    print("=== Second File ===")
    for key, value in data2.items():
        print(f"  {key}: {value} (type: {type(value).__name__})")
    
    print(f"Output format: {format_name}")
    
    return "Files parsed successfully"


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        default='stylish',
                        help='set format of output')
    
    args = parser.parse_args()
    
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
