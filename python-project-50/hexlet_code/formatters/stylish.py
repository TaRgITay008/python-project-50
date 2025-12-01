    def format_stylish(diff, depth=0):
        indent = "    " * depth
        lines = []
        for key, (action, value) in sorted(diff.items()):
            if action == "nested":
                lines.append(f"{indent}    {key}: {{")
                lines.append(format_stylish(value, depth + 1))
                lines.append(f"{indent}    }}")
            elif action == "added":
                lines.append(f"{indent}  + {key}: {format_value(value, depth + 1)}")
            elif action == "removed":
                lines.append(f"{indent}  - {key}: {format_value(value, depth + 1)}")
            elif action == "unchanged":
                lines.append(f"{indent}    {key}: {format_value(value, depth + 1)}")
            elif action == "changed":
                lines.append(f"{indent}  - {key}: {format_value(value[0], depth + 1)}")
                lines.append(f"{indent}  + {key}: {format_value(value[1], depth + 1)}")
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
        indent = "    " * depth
        lines = []
        for key, val in sorted(value.items()):
            lines.append(f"{indent}    {key}: {format_value(val, depth + 1)}")
        return "{\n" + "\n".join(lines) + "\n" + indent + "}"

