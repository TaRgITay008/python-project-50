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


def format_plain(diff, path=''):
    lines = []
    
    # Получаем список узлов из diff
    # diff может быть либо списком узлов, либо словарем с ключом 'children'
    if isinstance(diff, dict) and 'children' in diff:
        nodes = diff['children']
    else:
        nodes = diff
    
    for node in nodes:
        current_path = f"{path}.{node['key']}" if path else node['key']
        
        if node['type'] == 'nested':
            lines.extend(format_plain(node['children'], current_path))
        elif node['type'] == 'added':
            value = format_value(node['value'])
            lines.append(
                f"Property '{current_path}' was added with value: {value}"
            )
        elif node['type'] == 'removed':
            lines.append(f"Property '{current_path}' was removed")
        elif node['type'] == 'updated':
            old_value = format_value(node['old_value'])
            new_value = format_value(node['new_value'])
            lines.append(
                f"Property '{current_path}' was updated. From {old_value} to {new_value}"
            )
    
    return lines


def render_plain(diff):
    result = format_plain(diff)
    return '\n'.join(result)
