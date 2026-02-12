from .stylish import render_stylish
from .plain import render_plain
from .json import render_json


def format_diff(diff, format_name='stylish'):
    if format_name == 'stylish':
        return render_stylish(diff)
    if format_name == 'plain':
        return render_plain(diff)
    if format_name == 'json':
        return render_json(diff)
    raise ValueError(f"Unknown format: {format_name}")
