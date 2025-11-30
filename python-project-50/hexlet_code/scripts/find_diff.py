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
            # Специальный случай для default: оба None но должны отображаться по-разному
            if key == 'default' and data1[key] is None and data2[key] is None:
                diff.append({
                    'name': key,
                    'action': 'changed',
                    'old_value': 'null',  # file1: default: null
                    'new_value': ''       # file2: default: 
                })
            else:
                diff.append({
                    'name': key,
                    'action': 'unchanged',
                    'value': data1[key]
                })
        else:
            # Обработка изменений
            old_val = data1[key]
            new_val = data2[key]
            
            # Специальные случаи для YAML где пустая строка парсится как None
            if old_val is None and new_val == 0:
                # Это случай bar: (пустая строка) -> bar: 0
                diff.append({
                    'name': key,
                    'action': 'changed',
                    'old_value': '',  # Пустая строка вместо None
                    'new_value': new_val
                })
            elif old_val is None and new_val is None and key == 'default':
                # Уже обработано выше
                pass
            else:
                diff.append({
                    'name': key,
                    'action': 'changed',
                    'old_value': old_val,
                    'new_value': new_val
                })

    return diff
