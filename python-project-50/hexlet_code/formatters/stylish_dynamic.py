def format_stylish(diff, depth=0):
    lines = []
    indent = "    " * depth
    
    for item in diff:
        name = item["name"]
        action = item["action"]

        if action == "nested":
            nested_diff = item["children"]
            lines.append(f"{indent}    {name}: {{")
            lines.append(format_stylish(nested_diff, depth + 1))
            lines.append(f"{indent}    }}")
        elif action == "added":
            new_value = format_value(item["new_value"], depth)
            lines.append(f"{indent}  + {name}: {new_value}")
        elif action == "removed":
            old_value = format_value(item["old_value"], depth)
            lines.append(f"{indent}  - {name}: {old_value}")
        elif action == "changed":
            old_value = format_value(item["old_value"], depth)
            new_value = format_value(item["new_value"], depth)
            lines.append(f"{indent}  - {name}: {old_value}")
            lines.append(f"{indent}  + {name}: {new_value}")
        elif action == "unchanged":
            value = format_value(item["value"], depth)
            lines.append(f"{indent}    {name}: {value}")

    if depth == 0:
        return "{\n" + "\n".join(lines) + "\n}\n"
    else:
        return "\n".join(lines)


def format_value(value, depth):
    if value is None:
        return 'null'
    elif value == '':  # Special case for empty string
        return ''  # Пробел добавится автоматически
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, (int, float)):
        return str(value)
    elif isinstance(value, dict):
        return format_dict(value, depth)
    else:
        return str(value)


def format_dict(dictionary, depth):
    lines = []
    indent = "    " * depth
    
    for key, value in sorted(dictionary.items()):
        formatted_value = format_value(value, depth + 1)
        lines.append(f"{indent}        {key}: {formatted_value}")
    
    formatted_lines = "\n".join(lines)
    return f"{{\n{formatted_lines}\n{indent}    }}"
