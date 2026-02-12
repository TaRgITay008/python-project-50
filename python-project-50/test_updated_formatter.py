import sys
sys.path.insert(0, '.')

from hexlet_code.scripts.gendiff import generate_diff
import os

# Тест для JSON файлов
print("Тест для JSON файлов:")
result_json = generate_diff('test_data/file1.json', 'test_data/file2.json')
expected_json = open('test_data/expected_result_json.txt', 'r').read()

if result_json.strip() == expected_json.strip():
    print("✅ JSON тест пройден")
else:
    print("❌ JSON тест не пройден")
    # Покажем первые различия
    result_lines = result_json.strip().split('\n')
    expected_lines = expected_json.strip().split('\n')
    for i, (r, e) in enumerate(zip(result_lines, expected_lines)):
        if r != e:
            print(f"Различие в строке {i}:")
            print(f"  Наш: '{r}'")
            print(f"  Ожидаемый: '{e}'")
            break

# Тест для YAML файлов
print("\nТест для YAML файлов:")
result_yaml = generate_diff('test_data/file1.yaml', 'test_data/file2.yaml')
expected_yaml = open('test_data/expected_result_yaml.txt', 'r').read()

if result_yaml.strip() == expected_yaml.strip():
    print("✅ YAML тест пройден")
else:
    print("❌ YAML тест не пройден")
    result_lines = result_yaml.strip().split('\n')
    expected_lines = expected_yaml.strip().split('\n')
    for i, (r, e) in enumerate(zip(result_lines, expected_lines)):
        if r != e:
            print(f"Различие в строке {i}:")
            print(f"  Наш: '{r}'")
            print(f"  Ожидаемый: '{e}'")
            break

# Тест для форматтера plain
print("\nТест для форматтера 'plain':")
result_plain = generate_diff('test_data/file1.json', 'test_data/file2.json', formatter='plain')
expected_plain = open('test_data/expected_result_plain.txt', 'r').read()

if result_plain.strip() == expected_plain.strip():
    print("✅ Plain форматтер тест пройден")
else:
    print("❌ Plain форматтер тест не пройден")

# Тест для форматтера json
print("\nТест для форматтера 'json':")
result_json_fmt = generate_diff('test_data/file1.json', 'test_data/file2.json', formatter='json')
expected_json_fmt = open('test_data/expected_result_json_format.txt', 'r').read()

if result_json_fmt.strip() == expected_json_fmt.strip():
    print("✅ JSON форматтер тест пройден")
else:
    print("❌ JSON форматтер тест не пройден")
