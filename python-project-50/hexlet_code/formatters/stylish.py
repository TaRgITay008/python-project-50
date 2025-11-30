def format_stylish(diff, depth=0):
    lines = []
    indent = "    " * depth  # 4 пробела на уровень
    for item in diff:
        name = item["name"]
        action = item["action"]

        if action == "nested":
            nested_diff = item["children"]
            lines.append(f"{indent}    {name}: {{")  # 4 пробела отступа
            formatted_nested = format_stylish(nested_diff, depth + 1)
            lines.append(formatted_nested)
            lines.append(f"{indent}    }}")
        elif action == "added":
            new_value = format_value(item["new_value"], depth + 1)
            lines.append(f"{indent}  + {name}: {new_value}")  # 2 пробела перед +/-
        elif action == "removed":
            old_value = format_value(item["old_value"], depth + 1)
            lines.append(f"{indent}  - {name}: {old_value}")
        elif action == "changed":
            old_value = format_value(item["old_value"], depth + 1)
            new_value = format_value(item["new_value"], depth + 1)
            lines.append(f"{indent}  - {name}: {old_value}")
            lines.append(f"{indent}  + {name}: {new_value}")
        elif action == "unchanged":
            value = format_value(item["value"], depth + 1)
            lines.append(f"{indent}    {name}: {value}")  # 4 пробела для неизмененных

    if depth == 0:
        return "{\n" + "\n".join(lines) + "\n}"
    else:
        return "\n".join(lines)


def format_value(value, indent_level=0):
    if value is None:
        return 'null'
    elif value == '':  # Специальная обработка пустой строки
        return ''
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, (int, float)):
        return str(value)
    elif isinstance(value, dict):
        return format_dict(value, indent_level)
    else:
        return str(value)


def format_dict(dictionary, indent_level):
    lines = []
    indent = "    " * indent_level  # 4 пробела на уровень
    for key, value in dictionary.items():
        formatted_value = format_value(value, indent_level + 1)
        lines.append(f"{indent}    {key}: {formatted_value}")  # 4 пробела отступа
    
    return "{\n" + "\n".join(lines) + "\n" + indent + "}"
