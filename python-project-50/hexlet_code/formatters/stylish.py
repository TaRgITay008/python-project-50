def format_stylish(diff, depth=0):
    indent = "    " * depth
    lines = []
    
    for node in sorted(diff, key=lambda x: x["name"]):
        key = node["name"]
        state = node["action"]
        
        if state == "nested":
            children = node["children"]
            lines.append(f"{indent}    {key}: {{")
            lines.append(format_stylish(children, depth + 1))
            lines.append(f"{indent}    }}")
        elif state == "added":
            value = stringify(node["new_value"], depth + 1)
            lines.append(f"{indent}  + {key}: {value}")
        elif state == "removed":
            value = stringify(node["old_value"], depth + 1)
            lines.append(f"{indent}  - {key}: {value}")
        elif state == "changed":
            old_value = stringify(node["old_value"], depth + 1)
            new_value = stringify(node["new_value"], depth + 1)
            lines.append(f"{indent}  - {key}: {old_value}")
            lines.append(f"{indent}  + {key}: {new_value}")
        elif state == "unchanged":
            value = stringify(node["value"], depth + 1)
            lines.append(f"{indent}    {key}: {value}")
    
    if depth == 0:
        return "{\n" + "\n".join(lines) + "\n}"
    return "\n".join(lines)


def stringify(value, depth):
    if isinstance(value, dict):
        return stringify_dict(value, depth)
    elif value is None:
        return "null"
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, (int, float)):
        return str(value)
    elif value == "":
        return ""
    else:
        return str(value)


def stringify_dict(value, depth):
    if not value:
        return "{}"
    
    indent = "    " * depth
    lines = []
    for key, val in sorted(value.items()):
        formatted = stringify(val, depth + 1)
        lines.append(f"{indent}    {key}: {formatted}")
    return "{\n" + "\n".join(lines) + "\n" + indent + "}"
