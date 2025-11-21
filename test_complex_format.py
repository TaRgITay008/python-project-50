import json
from hexlet_code import generate_diff

# Создадим временные файлы с complex структурами как в Hexlet тестах
complex1 = {
    "common": {
        "setting1": "Value 1",
        "setting2": 200,
        "setting3": True,
        "setting6": {
            "key": "value", 
            "doge": {
                "wow": "too much"
            }
        }
    },
    "group1": {
        "baz": "bas",
        "foo": "bar",
        "nest": {
            "key": "value"
        }
    },
    "group2": {
        "abc": 12345,
        "deep": {
            "id": 45
        }
    }
}

complex2 = {
    "common": {
        "follow": False,
        "setting1": "Value 1",
        "setting3": {
            "key": "value"
        },
        "setting4": "blah blah",
        "setting5": {
            "key5": "value5"
        },
        "setting6": {
            "key": "value",
            "ops": "vops",
            "doge": {
                "wow": "so much"
            }
        }
    },
    "group1": {
        "foo": "bar",
        "baz": "bars", 
        "nest": "str"
    },
    "group3": {
        "deep": {
            "id": {
                "number": 45
            }
        },
        "fee": 100500
    }
}

with open('complex1.json', 'w') as f:
    json.dump(complex1, f, indent=2)

with open('complex2.json', 'w') as f:
    json.dump(complex2, f, indent=2)

result = generate_diff('complex1.json', 'complex2.json')
print('COMPLEX RESULT:')
print(repr(result))
print('ACTUAL:')
print(result)

# Очистка
import os
os.remove('complex1.json')
os.remove('complex2.json')
