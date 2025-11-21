import os
import sys

# Диагностика импортов
try:
    from gendiff import generate_diff
    print("DEBUG: Using gendiff import")
except ImportError:
    try:
        from hexlet_code import generate_diff
        print("DEBUG: Using hexlet_code import")
    except ImportError:
        try:
            from hexlet_code.scripts.gendiff import generate_diff
            print("DEBUG: Using hexlet_code.scripts.gendiff import")
        except ImportError as e:
            print(f"DEBUG: All imports failed: {e}")
            sys.exit(1)

def get_fixture_path(filename):
    return os.path.join(os.path.dirname(__file__), 'fixtures', filename)

def read_fixture(filename):
    with open(get_fixture_path(filename)) as f:
        return f.read()

def test_gendiff():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    expected = read_fixture('result_stylish.txt')
    result = generate_diff(file1, file2)
    assert result == expected, f"Expected: {expected}, Got: {result}"
