from hexlet_code.formatters.stylish import render_stylish

def format_diff(diff, format_name='stylish'):
    """
    Format diff using specified formatter
    """
    if format_name == 'stylish':
        return render_stylish(diff)
    else:
        raise ValueError(f"Unknown format: {format_name}")
