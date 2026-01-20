from hexlet_code.parsers import parse_data
from hexlet_code.scripts.find_diff import find_diff
from hexlet_code.formatters.stylish import format_stylish
from hexlet_code.formatters.plain import format_diff_plain
from hexlet_code.formatters.json_formatter import format_diff_json


def generate_diff(file_path1, file_path2, formatter='stylish'):
    """
    Generate difference between two files.
    
    Args:
        file_path1: Path to first file
        file_path2: Path to second file
        formatter: Output format ('stylish', 'plain', or 'json')
    
    Returns:
        Formatted difference string
    """
    data1 = parse_data(file_path1)
    data2 = parse_data(file_path2)

    diff = find_diff(data1, data2)

    if formatter == 'stylish':
        return format_stylish(diff)
    elif formatter == 'plain':
        return format_diff_plain(diff)
    elif formatter == 'json':
        return format_diff_json(diff)
    else:
        raise ValueError(f"Unsupported format: {formatter}")
