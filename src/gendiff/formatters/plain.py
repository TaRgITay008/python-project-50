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
    
    # diff - это словарь, где ключи это имена групп, а значения содержат 'children'
    if isinstance(diff, dict):
        # Собираем все узлы из всех групп
        all_nodes = []
        for group_name, group_data in diff.items():
            if isinstance(group_data, dict) and 'children' in group_data:
                # Добавляем узлы из этой группы
                for node in group_data['children']:
                    all_nodes.append(node)
        
        # Теперь обрабатываем все узлы
        for node in all_nodes:
            if not isinstance(node, dict) or 'key' not in node:
                continue
                
            key = node['key']
            current_path = f"{path}.{key}" if path else key
            node_type = node.get('type')
            
            if node_type == 'nested':
                children = node.get('children', [])
                lines.extend(build_plain({f"nested_{key}": {'children': children}}, current_path))
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
