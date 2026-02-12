import sys
sys.path.insert(0, '.')

print("Быстрый тест")
print("=" * 50)

# Импортируем
from hexlet_code.scripts.generate_diff import generate_diff

# Тест 1: stylish с JSON
print("\n1. Stylish форматтер (JSON):")
result = generate_diff('test_data/file1.json', 'test_data/file2.json', 'stylish')
expected = open('test_data/expected_result_json.txt').read().strip()

if result.strip() == expected:
    print("✅ Пройден")
else:
    print("❌ Не пройден")
    print("Первые 3 строки различий:")
    for r, e in zip(result.strip().split('\n')[:3], expected.split('\n')[:3]):
        if r != e:
            print(f"  Наш: {r}")
            print(f"  Ожид: {e}")

# Тест 2: stylish с YAML
print("\n2. Stylish форматтер (YAML):")
result = generate_diff('test_data/file1.yaml', 'test_data/file2.yaml', 'stylish')
expected = open('test_data/expected_result_yaml.txt').read().strip()

if result.strip() == expected:
    print("✅ Пройден")
else:
    print("❌ Не пройден")

# Тест 3: plain форматтер
print("\n3. Plain форматтер:")
try:
    result = generate_diff('test_data/file1.json', 'test_data/file2.json', 'plain')
    expected = open('test_data/expected_result_plain.txt').read().strip()
    
    if result.strip() == expected:
        print("✅ Пройден")
    else:
        print("❌ Не пройден")
        print("Начало результата (50 символов):", result[:50])
        print("Начало ожидаемого (50 символов):", expected[:50])
except Exception as e:
    print(f"❌ Ошибка: {e}")

# Тест 4: json форматтер
print("\n4. JSON форматтер:")
try:
    result = generate_diff('test_data/file1.json', 'test_data/file2.json', 'json')
    expected = open('test_data/expected_result_json_format.txt').read().strip()
    
    # Проверяем как JSON
    import json
    parsed_result = json.loads(result)
    parsed_expected = json.loads(expected)
    
    if parsed_result == parsed_expected:
        print("✅ Пройден (данные совпадают)")
    else:
        print("❌ Не пройден (данные различаются)")
except Exception as e:
    print(f"❌ Ошибка: {e}")

print("\n" + "=" * 50)
