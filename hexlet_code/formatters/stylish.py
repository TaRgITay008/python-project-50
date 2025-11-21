def stringify(value, depth):
    """Convert value to string with proper formatting."""
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, dict):
        return format_nested(value, depth + 1)
    return str(value)


def format_nested(data, depth):
    """Format nested dictionary."""
    indent = '  ' * depth
    lines = []
    for key, value in sorted(data.items()):
        formatted_value = stringify(value, depth + 1)
        lines.append(f"{indent}  {key}: {formatted_value}")
    result = '\n'.join(lines)
    return f"{{\n{result}\n{indent}}}"


def format_stylish(diff, depth=0):
    """Format diff tree to stylish string."""
    indent = '  ' * depth
    lines = []
    
    # Check if we have nested structures at top level
    has_nested_top_level = any(node['type'] == 'nested' for node in diff) if depth == 0 else False
    
    for i, node in enumerate(diff):
        key = node['key']
        type_ = node['type']
        
        if type_ == 'nested':
            children = format_stylish(node['children'], depth + 2)
            lines.append(f"{indent}  {key}: {children}")
        elif type_ == 'added':
            value = stringify(node['value'], depth + 1)
            lines.append(f"{indent}  + {key}: {value}")
        elif type_ == 'removed':
            value = stringify(node['value'], depth + 1)
            lines.append(f"{indent}  - {key}: {value}")
        elif type_ == 'unchanged':
            value = stringify(node['value'], depth + 1)
            lines.append(f"{indent}    {key}: {value}")
        elif type_ == 'changed':
            old_value = stringify(node['old_value'], depth + 1)
            new_value = stringify(node['new_value'], depth + 1)
            lines.append(f"{indent}  - {key}: {old_value}")
            lines.append(f"{indent}  + {key}: {new_value}")
        
        # Add empty line between top-level NESTED blocks only
        if depth == 0 and has_nested_top_level and i < len(diff) - 1:
            lines.append('')
    
    result = '\n'.join(lines)
    if depth == 0:
        return f"{{\n{result}\n}}\n"
    return f"{{\n{result}\n{indent}}}"
