import sys
sys.path.insert(0, '.')

print("=" * 70)
print("КОМПЛЕКСНЫЙ ТЕСТ ВСЕХ ФУНКЦИОНАЛЬНОСТЕЙ")
print("=" * 70)

# Импортируем все необходимое
try:
    from hexlet_code.scripts.generate_diff import generate_diff
    print("✅ Импорт generate_diff успешен")
    
    from hexlet_code.formatters.stylish import format_stylish
    from hexlet_code.formatters.plain import format_plain
    from hexlet_code.formatters.json_formatter import format_json
    print("✅ Импорт всех форматеров успешен")
    
except Exception as e:
    print(f"❌ Ошибка импорта: {e}")
    sys.exit(1)

def compare_results(result, expected, test_name):
    """Сравнивает результат с ожидаемым значением"""
    result = result.strip()
    expected = expected.strip()
    
    if result == expected:
        print(f"✅ {test_name}")
        return True
    else:
        print(f"❌ {test_name}")
        
        # Найдем первое отличие
        result_lines = result.split('\n')
        expected_lines = expected.split('\n')
        
        for i in range(min(len(result_lines), len(expected_lines))):
            if result_lines[i] != expected_lines[i]:
                print(f"   Первое отличие в строке {i}:")
                print(f"   Наш:     '{result_lines[i]}'")
                print(f"   Ожидаем: '{expected_lines[i]}'")
                break
        
        return False

# ТЕСТ 1: stylish форматтер с JSON
print("\n" + "-" * 70)
print("ТЕСТ 1: stylish форматтер с JSON файлами")
print("-" * 70)

with open('test_data/expected_result_json.txt', 'r') as f:
    expected_stylish_json = f.read()

result_stylish_json = generate_diff('test_data/file1.json', 'test_data/file2.json', formatter='stylish')
compare_results(result_stylish_json, expected_stylish_json, "stylish JSON")

# ТЕСТ 2: stylish форматтер с YAML
print("\n" + "-" * 70)
print("ТЕСТ 2: stylish форматтер с YAML файлами")
print("-" * 70)

with open('test_data/expected_result_yaml.txt', 'r') as f:
    expected_stylish_yaml = f.read()

result_stylish_yaml = generate_diff('test_data/file1.yaml', 'test_data/file2.yaml', formatter='stylish')
compare_results(result_stylish_yaml, expected_stylish_yaml, "stylish YAML")

# ТЕСТ 3: plain форматтер
print("\n" + "-" * 70)
print("ТЕСТ 3: plain форматтер")
print("-" * 70)

with open('test_data/expected_result_plain.txt', 'r') as f:
    expected_plain = f.read()

try:
    result_plain = generate_diff('test_data/file1.json', 'test_data/file2.json', formatter='plain')
    compare_results(result_plain, expected_plain, "plain форматтер")
except Exception as e:
    print(f"❌ Ошибка в plain форматтере: {e}")

# ТЕСТ 4: json форматтер
print("\n" + "-" * 70)
print("ТЕСТ 4: json форматтер")
print("-" * 70)

with open('test_data/expected_result_json_format.txt', 'r') as f:
    expected_json = f.read()

try:
    result_json = generate_diff('test_data/file1.json', 'test_data/file2.json', formatter='json')
    
    # Для JSON можем проверить как строки и как JSON
    if result_json.strip() == expected_json.strip():
        print("✅ json форматтер (точное совпадение строк)")
    else:
        # Попробуем сравнить как JSON объекты
        try:
            import json
            parsed_result = json.loads(result_json)
            parsed_expected = json.loads(expected_json)
            
            if parsed_result == parsed_expected:
                print("✅ json форматтер (данные совпадают, форматирование разное)")
            else:
                print("❌ json форматтер (данные различаются)")
                print(f"   Результат: {result_json[:100]}...")
                print(f"   Ожидаемый: {expected_json[:100]}...")
        except json.JSONDecodeError as je:
            print(f"❌ Ошибка парсинга JSON: {je}")
            print(f"   Результат (первые 200 символов): {result_json[:200]}")
except Exception as e:
    print(f"❌ Ошибка в json форматтере: {e}")

print("\n" + "=" * 70)
print("ИТОГОВЫЙ ОТЧЕТ")
print("=" * 70)
