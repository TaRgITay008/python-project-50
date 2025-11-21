#!/usr/bin/env python3
import os
from argparse import ArgumentParser

from hexlet_code.diff_builder import build_diff
from hexlet_code.formatters.json import format_json
from hexlet_code.formatters.plain import format_plain
from hexlet_code.formatters.stylish import format_stylish
from hexlet_code.scripts.parsers.parser import parse_file


def get_format(name):
    formats = {
        'stylish': format_stylish,
        'plain': format_plain,
        'json': format_json
    }
    return formats.get(name, format_stylish)


def generate_diff(file_path1, file_path2, format_name='stylish'):
    """Generate difference between two files."""
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)
    diff = build_diff(data1, data2)
    formatter = get_format(format_name)
    return formatter(diff)


def main():
    parser = ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', default='stylish',
                        help='set format of output: stylish, plain, json')
    args = parser.parse_args()

    if not os.path.exists(args.first_file):
        print(f"Error: File {args.first_file} does not exist")
        return 1
    if not os.path.exists(args.second_file):
        print(f"Error: File {args.second_file} does not exist")
        return 1

    try:
        diff = generate_diff(args.first_file, args.second_file, args.format)
        print(diff)
    except Exception as e:
        print(f"Error: {e}")
        return 1

    return 0


if __name__ == '__main__':
    main()
