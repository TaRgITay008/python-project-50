#!/usr/bin/env python3
"""Module for building diff between two data structures."""


def is_dict(value):
    """Check if value is a dictionary."""
    return isinstance(value, dict)


def build_diff(data1, data2):
    """Build diff between two dictionaries recursively."""
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = {}

    for key in keys:
        value1 = data1.get(key)
        value2 = data2.get(key)

        if key not in data2:
            diff[key] = {'type': 'removed', 'value': value1}
        elif key not in data1:
            diff[key] = {'type': 'added', 'value': value2}
        elif is_dict(value1) and is_dict(value2):
            diff[key] = {
                'type': 'nested',
                'children': build_diff(value1, value2)
            }
        elif value1 == value2:
            diff[key] = {'type': 'unchanged', 'value': value1}
        else:
            diff[key] = {
                'type': 'changed',
                'old_value': value1,
                'new_value': value2
            }
    return diff
