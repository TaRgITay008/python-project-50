import json


def format_diff_json(diff):
    # Функция для преобразования action в формат Hexlet
    def convert_action(action):
        action_map = {
            'added': 'added',
            'removed': 'deleted',  # <-- важно!
            'changed': 'modified', # <-- важно!
            'unchanged': 'unchanged',
            'nested': 'nested'
        }
        return action_map.get(action, action)
    
    # Функция для рекурсивного преобразования всех action
    def convert_actions(obj):
        if isinstance(obj, dict):
            new_dict = {}
            for key, value in obj.items():
                if key == 'action':
                    new_dict[key] = convert_action(value)
                else:
                    new_dict[key] = convert_actions(value)
            return new_dict
        elif isinstance(obj, list):
            return [convert_actions(item) for item in obj]
        else:
            return obj

    converted_diff = convert_actions(diff)
    return json.dumps(converted_diff, indent=4)
