from hexlet_code.formatters.json_formatter import format_diff_json
from hexlet_code.formatters.plain import format_diff_plain
from hexlet_code.formatters.stylish import format_stylish as format_diff_stylish


def format_identifier(diff, formatter):
    if formatter == 'stylish':
        return format_diff_stylish(diff)
    if formatter == 'plain':
        return format_diff_plain(diff)
    if formatter == 'json':
        return format_diff_json(diff)
    else:
        raise ValueError(f"Unsupported formatter: {formatter}")
