#!/usr/bin/env python3
import argparse
from hexlet_code.scripts.parsers.parser import parse_file
from hexlet_code.diff_builder import build_diff
from hexlet_code.formatters import format_stylish, format_plain, format_json

def get_formatter(format_name):
    """Get formatter function by name."""
    formatters = {
        'stylish': format_stylish,
        'plain': format_plain,
        'json': format_json,
    }
    return formatters.get(format_name)


def generate_diff(file1_path, file2_path, format_name='stylish'):
    """Generate diff between two files."""
    data1 = parse_file(file1_path)
    data2 = parse_file(file2_path)

    diff = build_diff(data1, data2)
    
    formatter = get_formatter(format_name)
    if formatter:
        return formatter(diff)
    else:
        return f"Format '{format_name}' is not supported"


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
