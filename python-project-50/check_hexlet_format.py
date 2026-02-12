import sys
sys.path.insert(0, '.')

from hexlet_code.scripts.generate_diff import generate_diff

# Берем первую часть ожидаемого результата прямо из ошибки Hexlet
expected_hexlet = '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: {
            key: value
        }
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: too much
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }'''

result = generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml')

print("Проверка первых 30 строк:")
print("=" * 60)

result_lines = result.split('\n')[:30]
expected_lines = expected_hexlet.split('\n')

for i, (r, e) in enumerate(zip(result_lines, expected_lines)):
    if r != e:
        print(f"\nСтрока {i}:")
        print(f"  Наш:      '{r}'")
        print(f"  Hexlet:   '{e}'")
        
        # Подсчитываем отступы
        our_spaces = len(r) - len(r.lstrip())
        exp_spaces = len(e) - len(e.lstrip())
        print(f"  Отступы:  наш={our_spaces}, hexlet={exp_spaces}")
        
        # Показываем ASCII коды для первых разных символов
        if len(r) > 0 and len(e) > 0:
            for j in range(min(len(r), len(e))):
                if r[j] != e[j]:
                    print(f"  Разница в позиции {j}:")
                    print(f"    наш='{r[j]}' (код {ord(r[j])})")
                    print(f"    hexlet='{e[j]}' (код {ord(e[j])})")
                    break
        break
