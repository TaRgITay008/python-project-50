### Hexlet tests and linter status:

[![Actions Status](https://github.com/TaRgITay008/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/TaRgITay008/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/ВАШ_CODE_CLIMATE_ID/maintainability)](https://codeclimate.com/github/TaRgITay008/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/ВАШ_CODE_CLIMATE_ID/coverage)](https://codeclimate.com/github/TaRgITay008/python-project-50/test_coverage)

# Gendiff - Генератор различий JSON и YAML

Командная утилита и Python библиотека для поиска различий между двумя JSON или YAML файлами конфигураций.

## Установка

```bash
# Установка в режиме разработки
git clone https://github.com/TaRgITay008/python-project-50.git
cd python-project-50
uv sync

# Или установка пакета глобально (после сборки)
uv tool install .

### JSON формат

```bash
uv run gendiff -f json file1.json file2.json
```

Вывод (пример структуры):
```json
{
  "common": {
    "type": "nested",
    "children": {
      "follow": {
        "type": "added", 
        "value": false
      },
      "setting1": {
        "type": "unchanged",
        "value": "Value 1"
      },
      "setting2": {
        "type": "removed", 
        "value": 200
      },
      "setting3": {
        "type": "changed",
        "old_value": true,
        "new_value": null
      }
    }
  }
}
```

## Демонстрация

### Asciinema запись

[![asciicast](https://asciinema.org/a/Pe6QypnLEmFWssNAjCOJN1iii.svg)](https://asciinema.org/a/Pe6QypnLEmFWssNAjCOJN1iii)

*Демонстрация показывает работу всех трех форматов вывода: stylish, plain и json*

### Примеры вывода

#### Stylish формат (по умолчанию)

```bash
uv run gendiff file1.json file2.json

