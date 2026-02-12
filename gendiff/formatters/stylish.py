def get_indent(depth):
    return ' ' * (depth * 4)


def get_sign_indent(depth):
    return ' ' * (depth * 4 - 2)


def get_close_indent(depth):
    return ' ' * ((depth - 1) * 4)


def stringify(value, depth):
    if not isinstance(value, dict):
        if value is None:
            return "null"
        if value is True:
            return "true"
        if value is False:
            return "false"
        return str(value)

    lines = []
    for k, v in value.items():
        lines.append(
            f"{get_indent(depth + 1)}{k}: {stringify(v, depth + 1)}"
        )

    result = "\n".join(lines)
    return "{\n" + result + "\n" + get_indent(depth) + "}"


def stylish(tree, depth=1):
    lines = []

    for node in tree:
        key = node["key"]
        node_type = node["type"]

        if node_type == "nested":
            children = stylish(node["children"], depth + 1)
            lines.append(f"{get_indent(depth)}  {key}: {children}")

        elif node_type == "added":
            lines.append(
                f"{get_sign_indent(depth)}+ {key}: {stringify(node['value'], depth)}"
            )

        elif node_type == "removed":
            lines.append(
                f"{get_sign_indent(depth)}- {key}: {stringify(node['value'], depth)}"
            )

        elif node_type == "unchanged":
            lines.append(
                f"{get_indent(depth)}  {key}: {stringify(node['value'], depth)}"
            )

        elif node_type == "changed":
            lines.append(
                f"{get_sign_indent(depth)}- {key}: {stringify(node['old'], depth)}"
            )
            lines.append(
                f"{get_sign_indent(depth)}+ {key}: {stringify(node['new'], depth)}"
            )

    result = "\n".join(lines)
    return "{\n" + result + "\n" + get_close_indent(depth) + "}"
