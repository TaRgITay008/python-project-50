from hexlet_code.parsers import parse_data
from hexlet_code.scripts.find_diff import find_diff

# Загрузим данные
data1 = parse_data('tests/fixtures/file1.yml')
data2 = parse_data('tests/fixtures/file2.yml')

# Создадим diff
diff = find_diff(data1, data2)

# Выведем структуру diff для отладки
def print_diff_structure(diff, level=0):
    indent = "  " * level
    for item in diff:
        print(f"{indent}{item['name']} ({item['action']})")
        if item['action'] == 'nested':
            print_diff_structure(item['children'], level + 1)

print("=== СТРУКТУРА DIFF ===")
print_diff_structure(diff)

# Проверим конкретно group4
print("\n=== GROUP4 STRUCTURE ===")
group4 = [item for item in diff if item['name'] == 'group4'][0]
print(f"Group4 action: {group4['action']}")
if group4['action'] == 'nested':
    for child in group4['children']:
        print(f"  {child['name']} ({child['action']})")
        if child['name'] == 'nest' and child['action'] == 'nested':
            for nested_child in child['children']:
                print(f"    {nested_child['name']} ({nested_child['action']})")
