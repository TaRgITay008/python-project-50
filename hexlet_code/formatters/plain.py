def to_string(value):
    """Convert value to string representation for plain format."""
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, str):
        return f"'{value}'"
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)


def format_plain(diff, path=''):
    """Format diff as plain text."""
    lines = []

    for node in diff:
        current_path = f"{path}.{node['key']}" if path else node['key']
        node_type = node['type']

        if node_type == 'nested':
            lines.append(format_plain(node['children'], current_path))
        elif node_type == 'added':
            lines.append(f"Property '{current_path}' was added with value: "
                        f"{to_string(node['value'])}")
        elif node_type == 'removed':
            lines.append(f"Property '{current_path}' was removed")
        elif node_type == 'changed':
            lines.append(f"Property '{current_path}' was updated. "
                        f"From {to_string(node['old_value'])} to "
                        f"{to_string(node['new_value'])}")

    result = '\n'.join(line for line in lines if line)
    return result + '\n' if result else result
