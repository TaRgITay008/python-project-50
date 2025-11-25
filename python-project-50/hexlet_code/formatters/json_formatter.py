import json


def format_diff_json(diff):
    # Функция для рекурсивной сортировки ключей в нужном порядке
    def sort_keys(obj):
        if isinstance(obj, dict):
            # Сортируем ключи в нужном порядке: action, name, затем остальные
            sorted_dict = {}
            # Сначала добавляем action если есть
            if 'action' in obj:
                sorted_dict['action'] = obj['action']
            # Затем name если есть  
            if 'name' in obj:
                sorted_dict['name'] = obj['name']
            # Затем остальные ключи в алфавитном порядке
            for key in sorted(obj.keys()):
                if key not in ['action', 'name']:
                    sorted_dict[key] = sort_keys(obj[key])
            return sorted_dict
        elif isinstance(obj, list):
            return [sort_keys(item) for item in obj]
        else:
            return obj
    
    sorted_diff = sort_keys(diff)
    return json.dumps(sorted_diff, indent=4)
