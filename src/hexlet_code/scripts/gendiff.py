#!/usr/bin/env python3
import argparse


def generate_diff(file1, file2, format_name='stylish'):
    """Generate diff between two files."""
    # Пока заглушка - реализуем на следующих шагах
    return f"Diff between {file1} and {file2} in {format_name} format"


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
