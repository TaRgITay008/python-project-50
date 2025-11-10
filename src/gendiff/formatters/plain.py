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
    
    # Отладочная информация
    print(f"DEBUG: build_plain called with diff type: {type(diff)}, path: '{path}'")
    
    # Обрабатываем разные структуры diff
    if isinstance(diff, dict):
        # Если это корневой узел с children
        if 'children' in diff:
            nodes = diff['children']
            print(f"DEBUG: Root node with {len(nodes)} children")
        # Если это обычный узел
        elif 'key' in diff and 'type' in diff:
            nodes = [diff]
            print(f"DEBUG: Single node: {diff['key']}")
        else:
            # Если это вложенная структура (как common: {children: [...]})
            nodes = []
            for key, value in diff.items():
                if isinstance(value, dict) and 'children' in value:
                    nodes.extend(value['children'])
                    print(f"DEBUG: Found nested structure '{key}' with {len(value['children'])} children")
    elif isinstance(diff, list):
        nodes = diff
        print(f"DEBUG: Direct list with {len(nodes)} nodes")
    else:
        nodes = []
        print(f"DEBUG: Unexpected diff type: {type(diff)}")
    
    for i, node in enumerate(nodes):
        print(f"DEBUG: Processing node {i}: {node}")
        
        if not isinstance(node, dict) or 'key' not in node:
            print(f"DEBUG: Skipping invalid node: {node}")
            continue
            
        key = node['key']
        current_path = f"{path}.{key}" if path else key
        node_type = node.get('type')
        
        print(f"DEBUG: Node key: '{key}', type: '{node_type}', path: '{current_path}'")
        
        if node_type == 'nested':
            children = node.get('children', [])
            print(f"DEBUG: Nested node, processing {len(children)} children")
            lines.extend(build_plain(children, current_path))
        elif node_type == 'added':
            value = format_value(node['value'])
            line = f"Property '{current_path}' was added with value: {value}"
            lines.append(line)
            print(f"DEBUG: Added: {line}")
        elif node_type == 'removed':
            line = f"Property '{current_path}' was removed"
            lines.append(line)
            print(f"DEBUG: Removed: {line}")
        elif node_type == 'updated':
            old_value = format_value(node['old_value'])
            new_value = format_value(node['new_value'])
            line = f"Property '{current_path}' was updated. From {old_value} to {new_value}"
            lines.append(line)
            print(f"DEBUG: Updated: {line}")
        elif node_type == 'unchanged':
            print(f"DEBUG: Skipping unchanged node: {key}")
        else:
            print(f"DEBUG: Unknown node type: {node_type}")
    
    return lines


def format_plain(diff):
    print("DEBUG: format_plain called")
    result = build_plain(diff)
    print(f"DEBUG: Final result: {result}")
    return '\n'.join(result)
