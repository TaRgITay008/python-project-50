def render_plain(diff):
    def format_value(value):
        if isinstance(value, dict):
            return "[complex value]"
        if isinstance(value, str):
            return f"'{value}'"
        if value is True:
            return "true"
        if value is False:
            return "false"
        if value is None:
            return "null"
        return str(value)

    lines = []

    def walk(node, path=""):
        for key in sorted(node.keys()):
            data = node[key]
            t = data["type"]
            prop = f"{path}{key}"

            if t == "nested":
                walk(data["children"], prop + ".")

            elif t == "added":
                val = format_value(data["value"])
                lines.append(f"Property '{prop}' was added with value: {val}")

            elif t == "removed":
                lines.append(f"Property '{prop}' was removed")

            elif t == "changed":
                old = format_value(data["old_value"])
                new = format_value(data["new_value"])
                lines.append(
                    f"Property '{prop}' was updated. From {old} to {new}"
                )

    walk(diff)
    return "\n".join(lines)
