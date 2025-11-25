def format_stylish(diff, depth=0):
    """Format diff in stylish format with exact indentation"""
    lines = []
    indent = "  " * depth
    
    for key in sorted(diff.keys()):
        node = diff[key]
        node_type = node['type']
        
        if node_type == 'nested':
            lines.append(f"{indent}  {key}: {{")
            lines.extend(format_stylish(node['children'], depth + 2))
            lines.append(f"{indent}  }}")
        elif node_type == 'added':
            value_str = format_value(node['value'], depth + 2)
            lines.append(f"{indent}+ {key}: {value_str}")
        elif node_type == 'removed':
            value_str = format_value(node['value'], depth + 2)
            lines.append(f"{indent}- {key}: {value_str}")
        elif node_type == 'changed':
            old_value = format_value(node['old_value'], depth + 2)
            new_value = format_value(node['new_value'], depth + 2)
            lines.append(f"{indent}- {key}: {old_value}")
            lines.append(f"{indent}+ {key}: {new_value}")
        elif node_type == 'unchanged':
            value_str = format_value(node['value'], depth + 2)
            lines.append(f"{indent}  {key}: {value_str}")
    
    return lines

def format_value(value, depth=0):
    """Format value with proper indentation"""
    if isinstance(value, dict):
        lines = ["{"]
        for k, v in sorted(value.items()):
            value_str = format_value(v, depth + 2)
            lines.append(f"{'  ' * (depth + 1)}{k}: {value_str}")
        lines.append(f"{'  ' * depth}}}")
        return "\n".join(lines)
    elif value is None:
        return "null"
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, (int, str)):
        return str(value)
    else:
        return str(value)

def render_stylish(diff):
    """Render diff in stylish format"""
    if not diff:
        return "{}"
    
    formatted = format_stylish(diff)
    # ВАЖНО: добавляем перенос строки в конце!
    return "{\n" + "\n".join(formatted) + "\n}\n"
