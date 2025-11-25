import os
import pytest
from gendiff import generate_diff

def get_path(filename):
    return os.path.join(os.path.dirname(__file__), 'fixtures', filename)

def read_fixture(filename):
    with open(get_path(filename)) as f:
        return f.read()

# Читаем ожидаемый результат ИЗ ФАЙЛА (как в логах Hexlet)
with open(get_path('result_stylish.txt'), 'r') as f:
    result_stylish = f.read()

test_cases = ['json', 'yml']

@pytest.mark.parametrize("format", test_cases)
def test_generate_diff(format):
    file_path1 = get_path(f"file1.{format}")
    file_path2 = get_path(f"file2.{format}")
    
    assert isinstance(
        generate_diff, type(lambda: None)
    ), "gendiff.generate_diff должна быть функцией"
    assert generate_diff(file_path1, file_path2) == result_stylish
