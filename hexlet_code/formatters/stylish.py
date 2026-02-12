def render_stylish(diff):
    def stringify(value, depth):
        if not isinstance(value, dict):
            if value is True:
                return "true"
            if value is False:
                return "false"
            if value is None:
                return "null"
            return str(value)

        indent = " " * (depth * 4)
        bracket_indent = " " * ((depth - 1) * 4)
        lines = []
        for k, v in value.items():
            lines.append(f"{indent}    {k}: {stringify(v, depth + 1)}")
        return "{\n" + "\n".join(lines) + f"\n{bracket_indent}}}"

    def walk(node, depth):
        indent = " " * (depth * 4 - 2)
        bracket_indent = " " * ((depth - 1) * 4)
        lines = []

        for key in sorted(node.keys()):
            data = node[key]
            t = data["type"]

            if t == "nested":
                children = walk(data["children"], depth + 1)
                lines.append(f"{indent}  {key}: {children}")

            elif t == "added":
                val = stringify(data["value"], depth)
                lines.append(f"{indent}+ {key}: {val}")

            elif t == "removed":
                val = stringify(data["value"], depth)
                lines.append(f"{indent}- {key}: {val}")

            elif t == "changed":
                old = stringify(data["old_value"], depth)
                new = stringify(data["new_value"], depth)
                lines.append(f"{indent}- {key}: {old}")
                lines.append(f"{indent}+ {key}: {new}")

            elif t == "unchanged":
                val = stringify(data["value"], depth)
                lines.append(f"{indent}  {key}: {val}")

        return "{\n" + "\n".join(lines) + f"\n{bracket_indent}}}"

    return walk(diff, 1)
