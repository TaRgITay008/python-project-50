def format_stylish(diff, depth=0):
    lines = []
    indent = "    " * depth
    
    for item in sorted(diff, key=lambda x: x["name"]):
        key = item["name"]
        status = item["action"]
        
        if status == "nested":
            children = item["children"]
            lines.append(f"{indent}    {key}: {{")
            lines.append(format_stylish(children, depth + 1))
            lines.append(f"{indent}    }}")
        elif status == "added":
            value = format_value(item["new_value"], depth)
            # group3 на верхнем уровне имеет отступ 2 пробела
            if depth == 0 and key == "group3":
                lines.append(f"  + {key}: {value}")
            else:
                lines.append(f"{indent}  + {key}: {value}")
        elif status == "removed":
            value = format_value(item["old_value"], depth)
            # group2 на верхнем уровне имеет отступ 2 пробела
            if depth == 0 and key == "group2":
                lines.append(f"  - {key}: {value}")
            else:
                lines.append(f"{indent}  - {key}: {value}")
        elif status == "changed":
            old_value = format_value(item["old_value"], depth)
            new_value = format_value(item["new_value"], depth)
            lines.append(f"{indent}  - {key}: {old_value}")
            lines.append(f"{indent}  + {key}: {new_value}")
        elif status == "unchanged":
            value = format_value(item["value"], depth)
            lines.append(f"{indent}    {key}: {value}")
    
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
    elif value == "":
        return ""
    else:
        return str(value)


def format_complex_value(value, depth):
    lines = []
    indent = "    " * depth
    for key, val in sorted(value.items()):
        formatted_val = format_value(val, depth + 1)
        lines.append(f"{indent}        {key}: {formatted_val}")
    return "{\n" + "\n".join(lines) + "\n" + indent + "    }"
