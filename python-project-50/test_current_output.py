import sys
sys.path.insert(0, '.')

from hexlet_code.scripts.gendiff import generate_diff

result = generate_diff('test_data/file1.json', 'test_data/file2.json')
print("Наш текущий вывод:")
print(result)

# Сохраним для сравнения
with open('current_output.txt', 'w') as f:
    f.write(result)
