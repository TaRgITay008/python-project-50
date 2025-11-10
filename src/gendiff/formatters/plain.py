def format_value(value):
    if isinstance(value, (dict, list)):
        return '[complex value]'
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, (int, float)):
        return str(value)
    return f"'{value}'"


def build_plain(diff, path=''):
    lines = []
    
    # Если diff - это корневой узел (словарь с children), берем children
    if isinstance(diff, dict) and 'children' in diff:
        nodes = diff['children']
    else:
        nodes = diff
    
    for node in nodes:
        key = node['key']
        current_path = f"{path}.{key}" if path else key
        node_type = node['type']
        
        if node_type == 'nested':
            lines.extend(build_plain(node['children'], current_path))
        elif node_type == 'added':
            value = format_value(node['value'])
            lines.append(
                f"Property '{current_path}' was added with value: {value}"
            )
        elif node_type == 'removed':
            lines.append(f"Property '{current_path}' was removed")
        elif node_type == 'updated':
            old_value = format_value(node['old_value'])
            new_value = format_value(node['new_value'])
            lines.append(
                f"Property '{current_path}' was updated. From {old_value} to {new_value}"
            )
        # unchanged nodes are skipped in plain format
    
    return lines


def format_plain(diff):
    result = build_plain(diff)
    return '\n'.join(result)
