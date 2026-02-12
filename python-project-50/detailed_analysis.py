import sys
sys.path.insert(0, '.')

from hexlet_code.scripts.gendiff import generate_diff

# Получим наш вывод
our_result = generate_diff('test_data/file1.json', 'test_data/file2.json')

# Прочитаем ожидаемый
with open('test_data/expected_result_json.txt', 'r') as f:
    expected = f.read()

print("Детальное сравнение отступов:")
print("=" * 80)

our_lines = our_result.strip().split('\n')
expected_lines = expected.strip().split('\n')

min_len = min(len(our_lines), len(expected_lines))

for i in range(min_len):
    our_line = our_lines[i]
    expected_line = expected_lines[i]
    
    if our_line != expected_line:
        our_spaces = len(our_line) - len(our_line.lstrip())
        exp_spaces = len(expected_line) - len(expected_line.lstrip())
        
        print(f"Строка {i}:")
        print(f"  Наш:      {our_spaces} пробелов: '{our_line}'")
        print(f"  Ожидаемый: {exp_spaces} пробелов: '{expected_line}'")
        print(f"  Разница:   {our_spaces - exp_spaces} пробелов")
        print()
        
        # Остановимся после нескольких различий
        if i > 20:
            break

print("\n" + "=" * 80)
print("Правила отступов из ожидаемого результата:")
print("-" * 80)

# Проанализируем паттерны
for i, line in enumerate(expected_lines[:50]):
    spaces = len(line) - len(line.lstrip())
    content = line.strip()
    
    if content.startswith('+ ') or content.startswith('- '):
        print(f"  +/- элементы: {spaces} пробелов (строка {i})")
    elif '{' in content and ':' in content and not content.startswith(('+', '-')):
        print(f"  Вложенные ключи: {spaces} пробелов (строка {i})")
    elif ':' in content and not content.startswith(('+', '-')) and '{' not in content:
        print(f"  Обычные ключи: {spaces} пробелов (строка {i})")
