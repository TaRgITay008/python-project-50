#!/usr/bin/env python3
"""Stylish formatter module."""


def format_value(value, depth):
    """Format value for stylish output."""
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        return format_dict(value, depth + 1)
    else:
        return value


def format_dict(dictionary, depth):
    """Format dictionary for stylish output."""
    indent = '    ' * depth
    lines = ['{']
    
    for key, value in sorted(dictionary.items()):
        formatted_value = format_value(value, depth)
        lines.append(f'{indent}    {key}: {formatted_value}')
    
    lines.append(f'{indent}}}')
    return '\n'.join(lines)


def format_stylish(diff, depth=0):
    """Format diff in stylish format."""
    indent = '    ' * depth
    lines = ['{']
    
    for key in sorted(diff.keys()):
        node = diff[key]
        current_indent = f'{indent}  '
        
        if node['type'] == 'nested':
            formatted_children = format_stylish(node['children'], depth + 1)
            lines.append(f'{current_indent}  {key}: {formatted_children}')
        elif node['type'] == 'added':
            value = format_value(node['value'], depth)
            lines.append(f'{current_indent}+ {key}: {value}')
        elif node['type'] == 'removed':
            value = format_value(node['value'], depth)
            lines.append(f'{current_indent}- {key}: {value}')
        elif node['type'] == 'unchanged':
            value = format_value(node['value'], depth)
            lines.append(f'{current_indent}  {key}: {value}')
        elif node['type'] == 'changed':
            old_value = format_value(node['old_value'], depth)
            new_value = format_value(node['new_value'], depth)
            lines.append(f'{current_indent}- {key}: {old_value}')
            lines.append(f'{current_indent}+ {key}: {new_value}')
    
    lines.append(f'{indent}}}')
    return '\n'.join(lines)
