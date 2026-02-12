def format_stylish(diff, depth=0):
    lines = []
    indent = "    " * depth
    
    for item in sorted(diff, key=lambda x: x["name"]):
        key = item["name"]
        status = item["action"]
        current_indent = "    " * depth
        
        if status == "nested":
            children = item["children"]
            lines.append(f"{current_indent}    {key}: {{")
            lines.append(format_stylish(children, depth + 1))
            lines.append(f"{current_indent}    }}")
        elif status == "added":
            value = format_value(item["new_value"], depth + 1)
            lines.append(f"{current_indent}   + {key}: {value}")  # 3 пробела!
        elif status == "removed":
            value = format_value(item["old_value"], depth + 1)
            lines.append(f"{current_indent}   - {key}: {value}")  # 3 пробела!
        elif status == "changed":
            old_value = format_value(item["old_value"], depth + 1)
            new_value = format_value(item["new_value"], depth + 1)
            lines.append(f"{current_indent}   - {key}: {old_value}")  # 3 пробела!
            lines.append(f"{current_indent}   + {key}: {new_value}")  # 3 пробела!
        elif status == "unchanged":
            value = format_value(item["value"], depth + 1)
            lines.append(f"{current_indent}    {key}: {value}")
    
    if depth == 0:
        return "{\n" + "\n".join(lines) + "\n}"
    return "\n".join(lines)


def format_value(value, depth):
    if isinstance(value, dict):
        return format_complex_value(value, depth)
    elif value is None:
        return "null"
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, (int, float)):
        return str(value)
    else:
        return str(value)


def format_complex_value(value, depth):
    if not value:
        return "{}"
    
    lines = []
    indent = "    " * depth
    
    for key, val in sorted(value.items()):
        formatted_val = format_value(val, depth + 1)
        lines.append(f"{indent}    {key}: {formatted_val}")
    
    return "{\n" + "\n".join(lines) + "\n" + indent + "}"
