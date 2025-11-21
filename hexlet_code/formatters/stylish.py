def format_value(value, depth=0):
    """Format a single value with proper nesting."""
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, dict):
        return format_dict(value, depth + 2)
    return str(value)


def format_dict(dictionary, depth):
    """Format dictionary as nested structure."""
    indent = '  ' * depth
    lines = []
    
    for key, value in sorted(dictionary.items()):
        formatted_value = format_value(value, depth)
        lines.append(f"{indent}  {key}: {formatted_value}")
    
    result = '\n'.join(lines)
    return f"{{\n{result}\n{indent}}}"


def format_stylish(diff, depth=0):
    """Format diff as stylish string."""
    indent = '  ' * depth
    lines = []

    for node in diff:
        key = node['key']
        node_type = node['type']

        if node_type == 'nested':
            formatted_children = format_stylish(node['children'], depth + 2)
            lines.append(f"{indent}  {key}: {formatted_children}")
        elif node_type == 'added':
            value = format_value(node['value'], depth)
            lines.append(f"{indent}  + {key}: {value}")
        elif node_type == 'removed':
            value = format_value(node['value'], depth)
            lines.append(f"{indent}  - {key}: {value}")
        elif node_type == 'unchanged':
            value = format_value(node['value'], depth)
            lines.append(f"{indent}    {key}: {value}")
        elif node_type == 'changed':
            old_value = format_value(node['old_value'], depth)
            new_value = format_value(node['new_value'], depth)
            lines.append(f"{indent}  - {key}: {old_value}")
            lines.append(f"{indent}  + {key}: {new_value}")

    result = '\n'.join(lines)
    if depth == 0:
        return f"{{\n{result}\n}}\n"
    return f"{{\n{result}\n{indent}}}"
