def format_value(value):
    """Format a single value."""
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)


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
            lines.append(f"{indent}  + {key}: {format_value(node['value'])}")
        elif node_type == 'removed':
            lines.append(f"{indent}  - {key}: {format_value(node['value'])}")
        elif node_type == 'unchanged':
            lines.append(f"{indent}    {key}: {format_value(node['value'])}")
        elif node_type == 'changed':
            lines.append(f"{indent}  - {key}: {format_value(node['old_value'])}")
            lines.append(f"{indent}  + {key}: {format_value(node['new_value'])}")

    result = '\n'.join(lines)
    return f"{{\n{result}\n{indent}}}"
