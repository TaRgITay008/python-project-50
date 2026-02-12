import sys
sys.path.insert(0, '.')
from hexlet_code.scripts.generate_diff import generate_diff

result = generate_diff('tests/fixtures/file1_hexlet.yml', 'tests/fixtures/file2_hexlet.yml')

# Найдем group4 в выводе
in_group4 = False
group4_lines = []
for line in result.split('\n'):
    if 'group4: {' in line:
        in_group4 = True
        group4_lines.append(line)
    elif in_group4 and '}' in line and not line.strip().startswith('+') and not line.strip().startswith('-'):
        group4_lines.append(line)
        break
    elif in_group4:
        group4_lines.append(line)

print("Наш порядок в group4:")
for line in group4_lines:
    print(line)
