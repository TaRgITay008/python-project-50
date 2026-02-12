import sys
sys.path.insert(0, '.')
from hexlet_code.scripts.generate_diff import generate_diff

result = generate_diff('tests/fixtures/file1_hexlet.yml', 'tests/fixtures/file2_hexlet.yml')

print("=== ПРОВЕРКА ОТСТУПОВ ===")
for line in result.split('\n'):
    if '+ follow:' in line:
        spaces = len(line) - len(line.lstrip())
        print(f"Строка: '{line}'")
        print(f"Длина строки: {len(line)}")
        print(f"Отступ: {spaces} пробелов")
        print(f"Символы отступа: {repr(line[:spaces])}")
        break

print("\n=== ПРОВЕРКА GROUP4 ===")
in_group4 = False
for line in result.split('\n'):
    if 'group4:' in line:
        in_group4 = True
    if in_group4:
        print(line)
        if '}' in line and not line.strip().startswith(('+', '-')):
            break
