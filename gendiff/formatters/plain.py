def to_str(value):
    if isinstance(value, dict):
        return "[complex value]"
    if value is None:
        return "null"
    if value is True:
        return "true"
    if value is False:
        return "false"
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)


def walk(tree, path=""):
    lines = []

    for node in tree:
        key = node["key"]
        node_type = node["type"]
        new_path = f"{path}.{key}" if path else key

        if node_type == "nested":
            lines.extend(walk(node["children"], new_path))

        elif node_type == "added":
            lines.append(
                f"Property '{new_path}' was added with value: {to_str(node['value'])}"
            )

        elif node_type == "removed":
            lines.append(f"Property '{new_path}' was removed")

        elif node_type == "changed":
            lines.append(
                f"Property '{new_path}' was updated. "
                f"From {to_str(node['old'])} to {to_str(node['new'])}"
            )

    return lines


def render_plain(tree):
    return "\n".join(walk(tree))
