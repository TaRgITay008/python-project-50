def format_stylish(diff, depth=0):
    lines = []

    for item in sorted(diff, key=lambda x: x["name"]):
        key = item["name"]
        status = item["action"]

        if status == "nested":
            children = item["children"]
            lines.append("    " * depth + f"    {key}: {{")
            lines.append(format_stylish(children, depth + 1))
            lines.append("    " * depth + f"    }}")
        elif status == "added":
            value = format_value(item["new_value"], depth)
            lines.append("    " * depth + f"  + {key}: {value}")
        elif status == "removed":
            value = format_value(item["old_value"], depth)
            lines.append("    " * depth + f"  - {key}: {value}")
        elif status == "changed":
            old_value = format_value(item["old_value"], depth)
            new_value = format_value(item["new_value"], depth)
            lines.append("    " * depth + f"  - {key}: {old_value}")
            lines.append("    " * depth + f"  + {key}: {new_value}")
        elif status == "unchanged":
            value = format_value(item["value"], depth)
            lines.append("    " * depth + f"    {key}: {value}")

    if depth == 0:
        return "{\n" + "\n".join(lines) + "\n}\n"  # <-- ИЗМЕНЕНИЕ ЗДЕСЬ!
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
    for key, val in sorted(value.items()):
        formatted_val = format_value(val, depth + 1)
        lines.append("    " * depth + f"        {key}: {formatted_val}")
    return "{\n" + "\n".join(lines) + "\n" + "    " * depth + "    }"
