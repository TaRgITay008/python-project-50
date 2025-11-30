def format_value(value, depth):
    if value is None:
        return "null"
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, dict):
        indent = "    " * (depth + 1)
        lines = []
        for key, val in value.items():
            formatted_value = format_value(val, depth + 1)
            lines.append(f"{indent}{key}: {formatted_value}")
        formatted = "\n".join(lines)
        end_indent = "    " * depth
        return f"{{\n{formatted}\n{end_indent}}}"
    if value == "":  # Для пустой строки возвращаем пустую строку
        return ""
    return str(value)

def format_stylish(diff, depth=0):
    indent = "    " * depth
    lines = []

    for item in diff:
        key = item["name"]
        action = item["action"]

        if action == "unchanged":
            value = format_value(item["value"], depth + 1)
            lines.append(f"{indent}    {key}: {value}")
        elif action == "added":
            value = format_value(item["new_value"], depth + 1)
            # Специальная обработка для пустых строк
            if value == "":
                lines.append(f"{indent}  + {key}: ")
            else:
                lines.append(f"{indent}  + {key}: {value}")
        elif action == "removed" or action == "deleted":
            value = format_value(item["old_value"], depth + 1)
            # Специальная обработка для пустых строк
            if value == "":
                lines.append(f"{indent}  - {key}: ")
            else:
                lines.append(f"{indent}  - {key}: {value}")
        elif action == "changed" or action == "modified":
            old_value = format_value(item["old_value"], depth + 1)
            new_value = format_value(item["new_value"], depth + 1)
            # Специальная обработка для пустых строк
            if old_value == "":
                lines.append(f"{indent}  - {key}: ")
            else:
                lines.append(f"{indent}  - {key}: {old_value}")
            if new_value == "":
                lines.append(f"{indent}  + {key}: ")
            else:
                lines.append(f"{indent}  + {key}: {new_value}")
        elif action == "nested":
            nested_diff = item["children"]
            formatted_nested = format_stylish(nested_diff, depth + 1)
            lines.append(f"{indent}    {key}: {formatted_nested}")

    result = "\n".join(lines)
    if depth == 0:
        return f"{{\n{result}\n}}"
    return f"{{\n{result}\n{indent}}}"
