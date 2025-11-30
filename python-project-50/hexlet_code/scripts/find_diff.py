def find_diff(data1, data2):
    diff = []
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))

    for key in all_keys:
        if key not in data2:
            diff.append({
                'name': key,
                'action': 'removed',
                'old_value': data1[key]
            })
        elif key not in data1:
            diff.append({
                'name': key,
                'action': 'added',
                'new_value': data2[key]
            })
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff.append({
                'name': key,
                'action': 'nested',
                'children': find_diff(data1[key], data2[key])
            })
        elif data1[key] == data2[key]:
            diff.append({
                'name': key,
                'action': 'unchanged',
                'value': data1[key]
            })
        else:
            diff.append({
                'name': key,
                'action': 'changed',
                'old_value': data1[key],
                'new_value': data2[key]
            })

    return diff
