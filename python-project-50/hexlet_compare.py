from hexlet_code.scripts.generate_diff import generate_diff

# Наш текущий вывод
our_result = generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml')

# Ожидаемый вывод из ошибки Hexlet (скопируем из лога тестов)
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
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
    group4: {
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
    }
}
'''

print("СОВПАДАЕТ С HEXLET:", our_result == expected_hexlet)

if our_result != expected_hexlet:
    print("\n=== ТОЧНЫЕ РАЗЛИЧИЯ ===")
    our_lines = our_result.splitlines()
    hex_lines = expected_hexlet.splitlines()
    
    for i in range(min(len(our_lines), len(hex_lines))):
        if our_lines[i] != hex_lines[i]:
            print(f"Строка {i+1}:")
            print(f"  Наш:    {repr(our_lines[i])}")
            print(f"  Hexlet: {repr(hex_lines[i])}")
            # Покажем разницу в символах
            min_len = min(len(our_lines[i]), len(hex_lines[i]))
            for j in range(min_len):
                if our_lines[i][j] != hex_lines[i][j]:
                    print(f"    Символ {j}: наш '{our_lines[i][j]}' vs hexlet '{hex_lines[i][j]}'")
            break
