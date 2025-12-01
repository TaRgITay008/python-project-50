def format_stylish(diff, depth=0):
    """Форматтер stylish с отладкой"""
    lines = []
    
    print(f"{'  ' * depth}Глубина: {depth}, элементов: {len(diff)}")
    
    for item in sorted(diff, key=lambda x: x["name"]):
        key = item["name"]
        status = item["action"]
        
        print(f"{'  ' * depth}Обработка: {key}, статус: {status}, глубина: {depth}")
        
        if status == "nested":
            children = item["children"]
            line = "    " * depth + f"    {key}: {{"
            print(f"{'  ' * depth}  -> Строка: {repr(line)}")
            lines.append(line)
            lines.append(format_stylish(children, depth + 1))
            lines.append("    " * depth + f"    }}")
        elif status == "added":
            value = format_value(item["new_value"], depth)
            line = "    " * depth + f"  + {key}: {value}"
            print(f"{'  ' * depth}  -> Строка: {repr(line)}")
            lines.append(line)
        elif status == "removed":
            value = format_value(item["old_value"], depth)
            line = "    " * depth + f"  - {key}: {value}"
            print(f"{'  ' * depth}  -> Строка: {repr(line)}")
            lines.append(line)
        elif status == "changed":
            old_value = format_value(item["old_value"], depth)
            new_value = format_value(item["new_value"], depth)
            lines.append("    " * depth + f"  - {key}: {old_value}")
            lines.append("    " * depth + f"  + {key}: {new_value}")
        elif status == "unchanged":
            value = format_value(item["value"], depth)
            line = "    " * depth + f"    {key}: {value}"
            print(f"{'  ' * depth}  -> Строка: {repr(line)}")
            lines.append(line)
    
    if depth == 0:
        return "{\n" + "\n".join(lines) + "\n}\n"
    return "\n".join(lines)
