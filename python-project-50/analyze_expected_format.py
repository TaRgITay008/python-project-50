with open('test_data/expected_result_json.txt', 'r') as f:
    expected = f.read()

print("Ожидаемый результат (первые 30 строк):")
print("=" * 60)

lines = expected.strip().split('\n')
for i, line in enumerate(lines[:30]):
    if line.strip():  # только непустые строки
        spaces = len(line) - len(line.lstrip())
        content = line.strip()
        
        # Определяем тип строки
        if content.startswith('+'):
            line_type = "added"
        elif content.startswith('-'):
            line_type = "removed" 
        elif '{' in content and ':' in content:
            line_type = "nested_open"
        elif '}' in content:
            line_type = "close_brace"
        elif ':' in content:
            line_type = "regular"
        else:
            line_type = "other"
            
        print(f"{i:3}: {spaces:2} пробелов | {line_type:12} | '{line}'")

print("\n" + "=" * 60)
print("Анализ ключевых строк:")
print("-" * 60)

key_lines = [
    (i, line) for i, line in enumerate(lines) 
    if 'group2' in line or 'follow' in line or 'abc: 12345' in line
]

for i, line in key_lines:
    spaces = len(line) - len(line.lstrip())
    print(f"{i:3}: {spaces:2} пробелов | '{line}'")
