from hexlet_code.scripts.parsers.parser import parse_file
from hexlet_code.diff_builder import build_diff
from hexlet_code.formatters import format_diff

def generate_diff(file1, file2, format_name='stylish'):
    """
    Generate difference between two files
    """
    data1 = parse_file(file1)
    data2 = parse_file(file2)
    diff = build_diff(data1, data2)
    return format_diff(diff, format_name)
