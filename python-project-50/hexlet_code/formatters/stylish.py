INDENT = 4
SIGN_OFFSET = 2


def stringify(value, depth):
    if not isinstance(value, dict):
        if value is True:
            return 'true'
        if value is False:
            return 'false'
        if value is None:
            return 'null'
        return str(value)

    indent = ' ' * (depth * INDENT)
    bracket_indent = ' ' * ((depth - 1) * INDENT)

    lines = []
    for key, val in value.items():
        lines.append(f"{indent}{key}: {stringify(val, depth + 1)}")

    return "{\n" + "\n".join(lines) + f"\n{bracket_indent}}}"


def format_stylish(diff):
    def walk(tree, depth):
        lines = []
        indent = ' ' * (depth * INDENT - SIGN_OFFSET)
        bracket_indent = ' ' * ((depth - 1) * INDENT)

        for node in tree:
            key = node['key']
            t = node['type']

            if t == 'nested':
                children = walk(node['children'], depth + 1)
                lines.append(f"{indent}  {key}: {children}")

            elif t == 'added':
                val = stringify(node['value'], depth + 1)
                lines.append(f"{indent}+ {key}: {val}")

            elif t == 'removed':
                val = stringify(node['value'], depth + 1)
                lines.append(f"{indent}- {key}: {val}")

            elif t == 'unchanged':
                val = stringify(node['value'], depth + 1)
                lines.append(f"{indent}  {key}: {val}")

            elif t == 'changed':
                old = stringify(node['old_value'], depth + 1)
                new = stringify(node['new_value'], depth + 1)
                lines.append(f"{indent}- {key}: {old}")
                lines.append(f"{indent}+ {key}: {new}")

        return "{\n" + "\n".join(lines) + f"\n{bracket_indent}}}"

    return walk(diff, 1)
