from src.gendiff.formatters.plain import render_plain

# Простая тестовая структура
test_diff = {
    'children': [
        {
            'key': 'common',
            'type': 'nested', 
            'children': [
                {'key': 'follow', 'type': 'added', 'value': False},
                {'key': 'setting1', 'type': 'unchanged', 'value': 'Value 1'},
                {'key': 'setting2', 'type': 'removed', 'value': 200}
            ]
        }
    ]
}

result = render_plain(test_diff)
print("RESULT:")
print(result)
