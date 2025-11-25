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
            lines.append(f"{indent}  + {key}: {value}")
        elif action == "deleted":
            value = format_value(item["old_value"], depth + 1)
            lines.append(f"{indent}  - {key}: {value}")
        elif action == "modified":
            old_value = format_value(item["old_value"], depth + 1)
            new_value = format_value(item["new_value"], depth + 1)
            lines.append(f"{indent}  - {key}: {old_value}")
            lines.append(f"{indent}  + {key}: {new_value}")
        elif action == "nested":
            children = format_stylish(item["children"], depth + 1)
            lines.append(f"{indent}    {key}: {children}")
    
    result = "\n".join(lines)
    end_indent = "    " * depth
    return f"{{\n{result}\n{end_indent}}}"


def format_diff_stylish(diff):
    return format_stylish(diff)
