#!/usr/bin/env python3
import argparse
from hexlet_code.parsers.parser import parse_file


def build_diff(data1, data2):
    """Build diff between two dictionaries."""
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = {}

    for key in keys:
        if key not in data2:
            diff[key] = {'type': 'removed', 'value': data1[key]}
        elif key not in data1:
            diff[key] = {'type': 'added', 'value': data2[key]}
        elif data1[key] == data2[key]:
            diff[key] = {'type': 'unchanged', 'value': data1[key]}
        else:
            diff[key] = {
                'type': 'changed',
                'old_value': data1[key],
                'new_value': data2[key]
            }
    return diff


def format_value(value):
    """Format value for stylish output."""
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return value


def format_stylish(diff):
    """Format diff in stylish format."""
    lines = []

    for key in sorted(diff.keys()):
        node = diff[key]

        if node['type'] == 'removed':
            value = format_value(node['value'])
            lines.append(f"  - {key}: {value}")
        elif node['type'] == 'added':
            value = format_value(node['value'])
            lines.append(f"  + {key}: {value}")
        elif node['type'] == 'unchanged':
            value = format_value(node['value'])
            lines.append(f"    {key}: {value}")
        elif node['type'] == 'changed':
            old_value = format_value(node['old_value'])
            new_value = format_value(node['new_value'])
            lines.append(f"  - {key}: {old_value}")
            lines.append(f"  + {key}: {new_value}")

    return '{\n' + '\n'.join(lines) + '\n}'


def generate_diff(file1_path, file2_path, format_name='stylish'):
    """Generate diff between two files."""
    data1 = parse_file(file1_path)
    data2 = parse_file(file2_path)

    diff = build_diff(data1, data2)

    if format_name == 'stylish':
        return format_stylish(diff)
    else:
        return f"Format {format_name} is not supported yet"


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
