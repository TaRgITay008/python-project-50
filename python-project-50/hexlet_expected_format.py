import sys
sys.path.insert(0, '.')

from hexlet_code.scripts.generate_diff import generate_diff

# Это пример из ошибки Hexlet
expected_sample = '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: {
            key: value
        }
    }
}'''

result = generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml')

print("Сравниваем с образцом из ошибки:")
print("=" * 50)

# Проверяем первые несколько строк
result_lines = result.split('\n')[:15]
expected_lines = expected_sample.split('\n')

for i, (r, e) in enumerate(zip(result_lines, expected_lines)):
    if r != e:
        print(f"Строка {i}:")
        print(f"  Наш:      '{r}'")
        print(f"  Ожидаем:  '{e}'")
        print(f"  Отступы:  наш={len(r)-len(r.lstrip())}, ожидаем={len(e)-len(e.lstrip())}")
        break
