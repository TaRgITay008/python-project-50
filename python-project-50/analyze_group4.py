import sys
sys.path.insert(0, '.')
from hexlet_code.scripts.generate_diff import generate_diff

result = generate_diff('tests/fixtures/file1_hexlet.yml', 'tests/fixtures/file2_hexlet.yml')

# Найдем group4 в выводе
in_group4 = False
group4_lines = []
for line in result.split('\n'):
    if 'group4:' in line:
        in_group4 = True
        group4_lines.append(line)
    elif in_group4:
        group4_lines.append(line)
        if '}' in line and not line.strip().startswith(('+', '-')):
            break

print("=" * 60)
print("ВЫВОД GROUP4 ИЗ НАШЕГО ГЕНЕРАТОРА")
print("=" * 60)
for line in group4_lines:
    print(line)

print("\n" + "=" * 60)
print("ЧТО ДОЛЖНО БЫТЬ (из ошибки Hexlet)")
print("=" * 60)
hexlet_group4 = '''    group4: {
      - default: null
      + default: 
      - foo: 0
      + foo: null
      - isNested: false
      + isNested: none
      + key: false
        nest: {
          - bar: 
          + bar: 0
          - isNested: true
        }
      + someKey: true
      - type: bas
      + type: bar
    }'''
print(hexlet_group4)

print("\n" + "=" * 60)
print("РАЗЛИЧИЯ")
print("=" * 60)
