#!/usr/bin/env python3
"""Plain formatter module."""


def format_value(value):
    """Format value for plain output."""
    if isinstance(value, (dict, list)):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    else:
        return str(value)


def build_plain_lines(diff, path=''):
    """Build lines for plain format recursively."""
    lines = []
    
    for key in sorted(diff.keys()):
        node = diff[key]
        current_path = f"{path}.{key}" if path else key
        
        if node['type'] == 'nested':
            nested_lines = build_plain_lines(node['children'], current_path)
            lines.extend(nested_lines)
        elif node['type'] == 'added':
            value = format_value(node['value'])
            lines.append(f"Property '{current_path}' was added with value: {value}")
        elif node['type'] == 'removed':
            lines.append(f"Property '{current_path}' was removed")
        elif node['type'] == 'changed':
            old_value = format_value(node['old_value'])
            new_value = format_value(node['new_value'])
            lines.append(f"Property '{current_path}' was updated. From {old_value} to {new_value}")
        # unchanged nodes are skipped in plain format
    
    return lines


def format_plain(diff):
    """Format diff in plain format."""
    lines = build_plain_lines(diff)
    return '\n'.join(lines)
